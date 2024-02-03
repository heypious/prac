# Write Roll Number, Name and Age into stu.dat binary file and display.
import pickle
db = file(open('stu.dat', 'ab'))
to_get = eval(input("[Roll Number, Name, Age]: "))
to_add = {'Roll Number': to_get[0], 'Name': to_get[1], 'Age': to_get[2]}
pickle.dump(to_add, db)
db.close()

with open('stu.dat', 'rb') as db:
    while True:
        try:
            to_print = pickle.load(db)
            print(to_print)
        except EOFError:
            break