#!/usr/bin/bash
input_file="twitter_dataset.csv"
if [ ! -f "$input_file" ]; then
	echo "Error: File doesn't exist"
	exit 1
fi

echo "Top 5 active users: "

grep -E '^[0-9]' "$input_file" \
	    | cut -d',' -f2 \
	    | sort \
            | uniq -c \
            | sort -rn \
	    | head -n 5 \
	    | awk '{print $1, $2}'

