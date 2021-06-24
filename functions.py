import datetime
import random as rd
import pandas as pd
import mysql.connector 
con=mysql.connector.connect(host="localhost",user="root",password="123456")
cur=con.cursor()

cur=con.cursor(buffered=True) 

cur.execute("create database if not exists Hospital2")

cur.execute("use Hospital2")

cur.execute("create table if not exists inpatient"
            "("
            "idno char(12) primary key,"
            "name char(20),"
            "age int(10),"
            "gender char(1),"
            "phone char(10),"
            "bg char(3))")

cur.execute("create table if not exists outpatient"
            "("
            "idno char(12) ,"
            "name char(20),"
            "age int(10),"
            "gender char(1),"
            "phone char(10),"
            "bg char(3),"
            "doa char(10))")    
def dat():
    while True:
        idn=input("ID no.:")
        if len(idn)==4 :
            break
        else:
            print(" ~!~!~!~~4 digits required~~!~!~!~")
    while True:    
        name=input("Patient name:")
        if type(name)!=str:
            print("~!~!~!~~Only string~~!~!~!~~!~!~!~")
        else:
            break    
    
    while True:
        age=int(input("Age:"))
        if type(age)!=int:
            print("~!~!~!~~digits required~~!~!~!~")
        else:
            break

    
    while True:
        gen=input("Gender M/F:")
        if gen==("M") or gen==("F"):
            break
        else:
            print("~!~!~!~~ M\F only ~~!~!~!~")
    
    while True:
        ph=input("Phone no.:")
        if len(ph)==10:
            break
        else:
            print("~!~!~!~~10 digits required~~!~!~!~")
    while True:
        bg=input("""Blood group(A+,B+,O+,AB+,A-,B-,O-,AB-):-""")
        if bg==("A+") or bg==("B+") or bg==("O+") or bg==("AB+") or bg==("A-") or bg==("B-") or bg==("O-") or bg==("AB-"):
            break
        else:
            print("~!~!~!~~ Enter valid value ~~!~!~!~")
    cur.execute("insert into inpatient(idno,name,age,gender,phone,bg) values(%s,%s,%s,%s,%s,%s)",(idn,name,age,gen,ph,bg,))
    con.commit()
    print(" ")
    print("""   
    __________________________        
    |                        |
    |YOU HAVE BEEN REGISTERED| 
    |________________________|     
        """)
    
    print("""
    _______________________________ 
    |                             |
    |Your details are as follows:-|
    |_____________________________| 
    
    """)
    cur.execute("select * from inpatient where idno=(%s);",(idn,))
    d=cur.fetchall()
    for i in d:
        print("""     ID no.:-""",i[0])
        print('''     Name:-''',i[1])
        print('''     Age:-''',i[2])
        print('''     Gender:-''',i[3])
        print('''     Phone:-''',i[4])
        print('''     Bloodgroup:-''',i[5])
    return("")

