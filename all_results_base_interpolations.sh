#!/bin/bash

mkdir -p data/results_base_interpolations
for f in data/results_base/*.avi ; do
    echo "$f"
    scripts/interpolate_fish_positions.py "$f" "data/results_base_interpolations/$(echo "$f" | sed 's/\///g')" 5-25 &
done


wait
