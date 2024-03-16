#!/bin/bash

# ENV
TARGET_HOST="http://172.16.0.12:8000"
ENDPOINT="/display"

if [ "$1" = "Get" ]; then
	response=$(curl -s -X GET ${TARGET_HOST}${ENDPOINT})

	# Parse response and echo result
	state=$(echo $response | jq -r '.state')
	if $state; then
		echo 1
	else
		echo 0
	fi
elif [ "$1" = "Set" ]; then
	# Set state
	if [ "$4" = "1" ]; then
		curl -s -X POST ${TARGET_HOST}${ENDPOINT} -d '{"state": true}'
	else
		curl -s -X POST ${TARGET_HOST}${ENDPOINT} -d '{"state": false}'
	fi
fi
