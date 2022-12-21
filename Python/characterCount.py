#!/usr/bin/python3
# Counts the number of individual characters in a string inputed my a user:
import pprint

message = input('Input your string to be counted here: ')
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
pprint.pprint(count)
