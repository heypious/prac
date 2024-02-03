# Copy all the lines from realfile.txt to copyfile.txt in which line starts with '@' sign
with open('realfile.txt', 'r') as db:
    realfile = db.readlines()

with open('copyfile.txt', 'a') as db:
    for line in realfile:
        if line.startsWith('@'):
            db.writeline(line)
