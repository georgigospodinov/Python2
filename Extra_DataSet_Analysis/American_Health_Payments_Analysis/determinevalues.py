import csv

drgDef_list = []
providerId_list = []
providerName_list = []
providerStreet_list = []
providerCity_list = []
providerState_list = []
providerZip_list = []
hospRef_list = []
totalDischarges_list = []
avgCovered_list = []
avgTotal_list = []
avgMedicare_list = []
values_lists = [drgDef_list, providerId_list, providerName_list,
		providerStreet_list, providerCity_list, providerState_list,
		providerZip_list, hospRef_list, totalDischarges_list,
		avgCovered_list, avgTotal_list, avgMedicare_list]

def save_lists():
	"""
		Save the lists from the list of lists of values into "values.csv".
	"""
	f = open("values.csv", 'w')
	for vl in values_lists:
		length = len(vl)
		for i in range(length-1):
			f.write(vl[i])
			f.write(",")
		f.write(vl[length-1])
		f.write('\n')
	f.close()

def create_lists():
	"""
		Create the list of lists of values by reading from "reformatted.csv".
	"""
	rc = 0
	cc = 1
	infile = csv.reader(open("reformatted.csv"))
	infile.__next__()  # Ignore header
	for row in infile:
		if rc == 1000:
			print(cc)
			cc = cc+1
			rc = 0
		for i in range(len(row)):
			v = row[i]
			if v not in values_lists[i]:
				# Put quotes to avoid splitting a string because of commas in it.
				values_lists[i].append("\""+v+"\"")
		rc = rc+1

def determine():
	"""
		Create and save the lists of values by calling the other two functions.
	"""
	create_lists()
	save_lists()
