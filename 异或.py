payload = "_GET"
flag = []

for i in payload:
	for j in range(1,256):
		if (j ^ 254) == ord(i):
			flag.append(hex(j))
			break

for x in flag:
	print(x.replace("0x", "%"), end="")
