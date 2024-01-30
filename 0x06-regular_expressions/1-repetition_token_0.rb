#!/usr/bin/env ruby
# A regular expression that will match the specified cases
puts ARGV[0].scan(/hbt{2,5}n/).join
