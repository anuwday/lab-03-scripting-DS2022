#!/bin/bash
set -euo pipefail

BUNDLE_URL="https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz"
curl -s -L -O "$BUNDLE_URL"

tar -xzf lab3-bundle.tar.gz
awk '!/^[[:space:]]*$/' lab3_data.tsv > cleaned.tsv

tr '\t' ',' < cleaned.tsv > cleaned_data.csv

ROW_COUNTS=$(( $(wc -l < cleaned_data.csv) - 1 ))

echo "${ROW_COUNTS} line(s) of data remain in the cleaned file."

tar -czf converted-archive.tar.gz cleaned_data.csv
