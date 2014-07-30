aplhabets = {}
aplhabets = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H': 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' :24, 'Y' : 25, 'Z' : 26 }


new_deck = []
for x in range(1, 55):
	new_deck.append(x)


new_message = raw_input("write the new text for encryption")
new_message = new_message.upper()

key_stream = raw_input("insert key stream")
key_stream = key_stream.upper()

new_message_num = []
for item in new_message:
	for x, y in aplhabets.iteritems():
		if item == x:
			new_message_num.append(y) 	

key_stream_num = []
for item in key_stream:
	for x, y in aplhabets.iteritems():
		if item == x:
			key_stream_num.append(y)

encrypt_num = []
for x in range (0, len(new_message)):
	encrypt_num_new = int(new_message_num[x]) + int(key_stream_num[x])
	encrypt_num_new = encrypt_num_new % 26
	encrypt_num.append(encrypt_num_new)

encrypt = []
for item in encrypt_num:
	for x, y in alphabets.iteritems():
		if item == y:
			encrypt.append(x)
print encrypt
