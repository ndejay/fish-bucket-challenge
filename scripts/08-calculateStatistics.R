#!/usr/bin/env Rscript

library('stringr')

video_list <- Sys.glob('../data/input_videos/*')
capture <- lapply(video_list, function (x) {
  video_basename <- str_match(x, ".*/([0-9 .-_a-zA-Z]*)")[2]
  interpolation <- read.csv(paste('../data/PIPELINE/dataimages', video_basename, sep = ''))
  interpolation[, 1] <- as.numeric(interpolation[, 1])
  interpolation[, 2] <- as.numeric(interpolation[, 2])

  distance <- Reduce(f = c, x = sapply(1:(nrow(interpolation) - 1), function (i) {
    j <- i + 1
    d_x <- (interpolation[i, 1] - interpolation[j, 1]) ** 2
    d_y <- (interpolation[i, 2] - interpolation[j, 2]) ** 2
    sqrt(sum(d_x, d_y))
  }))
  out <- data.frame('X'              = interpolation[, 1],
                    'Y'              = interpolation[, 2],
                    'DISTANCE'       = c(NA, distance),
                    'MAX_DISTANCE'   = max(distance, na.rm = TRUE),
                    'MEAN_DISTANCE'  = mean(distance, na.rm = TRUE),
                    'TOTAL_DISTANCE' = sum(distance, na.rm = TRUE))
  output_file <- paste('../data/output_videos/', video_basename, '-stats.csv', sep = '')
  write.csv(x = out, file = output_file, row.names = F)

  NULL
})
