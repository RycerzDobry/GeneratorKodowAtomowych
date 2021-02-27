import sys
import time
import os

filenames = ["kody1.txt", "kody2.txt", "kody3.txt", "kody4.txt"]
frames = []

message1 = 'czy chcesz rozpocząć? [t/n]\n'
message2 = 'rozpoczynam...'
message3 = 'twój kod: '
message4 = 'wyłączenie za: '
message5 = 'jak nie to nie... '
message6 = 'tchórzu'
odliczanie1 = '3...'
odliczanie2 = '2...'
odliczanie3 = '1...'

def pisanie(message):
	for char in message:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.05)
