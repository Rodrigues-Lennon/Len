import mysql.connector

conn= mysql.connector.connect(host='localhost',password='Lennon@15',user='root',port=3006,database='college')
cur=conn.cursor()


def insert_values():
    while 1:
        student_id=int(input("\nEnter Student ID: "))
        s_name=input("Enter Student Name: ")
        s_age=int(input("Enter Student Age: "))
        s_class=input("Enter Student Class: ")
        select='select * from student where student_id=%s'
        cur.execute(select,(student_id,))
        check=cur.fetchone()
        if (check):
            print(f"Student with ID {student_id} already exists")
        else:
            insert='insert into student values(%s,%s,%s,%s)'
            val=(student_id,s_name,s_age,s_class)
            cur.execute(insert,val)
            conn.commit()
            print("\nDetails Updated")
        
            
        user_input=input("\nDo you want to continue (yes/no): ").lower()
        if user_input== 'no':
            break

        
def delete_value():
    val=int(input("\nEnter Student ID to be deleted: "))
    select='select * from student where student_id=%s'
    cur.execute(select,(val,))
    check=cur.fetchone()
    
    if check:
        confirm=input("\nAre you sure (yes/no): ").lower()
        if confirm=='yes':
            delete='delete from student where student_id=%s'
            cur.execute(delete,(val,))
            conn.commit()
            print(f"\nStudent ID {val} has been deleted")
        else:
            print(f"\nStudent ID {val} has not been deleted")
    else:
        print(f"Student ID {val} does not exist")
        
def display_values():
    display='select * from student'
    cur.execute(display)
    students=cur.fetchall()
    print("\nStudent Details")
    print("{:<10} {:<20} {:<10} {:<10}".format("ID", "Name", "Age", "Class"))
    for student in students:
        print("{:<10} {:<20} {:<10} {:<10}".format(student[0], student[1], student[2], student[3]))
        
def search_update():
    val=int(input("\nEnter Student ID to search: "))
    select='select * from student where student_id=%s'
    cur.execute(select,(val,))
    check=cur.fetchone()
    
    if check:
        print(f"\nStudent ID {val} Found")
        print("\nOptions")
        print("1. To Update Name")
        print("2. To Update Age")
        print("3. To Update Class")
        
        choice=input("\nEnter your choice (1/2/3): ")
        if choice=='1':
            update_s_name=input("Enter new name: ")
            update='update student set s_name=%s where student_id=%s'
            cur.execute(update,(update_s_name,val))
        elif choice=='2':
            update_s_age=int(input("Enter new age: "))
            update='update student set s_age=%s where student_id=%s'
            cur.execute(update,(update_s_age,val))
        elif choice=='3':
            update_s_class=input("Enter new class: ")
            update='update student set s_class=%s where student_id=%s'
            cur.execute(update,(update_s_class,val))
        conn.commit()
        print("\nStudent Details Updated")
    else:
        print(f"\nStudent ID {val} Not found")

while True:    
    print("\nOptions:")
    print("1. Add Student Details")
    print("2. Delete a specific Student Details")
    print("3. Display Students")
    print("4. Search and Update")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")   
    if choice=='1':
        insert_values()
    elif choice=='2':
        delete_value()
    elif choice=='3':
        display_values()
    elif choice=='4':
        search_update()
    elif choice=='5':
        break
    else:
        print("\nInvalid Input")
    
print("\nThank You!!")
cur.close()
conn.close(
