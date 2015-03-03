#!/bin/bash

mkdir -p data/PIPELINE
for f in data/images/*.avi ; do
    echo "$f"
    outfile="data/PIPELINE/$(echo "$f" | sed 's/\///g')"
    ./driver.py "$f" "$outfile"
done
