import sqlite3

db = sqlite3.connect('./A4/NCCOVID19.db')
db.row_factory = sqlite3.Row
cursor = db.cursor()


#A function to get the hash-bucket pageid for records in Demographics table is provided below:

def getPageId(year, fips):
        return int((fips + 7*year) % 512)


#Q1

sql1 = 'SELECT year, fips FROM Demographics'
cursor.execute(sql1)
rows = cursor.fetchall()
#print(rows[1].keys())
#print(rows[1]['fips'])

buckets = {}
ofAmount = 0;
alreadyCaught = []

for row in rows:
        currId = getPageId(row['year'], row['fips']) 

        if currId not in buckets:
                arr = [{'year': row['year'], 'fips': row['fips'], 'pageId': currId}]
                buckets[currId] = arr
        else:
                newArr = {'year': row['year'], 'fips': row['fips'], 'pageId': currId}
                buckets[currId].append(newArr)

                if len(buckets[currId]) > 400:
                        if currId in alreadyCaught:
                                 pass
                        else:
                                ofAmount+=1
                                alreadyCaught.append(currId)       




print(ofAmount)
numer = 0
for x in buckets:
        numer+= len(buckets[x])
print(numer/512) #4.1015625



#Q2

#Q3

#Q4

#Q5

#Q6

#Q7

#Q8