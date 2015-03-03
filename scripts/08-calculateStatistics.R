#!/usr/bin/env Rscript

library('stringr')

video_list <- Sys.glob('../data/input_videos/*')
capture <- lapply(video_list, function (x) {
  video_basename <- str_match(x, ".*/([0-9 .-_a-zA-Z]*)")[2]
  interpolation <- read.csv(paste('../data/PIPELINE/dataimages', video_basename, '-interpolated', sep = ''))
  interpolation[, 1] <- as.numeric(interpolation[, 1])
  interpolation[, 2] <- as.numeric(interpolation[, 2])

  velocity <- Reduce(f = c, x = sapply(1:(nrow(interpolation) - 1), function (i) {
    j <- i + 1
    sqrt( sum(interpolation[i, 1:2]**2 - interpolation[j, 1:2]**2) )
  }))
  output_file <- paste('../data/output_videos/', video_basename, '-velocity.csv', sep = '')
  write.csv(x = velocity, file = output_file, row.names = F)

  meanVelocity <- mean(velocity, na.rm = TRUE)
  output_file <- paste('../data/output_videos/', video_basename, '-meanVelocity.csv', sep = '')
  write.csv(x = meanVelocity, file = output_file, row.names = F)

  NULL
})
