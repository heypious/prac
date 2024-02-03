# Interface Question - create sql table 'stock' with field item_no, item_name, rate, quantity, DOS(date of sales)
import mysql.connector as mq
connection = mq.connect(host='10.0.0.2', user='root', password='t3po', db='prac')
cursor = connection.cursor()
cursor.execute('create table if not exists stock(item_no int(3) primary key, item_name varchar(20), rate int(5), quantity int(3), dos date);')
cursor.commit() #executing commit function is required if any changes are made to the table
# insert a values into table
to_add = eval(input("(Item Number, Item Name, rate, quantity, Date of Sales): "))
cursor.execute(f'insert into stock values({to_add})')
cursor.commit()

# display item number, name and amount.
cursor.execute(f'select item_no, name, amount from stock;')
to_display = cursor.fetchall()
for record in to_display:
    print(record)

# display all the entries where stock quantity less than 10
cursor.execute(f'select * from stock where quantity < 10;')
to_display = cursor.fetchall()
for record in to_display:
    print(record)
