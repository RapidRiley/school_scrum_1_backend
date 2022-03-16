#! /bin/sh

while true
do
	SLEEP_TIMER=$(shuf -i 60-15400 -n 1)

	python3 /app/main.py

	echo "Batch created, sleeping for $SLEEP_TIMER seconds."
	sleep "$SLEEP_TIMER";
done
