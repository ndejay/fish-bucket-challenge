#!/bin/bash

mkdir -p data/PIPELINE
for f in data/images/*.avi ; do
    echo "$f"
    outfile="data/PIPELINE/$(echo "$f" | sed 's/\///g')"
    ./driver.py "$f" "$outfile"
    scripts/interpolate_path.py "$outfile" "$outfile-interpolated"
done
