import csv

input_file = "reformatted.csv"
temp_file = "temp"  # when complete, rename to 'values.csv'
delim = ","
precision = 1000

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
	f = open(temp_file, 'w')
	for vl in values_lists:
		length = len(vl)
		for i in range(length-1):
			f.write(vl[i])
			f.write(delim)
		f.write(vl[length-1])
		f.write('\n')
	f.close()

def create_lists():
	rc = 0
	infile = csv.reader(open(input_file))
	infile.__next__()  # Ignore header
	for row in infile:
		for i in range(len(row)):
			v = row[i]
			if v not in values_lists[i]:
				values_lists[i].append("\""+v+"\"")

def determine():
	create_lists()
	save_lists()
	for i in range(len(values_lists)):
		print(i, len(values_lists[i]))
