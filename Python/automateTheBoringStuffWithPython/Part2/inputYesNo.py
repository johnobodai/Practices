#!/usr/bin/python3
# Program to keep an idiot busy for hours
import pyinputplus as pyin
while True:
    prompt = 'What to know how to keep an idiot busy for hours?\n'
    response = pyin.inputYesNo(prompt)
    if response == 'no':
        break
print('Thank you, Have a nice day.')
