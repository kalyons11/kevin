#!/usr/bin/env bash

# https://leetcode.com/problems/word-frequency/

FILENAME=$1

tr -s ' ' '\n' < $FILENAME \
    | sort \
    | uniq -c \
    | sort -r \
    | awk '{print $2" "$1}'
