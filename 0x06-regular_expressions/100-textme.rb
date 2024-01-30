#!/usr/bin/env ruby

# Get the log entry from the command line argument
log_entry = ARGV[0]

# Extract sender, receiver, and flags using regex
match_data = log_entry.match(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)

# Check if the match was successful
if match_data
  sender = match_data[1]
  receiver = match_data[2]
  flags = match_data[3]

  # Output structured result
  puts "Sender: #{sender}, Receiver: #{receiver}, Flags: #{flags}"
else
  puts "No match found in the log entry."
end
