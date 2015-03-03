#!/usr/bin/env bash

for f in ../data/images/*.avi ; do
    echo "$f"
    p="$(basename "$f")"
    d="../data/output_videos/"
    mkdir -p "$d"
    echo ffmpeg -f image2 -i "$f"/final_%04d.png -r 12 -s WxH "$d$p"
done
