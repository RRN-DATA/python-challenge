import sys, csv

Contestant = []
candiDic = {}
count = 0
with open("election_data.csv", "r") as input:
	r = csv.reader(input)
	next(r, None)
	row_count = sum(1 for row in r)
input.close()
with open("election_data.csv", "r") as data:
	read = csv.reader(data, delimiter=',')
	next(read, None)	
	for row in read:
		if row[2] not in Contestant:
			Contestant.append(row[2])
data.close()
with open("election_data.csv", "r") as content:
	r = csv.reader(content)
	next(r, None)
	for elem in r:
		if elem[2] not in candiDic:
			candiDic[elem[2]] = 0
		candiDic[elem[2]] = candiDic[elem[2]] + 1

maxVal = 0
for elem in candiDic:
        if (int(candiDic[elem])>maxVal):
                maxVal = int(candiDic[elem])
                name = str(elem)

class Logger(object):
        def __init__(self):
                self.terminal = sys.stdout
                self.log = open("PyPollResult.txt", "a")

        def write(self, message):
                self.terminal.write(message)
                self.log.write(message)

        def flush(self):
                pass
sys.stdout = Logger()

	
print ("Election Results")
print ("----------------------------")
print ("Total Votes: ", row_count)
print ("----------------------------") 
for elem in candiDic:
        print (elem,":", round(float((candiDic[elem]/row_count)*100), 2), "%", "(", candiDic[elem], ")")
print ("----------------------------")
print ("Winner: ", name)
print ("----------------------------")

#print (Contestant)
content.close()
