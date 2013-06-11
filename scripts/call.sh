#!/bin/bash
#
NUMBER="01123456789"
LIMIT=10
CMD="originate SIP/${NUMBER}@powervoip application Playback monkeys"

for ((i=0; i < $LIMIT; i++)); do
        SLEEP=$(( RANDOM %= 1800 ))
        asterisk -r -x "$CMD"
        sleep ${SLEEP}
done
