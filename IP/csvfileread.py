import csv

with open('C:\\Users\\admin\\Desktop\\loanapp.csv') as csvFile:
    csvReader=csv.reader(csvFile,delimiter=',')
    #print(csvReader)
    #print(list(csvReader))
    names=[]
    stats=[]
    for row in csvReader:
        print(row[0])
        names.append(row[0])
        stats.append(row[1])

print(names)
print(stats)
Index=names.index('John')
loanStatus=stats[Index]
print('sam loan status is '+loanStatus)
