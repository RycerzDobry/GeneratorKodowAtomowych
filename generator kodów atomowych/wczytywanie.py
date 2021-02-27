import os
import time
import random

os.system('cls')
filenames = ["kody1.txt", "kody2.txt", "kody3.txt", "kody4.txt"]
frames = []

print('\033[31m')
for nazwa in filenames:
	with open(nazwa,'r',encoding='utf8') as f:
		frames.append(f.readlines())
for i in range(20):
	for frame in frames:
		print(''.join(frame))
		time.sleep(0.2)
		os.system('cls')