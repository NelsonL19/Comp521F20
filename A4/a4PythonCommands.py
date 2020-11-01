import sqlite3

db = sqlite3.connect('./A4/NCCOVID19.db')
db.row_factory = sqlite3.Row
cursor = db.cursor()


#A function to get the hash-bucket pageid for records in Demographics table is provided below:

def getPageId(year, fips):
        return int((fips + 7*year) % 512)


#Q1

sql1 = 'SELECT year, fips FROM Demographics GROUP BY year, fips'
cursor.execute(sql1)
rows = cursor.fetchall()
print(len(rows))




#Q2

#Q3

#Q4

#Q5

#Q6

#Q7

#Q8