#name modify
def name():
    adr=int(input('ENTER YOUR ID NO:'))
    cur.execute('select * from inpatient where idno=(%s)',(adr,))
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)
        
    if len(a)!=1:
        print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
        
    else:
        print('')
        print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
        
        print("")
        print("""     ID no.:-""",i[0])
        print('''     Name:-''',i[1])
        print('''     Age:-''',i[2])
        print('''     Gender:-''',i[3])
        print('''     Phone:-''',i[4])
        print('''     Bloodgroup:-''',i[5])
        n=input('ENTER NEW NAME:-')
        cur.execute('update inpatient set name=(%s) where idno=(%s);',(n,adr,))
        con.commit()
        cur.execute('select * from inpatient where idno=(%s)',(adr,))
        dat=cur.fetchall()
        for row in dat:
                print('')
                print('''
        ------------------------      
        | YOU NEW DETAILS ARE  |
        ------------------------      
                ''')
                print('')                
                print("""     ID no.:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])
                print('''     Gender:-''',row[3])
                print('''     Phone:-''',row[4])
                print('''     Bloodgroup:-''',row[5])
                con.commit()
        return("")




def age():
        adr=int(input('ENTER YOUR ID NO:'))
        cur.execute('select * from inpatient where idno=(%s)',(adr,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
            
        if len(a)!=1:
            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
            
        else:
            print('')
            print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
            
            print("")
            print("""     ID no.:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     Bloodgroup:-''',i[5])
            n=input('ENTER NEW AGE:-')
            cur.execute('update inpatient set age=(%s) where idno=(%s);',(n,adr,))
            con.commit()
            cur.execute('select * from inpatient where idno=(%s)',(adr,))
            dat=cur.fetchall()
            for row in dat:
                print('')
                print('''
        ------------------------      
        | YOU NEW DETAILS ARE  |
        ------------------------      
                ''')
                print('')                
                print("""     ID no.:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])
                print('''     Gender:-''',row[3])
                print('''     Phone:-''',row[4])
                print('''     Bloodgroup:-''',row[5])
                con.commit()
        return("")
    
def gen():
        adr=int(input('ENTER YOUR ID NO:'))
        cur.execute('select * from inpatient where idno=(%s)',(adr,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
            
        if len(a)!=1:
            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
            
        else:
            print('')
            print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
            
            print("")
            print("""     ID no.:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     Bloodgroup:-''',i[5])
            n=input('ENTER NEW GENDER:-')
            cur.execute('update inpatient set gender=(%s) where idno=(%s);',(n,adr,))
            con.commit()
            cur.execute('select * from inpatient where idno=(%s)',(adr,))
            dat=cur.fetchall()
            for row in dat:
                print('')
                print('''
        ------------------------      
        | YOU NEW DETAILS ARE  |
        ------------------------      
                ''')
                print('')                
                print("""     ID no.:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])
                print('''     Gender:-''',row[3])
                print('''     Phone:-''',row[4])
                print('''     Bloodgroup:-''',row[5])
                con.commit()
        return("")         


def ph():
        adr=int(input('ENTER YOUR ID NO:'))
        cur.execute('select * from inpatient where idno=(%s)',(adr,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
            
        if len(a)!=1:
            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
            
        else:
            print('')
            print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
            
            print("")
            print("""     ID no.:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     Bloodgroup:-''',i[5])
            n=input('ENTER NEW PHONE NO:-')
            cur.execute('update inpatient set phone=(%s) where idno=(%s);',(n,adr,))
            con.commit()
            cur.execute('select * from inpatient where idno=(%s)',(adr,))
            dat=cur.fetchall()
            for row in dat:
                print('')
                print('''
        ------------------------      
        | YOU NEW DETAILS ARE  |
        ------------------------      
                ''')
                print('')                
                print("""     ID no.:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])
                print('''     Gender:-''',row[3])
                print('''     Phone:-''',row[4])
                print('''     Bloodgroup:-''',row[5])
                con.commit()
        return("")


def bg():
        adr=int(input('ENTER YOUR ID NO:'))
        cur.execute('select * from inpatient where idno=(%s)',(adr,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
            
        if len(a)!=1:
            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
            
        else:
            print('')
            print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
            
            print("")
            print("""     ID no.:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     Bloodgroup:-''',i[5])
            n=input('ENTER NEW BLOOD GROUP:-')
            cur.execute('update inpatient set bg=(%s) where idno=(%s);',(n,adr,))
            con.commit()
            cur.execute('select * from inpatient where idno=(%s)',(adr,))
            dat=cur.fetchall()
            for row in dat:
                print('')
                print('''
        ------------------------      
        | YOU NEW DETAILS ARE  |
        ------------------------      
                ''')
                print('')                
                print("""     ID no.:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])
                print('''     Gender:-''',row[3])
                print('''     Phone:-''',row[4])
                print('''     Bloodgroup:-''',row[5])
                con.commit()
        return("") 



def ret():
        adr=int(input('Enter ID no:'))
        cur.execute('select * from inpatient where idno=(%s)',(adr,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
        if len(a)!=1:
            print('')
            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
            
        else:

            while True:
                print('''
    _______________________     
    |                     |
    |SELECT DEPARTMENT:-  |
    |                     |
    |1.Cardiologist       |
    |2.Rheumatologist     |
    |3.Psychitrist        |
    |4.Neurologist        |
    |5.Otolaryngonologist |
    |6.MI Room            |
    |7.Back               |
    |_____________________|
                ''')
                
                x=int(input("Enter choice:-"))
                
                if x==1:
                    i=("Dr. Varun \nRoom no:- 201")
                    j=("Dr. Hrithik \nRoom no:- 202")
                    q=(i,j)
                    h=rd.choice(q)
                    print(" ")
                    print("Your appointment is fixed with",h,"\nDate:-",datetime.date.today() + datetime.timedelta(days=3))
                    u=(12,43,54,71,32,65)
                    o=rd.choice(u)
                    print("Appointment no:-",o)
                    break
                elif x==2:
                    i=("Dr. Sidharth \nRoom no. 207")
                    j=("Dr. Abhishek \nRoom no. 208")
                    q=(i,j)
                    h=rd.choice(q)
                    print(" ")
                    print("Your appointment is fixed with",h,"Date:-",datetime.date.today() + datetime.timedelta(days=5))
                    u=(12,43,54,71,32,65)
                    o=rd.choice(u)
                    print("Appointment no:-",o)
                    break
            
                elif x==3:
                    i=("Dr. Salman \nRoom no. 203")
                    j=("Dr. Shahrukh \nRoom no. 204")
                    q=(i,j)
                    h=rd.choice(q)
                    print(' ')
                    print("Your appointment is fixed with",h,"Date:-",datetime.date.today() + datetime.timedelta(days=3))
                    u=(12,43,54,71,32,65)
                    o=rd.choice(u)
                    print("Appointment no:-",o)
                    break
                elif x==4:
                    i=("Dr. Ajay, \nRoom no. 209")
                    j=("Dr. Ranveer \nRoom no. 200")
                    q=(i,j)
                    h=rd.choice(q)
                    print(' ')
                    print("Your appointment is fixed with",h,"Date:-",datetime.date.today() + datetime.timedelta(days=6))
                    u=(12,43,54,71,32,65)
                    o=rd.choice(u)
                    print("Appointment no:-",o)
                    break
                elif x==5:
                    i=("Dr. Akshay \nRoom no. 205")
                    j=("Dr. Amir \nRoom no. 206")
                    q=(i,j)
                    h=rd.choice(q)
                    print(' ')
                    print("Your appointment is fixed with",h,"Date:-",datetime.date.today() + datetime.timedelta(days=4))
                    u=(12,43,54,71,32,65)
                    o=rd.choice(u)
                    print("Appointment no:-:",o)
                    break
                elif x==6:
                    i=("Dr. Irfan \nRoom no. 001")
                    j=("Dr. John \nRoom no. 002")
                    k=("Dr. Sanjay \nRoom no. 003")
                    l=("Dr. Shahid \nRoom no. 004")
                    q=(i,j,k,l)
                    h=rd.choice(q)
                    print(" ")
                    print("Your appointment is fixed with",h,"Date:-",datetime.date.today() + datetime.timedelta(days=1))
                    u=(12,43,54,71,32,65)
                    o=rd.choice(u)
                    print("Appointment no:-",o)
                    break
                
                elif x==7:
                    break
                
                else:
                    print("~!~!~!~WRONG OPTION PLEASE ENTER VALID VALUE~!~!~!~")
                
        return(" ")


def dat1():
    while True:
            idn1=input("ID no.:")
            if len(idn1)==4 :
                break
            else:
                print(" ~!~!~!~~4 digits required~~!~!~!~")

    while True:    
        name1=input("Patient name:")
        if type(name1)!=str:
            print("~!~!~!~~Only String~~!~!~!~")
        else:
            break

    while True:
        age1=int(input("Age:"))
        if type(age1)!=int:
            print("~!~!~!~~digits required~~!~!~!~")
        else:
            break

    
    while True:
        gen1=input("Gender M/F:")
        if gen1==("M") or gen1==("F"):
            break
        else:
            print("~!~!~!~~ M\F only ~~!~!~!~")
    
    while True:
        ph1=input("Phone no.:")
        if len(ph1)==10:
            break
        else:
            print("~!~!~!~~10 digits required~~!~!~!~")
    while True:
        bg1=input("""Blood group(A+,B+,O+,AB+,A-,B-,O-,AB-):-""")
        if bg1==("A+") or bg1==("B+") or bg1==("O+") or bg1==("AB+") or bg1==("A-") or bg1==("B-") or bg1==("O-") or bg1==("AB-"):
            break
        else:
            print("~!~!~!~~ Enter valid value ~~!~!~!~")
    while True:
        doa=input("""Date Of Admission(YY-MM-DD):-""")
        break
    cur.execute("insert into outpatient(idno,name,age,gender,phone,bg,doa) values(%s,%s,%s,%s,%s,%s,%s)",(idn1,name1,age1,gen1,ph1,bg1,doa))
    con.commit()
    print(" ")
    print("""   
    __________________________        
    |                        |
    |YOU HAVE BEEN REGISTERED| 
    |________________________|     
        """)
    
    print("""
    _______________________________ 
    |                             |
    |Your details are as follows:-|
    |_____________________________| 
    
    """)
    cur.execute("select * from outpatient where idno=(%s);",(idn1,))
    d=cur.fetchall()
    for i in d:
        print("""     ID no.:-""",i[0])
        print('''     Name:-''',i[1])
        print('''     Age:-''',i[2])
        print('''     Gender:-''',i[3])
        print('''     Phone:-''',i[4])
        print('''     Bloodgroup:-''',i[5])
        print('''     Date of Admission:-''',i[6])
    return("")

#name modify
def name1():
    adr=int(input('ENTER YOUR ID NO:'))
    cur.execute('select * from outpatient where idno=(%s)',(adr,))
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)
        
    if len(a)!=1:
        print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
        
    else:
        print('')
        print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
        
        print("")
        print("""     ID no.:-""",i[0])
        print('''     Name:-''',i[1])
        print('''     Age:-''',i[2])
        print('''     Gender:-''',i[3])
        print('''     Phone:-''',i[4])
        print('''     Bloodgroup:-''',i[5])
        print('''     Date of Admission:-''',i[6])
        n=input('ENTER NEW NAME:-')
        cur.execute('update outpatient set name=(%s) where idno=(%s);',(n,adr,))
        con.commit()
        cur.execute('select * from outpatient where idno=(%s)',(adr,))
        dat=cur.fetchall()
        for row in dat:
                print('')
                print('''
        ------------------------      
        | YOU NEW DETAILS ARE  |
        ------------------------      
                ''')
                print('')                
                print("""     ID no.:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])
                print('''     Gender:-''',row[3])
                print('''     Phone:-''',row[4])
                print('''     Bloodgroup:-''',row[5])
                print('''     Date of Admission:-''',row[6])
                con.commit()
        return("")




