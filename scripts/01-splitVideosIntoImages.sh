#!/usr/bin/env bash

# for each avi file in the data, we create a similarly named directory (without
# the avi file extension) and split out all the images there, in sequence.
for f in ../data/input_videos/*.avi ; do
    echo "$f"
    p="$(basename "$f")"
    d="../data/images/$p"
    mkdir -p "$d"
    # Specify the framerate and output file name format.
    ffmpeg -i "$f" -r 30 -f image2 "$d/static_%4d.png"
done
