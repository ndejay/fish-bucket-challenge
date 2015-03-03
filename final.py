#!/usr/bin/env python

from scripts.Image import Image
import numpy as np
import os

video_container = "data/images"
video_list      = os.listdir("%s" % video_container)

for video in video_list:
  image_container = "%s/%s" % (video_container, video)
  image_list      = os.listdir("%s" % image_container)

  interpolation_filename = "data/PIPELINE/dataimages%s-interpolated" % video
  interpolation = np.loadtxt(interpolation_filename, delimiter = ",")[::-1]

  for i in xrange(0, len(image_list)):
    static_image_filename  = "%s/%s" % (image_container, image_list[i])
    static_image = Image().load(static_image_filename)

    try:
        os.mkdir("data/PIPELINE/%s" % video)
    except:
        pass

    final_image_filename   = "data/PIPELINE/%s/%s" % (video, image_list[i])
    static_image.saveFigWithTrajectory(final_image_filename, interpolation[0:i])




