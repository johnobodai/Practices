#!/usr/bin/python3

message = input('Input your string to be counted here: ')
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