def age1():
        adr=int(input('ENTER YOUR ID NO:'))
        cur.execute('select * from outpatient where idno=(%s)',(adr,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
            
        if len(a)!=1:
            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
            
        else:
            print('')
            print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
            
            print("")
            print("""     ID no.:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     Bloodgroup:-''',i[5])
            print('''     Date of Admission:-''',i[6])
            n=input('ENTER NEW AGE:-')
            cur.execute('update outpatient set age=(%s) where idno=(%s);',(n,adr,))
            con.commit()
            cur.execute('select * from outpatient where idno=(%s)',(adr,))
            dat=cur.fetchall()
            for row in dat:
                print('')
                print('''
        ------------------------      
        | YOU NEW DETAILS ARE  |
        ------------------------      
                ''')
                print('')                
                print("""     ID no.:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])
                print('''     Gender:-''',row[3])
                print('''     Phone:-''',row[4])
                print('''     Bloodgroup:-''',row[5])
                print('''     Date of Admission:-''',row[6])
                con.commit()
        return("")
    
def gen1():
        adr=int(input('ENTER YOUR ID NO:'))
        cur.execute('select * from outpatient where idno=(%s)',(adr,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
            
        if len(a)!=1:
            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
            
        else:
            print('')
            print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
            
            print("")
            print("""     ID no.:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     Bloodgroup:-''',i[5])
            print('''     Date of Admission:-''',i[6])
            n=input('MODIFY GENDER DETAILS(M/Y):-')
            cur.execute('update outpatient set gender=(%s) where idno=(%s);',(n,adr,))
            con.commit()
            cur.execute('select * from outpatient where idno=(%s)',(adr,))
            dat=cur.fetchall()
            for row in dat:
                print('')
                print('''
        ------------------------      
        | YOU NEW DETAILS ARE  |
        ------------------------      
                ''')
                print('')                
                print("""     ID no.:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])
                print('''     Gender:-''',row[3])
                print('''     Phone:-''',row[4])
                print('''     Bloodgroup:-''',row[5])
                print('''     Date of Admission:-''',row[6])
                con.commit()
        return("")         


def ph1():
        adr=int(input('ENTER YOUR ID NO:'))
        cur.execute('select * from outpatient where idno=(%s)',(adr,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
            
        if len(a)!=1:
            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
            
        else:
            print('')
            print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
            
            print("")
            print("""     ID no.:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     Bloodgroup:-''',i[5])
            print('''     Date of Admission:-''',i[6])
            n=input('ENTER NEW PHONE NO:-')
            cur.execute('update outpatient set phone=(%s) where idno=(%s);',(n,adr,))
            con.commit()
            cur.execute('select * from outpatient where idno=(%s)',(adr,))
            dat=cur.fetchall()
            for row in dat:
                print('')
                print('''
        ------------------------      
        | YOU NEW DETAILS ARE  |
        ------------------------      
                ''')
                print('')                
                print("""     ID no.:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])
                print('''     Gender:-''',row[3])
                print('''     Phone:-''',row[4])
                print('''     Bloodgroup:-''',row[5])
                print('''     Date of Admission:-''',row[6])
                con.commit()
        return("")


def bg1():
        adr=int(input('ENTER YOUR ID NO:'))
        cur.execute('select * from outpatient where idno=(%s)',(adr,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
            
        if len(a)!=1:
            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
            
        else:
            print('')
            print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
            
            print("")
            print("""     ID no.:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     Bloodgroup:-''',i[5])
            print('''     Date of Admission:-''',i[6])
            n=input('ENTER NEW BLOOD GROUP:-')
            cur.execute('update outpatient set bg=(%s) where idno=(%s);',(n,adr,))
            con.commit()
            cur.execute('select * from outpatient where idno=(%s)',(adr,))
            dat=cur.fetchall()
            for row in dat:
                print('')
                print('''
        ------------------------      
        | YOU NEW DETAILS ARE  |
        ------------------------      
                ''')
                print('')                
                print("""     ID no.:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])
                print('''     Gender:-''',row[3])
                print('''     Phone:-''',row[4])
                print('''     Bloodgroup:-''',row[5])
                print('''     Date of Admission:-''',row[6])
                con.commit()
        return("")