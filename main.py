import pyfirmata
import time

board = pyfirmata.Arduino('COM3')

dot = 1
line = 3 * dot
pause = 3 * dot
long_pause = 7 * dot

message = 'SOS please help me'

alphabet = {
	'a': '*-',
	'b': '-***',
	'c': '-*-*',
	'd': '-**',
	'e': '*',
	'f': '**-*',
	'g': '--*',
	'h': '****',
	'i': '**',
	'j': '*---',
	'k': '-*-',
	'l': '*-**',
	'm': '--',
	'n': '-*',
	'o': '---',
	'p': '*--*',
	'q': '--*-',
	'r': '*-*',
	's': '***',
	't': '-',
	'u': '**-',
	'v': '***-',
	'w': '*--',
	'x': '-**-',
	'y': '-*--',
	'z': '--**',
	'1': '*----',
	'2': '**---',
	'3': '***--',
	'4': '****-',
	'5': '*****',
	'6': '-****',
	'7': '--***',
	'8': '---**',
	'9': '----*',
	'0': '-----',
}


for i in range(0, len(message)):
	# print(message[i] + ' ' + alphabet[message[i].lower()])
	print(message[i])
	if message[i].lower() == ' ':
		time.sleep(long_pause)
	else:
		for x in range(0, len(alphabet[message[i].lower()])):
			if alphabet[message[i].lower()][x] == '*':
				board.digital[13].write(1)
				time.sleep(dot)
				board.digital[13].write(0)
			elif alphabet[message[i].lower()][x] == '-':
				board.digital[13].write(1)
				time.sleep(line)
				board.digital[13].write(0)
			if x < len(alphabet[message[i].lower()]) - 1:
				time.sleep(dot)
		time.sleep(pause)
"""
while True:
	board.digital[13].write(1)
	time.sleep(1)
	board.digital[13].write(0)
	time.sleep(1)
	print(board.analog)
"""
