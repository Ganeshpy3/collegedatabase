import mysql.connector
import sys
host=input("Enter  your host")
user=input("Enter your  mysql username")
password=input("Enter your mysql password")
try:
    db=mysql.connector.connect(host=host,user=user,passwd=password)
    cur = db.cursor()
except Exception:
    print("please enter correct username pasword")
    sys.exit()

# cur.execute("""CREATE DATABASE COLLEGE""")
cur.execute("""USE COLLEGE""")
# cur.execute("""CREATE TABLE ADMIN(NAME VARCHAR(255),
#                 USERNAME VARCHAR(255)
#                 PASSWORD """)
# cur.execute("""CREATE TABLE student(Register_number INT primary key AUTO_INCREMENT,
#             First_name VARCHAR(255),
#             last_name VARCHAR(255),
#             DOB VARCHAR(255),
#             USERNAME VARCHAR(255),


#             PASSWORD VARCHAR(255))""")
# cur.execute("""CREATE TABLE Teacher(Register_number INT primary key AUTO_INCREMENT,
#             First_name VARCHAR(255),
#             last_name VARCHAR(255),
#             DOB VARCHAR(255),
#             Subject_name VARCHAR(255),
#             USERNAME VARCHAR(255),
#             PASSWORD VARCHAR(255))""")
# cur.execute("DROP TABLE STUDENT")
# cur.execute("DROP TABLE TEACHER")
# cur.execute("""CREATE TABLE  ECE (Register_number INT primary key AUTO_INCREMENT,
# # #              First_name VARCHAR(255),
# # #              last_name VARCHAR(255))""")
# cur.execute("DROP TABLE ECE")
class college():
    def user(users):
        if users=="1":
            pas=input("Enter your mysql password")
            if pas==password:
                print("Welcome")
                print("1.Register New Student")
                print("2.Register New Teacher")
                print("3.Add new Department")
                choice=int(input())
                if choice==1:
                   college.add_student()
                elif choice==2:
                    college.add_teacher()
                elif choice==3:
                    college.add_department()
            else:
                print("Password is wrong /n Please enter correct password")
                college.user("1")

        elif users=="2":
            college.students_login()
    def add_student():
        fname = input("Enter your First name :\n")
        lname = input("Enter your Last name :\n")
        dob = input("Enter your DOB :\n")
        usname = fname + dob[:2] + "@clg.com"
        password = dob.replace("-", "")
        cur.execute("""INSERT INTO STUDENT(FIRST_NAME,LAST_NAME,DOB,USERNAME,PASSWORD)
                            VALUES(%s,%s,%s,%s,%s)""", (fname, lname, dob, usname, password))

        db.commit()
    def add_teacher():
        fname = input("Enter your First name :\n")
        lname = input("Enter your Last name :\n")
        dob = input("Enter your DOB :\n")
        subject=input("Enter your Subject :\n")
        usname = fname + subject + "@clg.com"
        password = dob.replace("-", "")
        cur.execute("""INSERT INTO teacher(FIRST_NAME,LAST_NAME,DOB,SUBJECT_NAME,USERNAME,PASSWORD)
                             VALUES(%s,%s,%s,%s,%s)""", (fname, lname, dob,subject, usname, password))
        db.commit()
    def students_login():
        us = input("Enter your username :\n")
        pas = input("Enter your Password :\n")
        cur.execute("SELECT PASSWORD FROM STUDENT WHERE USERNAME=%s", (us,))
        for i in cur.fetchall():
            for j in i:
                passcheck = j
        if pas == passcheck:
            print("Access grant :\n")
            inp=int(input("1.Password reset\n2.Mark\n"))
            if inp==1:
                newpass=input("Enter new password:\n")
                new1pass=input("Confirm your password:\n")
                if(new1pass==newpass):
                    cur.execute("UPDATE student set PASSWORD= %s WHERE USERNAME= %s",(newpass,us))
                    db.commit()
                    print("Password changed successfully..")
        else:
            print("Access Denied")

    def teacher_login():
        us = input("Enter your username :\n")
        pas = input("Enter your Password :\n")
        cur.execute("SELECT PASSWORD FROM TEACHER WHERE USERNAME=%s", (us,))
        for i in cur.fetchall():
            print(i)
            for j in i:
                passcheck = j
        if pas == passcheck:
            print("Access grant :\n")
            inp=int(input("1.Password reset\n2.Add students\n3.Update mark\n"))
            if inp==1:
                newpass=input("Enter new password:\n")
                new1pass=input("Confirm your password:\n")
                if(new1pass==newpass):
                    cur.execute("UPDATE TEACHER set PASSWORD=%s WHERE USERNAME=%s",(newpass,us))
                    db.commit()
                    print("Password changed successfully..")
            elif  inp==2:
                newclass=input("Enter the class name")

        else:
            print("Access Denied")
    def add_department():
        newdepartment=input("Enter the Department ID")
        try:
            query="Create table "+newdepartment+"(Dep_class varchar(255),Students_Strength int,Faculty_Strength int)"
            cur.execute(query)
        except Exception:
            print("Department is already exists")


a=college.user(input("1.Admin\n2.Student\n3.Teacher\n"))