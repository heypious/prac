# Add Roll Number, Name and Age in stu.csv file and display it.
import csv
db = open('stu.csv', 'w')
writer = csv.writer(db)
to_add = eval(input('Enter [Roll No, Name, Age]: '))
writer.writeline(to_add)
db.close()
with open('stu.csv', 'r') as db:
    reader = csv.reader(db)
    for record in reader:
        print(record)
