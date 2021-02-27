import random
import os
import time
from CONFIG import *

os.system('cls')
time.sleep(3)
k = open('generator_nazwa.txt', encoding='utf8')
nazwa = k.read()
print(nazwa)
k.close()

time.sleep(2)
pisanie(message1)
rozpoczynanie = input()
if rozpoczynanie == 't':
	print('\033[32m', end='')
	pisanie(message2)
	print('\033[39m')
	time.sleep(1.5)
	os.system('cls')
	print('\033[31m')
	for nazwa in filenames:
		with open(nazwa,'r',encoding='utf8') as f:
			frames.append(f.readlines())
	for i in range(20):
		for frame in frames:
			print(''.join(frame))
			time.sleep(0.2)
			os.system('cls')
	print('\033[32m' + 'GOTOWE' + '\033[39m')
	time.sleep(2)
	kod = str(random.randrange(100000, 999999))
	pisanie(message3)
	print('\033[31m', end='')
	pisanie(kod)
	print('\033[39m')
	time.sleep(1)
	pisanie(message4)
	time.sleep(0.5)
	pisanie(odliczanie1)
	time.sleep(1.5)
	pisanie(odliczanie2)
	time.sleep(1.5)
	pisanie(odliczanie3)
	time.sleep(1.5)
	os.system('cls')
	exit()
elif rozpoczynanie == 'n':
	pisanie(message5)
	time.sleep(0.6)
	pisanie(message6)
	time.sleep(0.6)
	os.system('cls')
	exit()
else:
	print('\033[31m' + 'BŁĄD KRYTYCZNY' + '\033[39m')
	time.sleep(2)
	os.system('cls')
	exit()
