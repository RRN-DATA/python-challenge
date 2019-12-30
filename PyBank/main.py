import csv
import os, sys
total = 0
firstLine = True
with open("budget_data.csv") as csvfile:
	for row in csv.reader(csvfile):
		if firstLine:
			firstLine = False
			continue
		total += int(row[1])
csvfile.close()

with open("budget_data.csv") as cf:
	reader = csv.reader(cf, delimiter=",")
	next(reader, None)
	data = list(reader)
	row_count = len(data)
cf.close()

f = open('budget_data.csv','r')
r = csv.reader(f)
next(r, None)
k=0
deltaList = []
deltadic = {}
diffSigma=0
for i in r:
	if (k==0):
		#List assignment when k=0
		listn=[i[1]]
	if (k > 0):
		#List assignment from row 3 onwards(including header in csv)
		#Assigning kth element to the list
		listn.append(i[1])
		#printing kth element of the list
		delta=float(listn[k])-float(listn[k-1])
		deltaList.append(delta)
		deltadic.update({i[0] : delta})
		diffSigma=diffSigma+delta
		
	k+=1
avg = float(diffSigma/(row_count-1))
keyMax = max(deltadic, key = deltadic.get)
keyMin = min(deltadic, key = deltadic.get)

class Logger(object):
	def __init__(self):
		self.terminal = sys.stdout
		self.log = open("PyBankResult.txt", "a")

	def write(self, message):
		self.terminal.write(message)
		self.log.write(message)

	def flush(self):
		pass
sys.stdout = Logger()

print ("Financial Analysis")
print ("-------------------------------")
print ("Total Months: ", row_count)
print ("Total: $",total)
print ("Average  Change: $", str(round(avg,2)))
print ("Greatest Increase in Profits: ", keyMax, "($", int(max(deltadic.values())),")")
print ("Greatest Decrease in Profits: ", keyMin, "($", int(min(deltadic.values())), ")")
f.close()
