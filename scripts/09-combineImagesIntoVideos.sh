#!/usr/bin/env bash

IFS=$'\n'
for f in ../data/input_videos/*.avi ; do
    echo "$f"
    p="$(basename "$f")"
    d="../data/output_videos/"
    mkdir -p "$d"
    ffmpeg -i "../data/PIPELINE/$p/static_%4d.png" -c:v libx264 -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -r 30 -pix_fmt yuv420p "$d${p/avi/mp4}" &
done

wait
