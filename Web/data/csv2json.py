#!/usr/bin/python
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
		if (header[i] in ["orig_upb", "curr_upb", "orig_p_i", "orig_rate",
			"is_adjustable", "advance_amt", "funding_method_code",
			"funding_id", "inv_commit_price", "lien_position", "original_ltv",
			"original_cltv", "mtg_ins_pct", "fico_score", "original_term",
			"amortization_term", "orig_appraised_value", "debt_service_ratio",
			"is_escrow_required", "armmargin", "armteaser", "anncap_init",
			"rate_change_frequency", "purchase_price", "reserved_amt",
			"Cur_note_rate", "Max_Rate", "CoreLogic Fraud Risk Score",
			"CoreLogic Collateral Risk Score"]):
			if row[i] == '':
				print '"' + header[i] + '":"' + row[i] + '"',
			else:
				print '"' + header[i] + '":' + row[i],
		else :
			print '"' + header[i] + '":"' + row[i] + '"',
		if i!=len(row) - 1:
			print ","
		else:
			print ""
	print "}",
print "]}"
f.close()
