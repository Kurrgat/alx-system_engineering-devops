#!/usr/bin/env ruby
# The script scans the input string for occurrences of the pattern 'hbt*n' and joins them together.
puts ARGV[0].scan(/hbt*n/).join
