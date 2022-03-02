import sqlite3
import os

conn = sqlite3.connect('phonebook.db')

cursor_obj = conn.cursor()

table = """ CREATE TABLE IF NOT EXISTS PHONEBOOK(
            name VARCHAR(25) NOT NULL,
            number VARCHAR(25) NOT NULL
        );"""

cursor_obj.execute(table)
conn.commit()

#start functions:
def add(name,number):
   cursor_obj.execute("INSERT INTO PHONEBOOK(name,number) VALUES ("+ "'" + name + "'"  +","+ "'"+ number+ "'" +")")
   conn.commit()


def search(name):
    cursor_obj.execute("select * from PHONEBOOK where name ="+ "'" +name+ "'" )
    output = cursor_obj.fetchall()
    for row in output:
        print(row[0]+ ':' +row[1])
    conn.commit()
   
def delete(name):
    cursor_obj.execute("DELETE from PHONEBOOK where name ="+ "'" +name+ "'" )    
    conn.commit()
   
def show_all():
    cursor_obj.execute("select * from PHONEBOOK " )
    output = cursor_obj.fetchall()
    for row in output:
        print(row[0]+ ':' +row[1])
    conn.commit()
  
#end functions defination
ch = 1
while ch != 0 :
    print("1-Add Phone Number\n2-Search Phone Number\n3-Delete Phone Number\n4-Show All Phone Number\n0-Exit")
    ch = int(input("Enter Your Choice:"))
    os.system('cls')
    if ch == 1:
        name = input("Enter Name:")
        number = input("Entere Number:")
        add(name,number)

    elif ch ==2:
        name = input("Enter Name:")
        search(name)

    elif ch == 3:
        name = input("Enter Name:")
        delete(name)

    elif ch == 4:
        show_all()

conn.close()