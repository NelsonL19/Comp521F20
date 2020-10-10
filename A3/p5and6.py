import sqlite3
import time
db = sqlite3.connect('NCCOVID19 copy.db')
cursor = db.cursor()






sql = '''CREATE INDEX i_cvfips ON Covid19(cases, date, fips)'''
cursor.execute(sql)


finalrow = []
  
sql = '''SELECT C1.name, C2.name, V1.date, V1.cases 
         FROM County C1, Covid19 V1, County C2, Covid19 V2
         WHERE C1.fips=V1.fips AND C2.fips=V2.fips
          AND V1.cases=V2.cases AND V1.date=V2.date 
          AND V1.fips < V2.fips AND V1.cases >= 1'''

startTime = time.perf_counter()

cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
    finalrow.append(row)

endTime = time.perf_counter()
totalTime = endTime - startTime

print(totalTime)
print(len(rows))


sql = '''DROP INDEX i_cvfips'''
cursor.execute(sql)




#0.0122789 Seconds
#26826 Rows