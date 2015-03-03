#!/usr/bin/env python

import numpy as np

import sys
import os
import itertools as it

import matplotlib.pyplot as plt

from math import sqrt

THRESHOLD = 64.0 # max acceptable distance for the fish to travel between two diffs

def _flip( (x, y) ):
    return (y, x)

def maximum_outlier(frame):
    """ Find which blob is the maximum outlier in a frame of blobs. """
    best_blob = None
    for blob in frame:
        pairwise_dist_sum = 0
        y1, x1, r1 = blob

        # compare the blob to each of the others
        for blob2 in frame:
            if blob is not blob2:
                y2, x2, r2 = blob2
                # accumulate its pairwise distances
                pairwise_dist_sum += sqrt((x2 - x1)**2 + (y2 - y1)**2)

        # and we want to get the blob whose pairwise dist sum is the largest
        if best_blob is None:
            best_blob = (blob, pairwise_dist_sum)
        else:
            if best_blob[1] < pairwise_dist_sum:
                best_blob = (blob, pairwise_dist_sum)
    return best_blob[0]

def compute_trajectory(frames, fish):
    """ Given a list of frames to analyze and a starting blob for a fish in
        the first frame, compute its trajectory.
    """
    # start with the last frame.
    # We want to find the one that's the furthest away, according to the pairwise distance with the other blobs.
    last_frame = frames_with_cutoff[-1]

    best_blob = maximum_outlier(last_frame)

    # this best blob is in fact the last position of the fish (since we were looking at the last frame)
    reversed_fish_positions = [fish] # for better names

    def last_dist(blob):
        y1, x1, r1 = reversed_fish_positions[-1]
        y2, x2, r2 = blob
        return sqrt((x2 - x1)**2 + (y2 - y1)**2)

    for frame in reversed(frames_with_cutoff[:-1]):
        blobs_and_distances = filter(lambda x: x[1] <= THRESHOLD, it.imap(lambda x: (x, last_dist(x)), frame))

        if blobs_and_distances: # there needs to be at least one candidate fish, according to our threshold
            reversed_fish_positions.append(min(blobs_and_distances, key=lambda x: x[1])[0])

    return reversed_fish_positions

if __name__ == "__main__":
    # Create the figure and subplot for later use
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim(left=0, right=640)
    ax.set_ylim(top=0, bottom=480)

    # load the input data
    # All .csv files in the directory specified as the first command line argument are loaded
    input_paths = sorted([os.path.join(sys.argv[1], f) for f in os.listdir(sys.argv[1]) if f.endswith('.csv')])

    # The output file
    output_path = sys.argv[2]

    if len(sys.argv) == 4:
        cutoff_limit = map(int, sys.argv[4].split('-'))
    else:
        cutoff_limit = (0, 1)

    input_diffdata = map(lambda x: x if len(np.shape(x)) != 1 else np.array([x]), it.imap(lambda x: np.loadtxt(x, delimiter=','), input_paths))

    for cutoff in xrange(*cutoff_limit):
        print "Dropping the last", cutoff, "frames in interpolation."

        if cutoff == 0:
            frames_with_cutoff = input_diffdata
        else:
            frames_with_cutoff = input_diffdata[:-cutoff]

        traj = compute_trajectory(frames_with_cutoff, maximum_outlier(frames_with_cutoff[-1]))

        with open(output_path + str(cutoff), 'w') as f:
            for position in reversed(traj):
                f.write(','.join(map(str, position[:2])) + '\n')

        ax.plot(*zip(*map(lambda x: _flip(x[:2]), traj)))

    fig.savefig('data/asdf.png')

# vim: set ts=4 sw=4 expandtab
