#!/usr/bin/env python3
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url):
	"""Download GitHub data for user and parse as JSON.
	url points to GitHub API events.
	returns a list of dictionaries with event objects."""
	reply_text = requests.get(url).text
	return json.loads(reply_text)

def print_events(events,n=5):
	"""Prints event type and name for n events.
	events holds list of event dictionaries from GitHub,
	n holds number of events to print, defaulted at 5."""
	for x in events[:n]:
		event = x['type'] + ' :: ' + x['repo']['name']
		print(event)

def main():
	"""Show GitHub user details and print recent events."""
	print(GHUSER)
	print(url)
	event_list = retrieve_events(url)
	print_events(event_list)

if __name__ == '__main__':
	main()
