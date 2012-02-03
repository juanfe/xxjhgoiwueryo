#!//usr/bin/python
import csv
import json

#TODO, use ordereddict to order dict, and it will reduce the ammount con code
#there are a web page, google it: python, csv, json
f = open( 'FundingData.csv', 'r' )
reader = csv.reader(f)
header = reader.next()
print '{"Loans": ['

row = reader.next()
print "{",
for i in range(len(row)):
	print '"' + header[i] + '":"' + row[i] + '"',
	if i!=len(row) - 1:
		print ","
	else:
		print ""
print "}",

for row in reader:
	print ",{",
	for i in range(len(row)):
		print '"' + header[i] + '":"' + row[i] + '"',
		if i!=len(row) - 1:
			print ","
		else:
			print ""
	print "}",
print "]}"
f.close()
