#!/bin/bash

mkdir -p data/PIPELINE
for f in data/images/*.avi ; do
    echo "$f"
    ./driver.py "$f" "data/PIPELINE/$(echo "$f" | sed 's/\///g')"
done

wait
