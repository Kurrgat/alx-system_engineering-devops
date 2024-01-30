#!/usr/bin/env ruby

# Extracts sender, receiver, and flags from the log entry
match_data = ARGV[0].match(/\[from:(.*?)\].*\[to:(.*?)\].*\[flags:(.*?)\]/)

# Formats and outputs the result
puts "#{match_data[1]},#{match_data[2]},#{match_data[3]}"
