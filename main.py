from functions import *
import pandas as pd
print("""  
  
               ___       ___   ___            ___     _____ ___       ___  _____ _____
     |      | |    |    |   | |   | |\    /| |          |  |   |     |   |   |     |   |   |
     |  /\  | |__  |    |     |   | | \  / | |__        |  |   |     |       |     |   |___|
     | /  \ | |    |    |     |   | |  \/  | |          |  |   |     |       |     |       |
     |/    \| |___ |___ |___| |___| |      | |___       |  |___|     |___| __|__   |    ___|
   _________________________________________________  __________    _________________________
                         
                            ___   ___   ___  _____  _____  ____    
                     |   | |   | |     |   |   |      |   |    |  |
                     |___| |   | |___  |___|   |      |   |____|  |
                     |   | |   |     | |       |      |   |    |  |
                     |   | |___|  ___| |     __|__    |   |    |  |____
                    ____________________________________________________                
          """)

d=datetime.date.today()
t=datetime.datetime.now()
print(" ")
print(" ")
print("        DATE:-",d.strftime("%A, %d %B %Y"))
print(" ")
print("        TIME:-",t.strftime("%H:%M:%S"))
print("")
print('')

while True:
    print(""" 
      
    
        
        _______________                _______________                ____________
        |             |                |             |                |          |
        | 1. PATIENT  |                | 2. DOCTOR   |                | 3. EXIT  |
        |_____________|                |_____________|                |__________|
        
         
        
        """)
    e=input("||  SELECT || :-")
    #outpatient
    if e=="1":
        while True:
            print(""" 
            
            
                
                ___________________                ___________________                ____________
                |                 |                |                 |                |          |
                | 1. OUT PATIENT  |                | 2. IN PATIENT   |                | 3. EXIT  |
                |_________________|                |_________________|                |__________|
                
                
                
                """)
            g=input("||  SELECT || :-")
            if g=="1":
                    l={"NAME OF DOCTOR":["Dr. Varun","Dr. Hrithik","Dr. Salman","Dr. Shahrukh","Dr. Akshay","Dr. Amir","Dr. Sidharth","Dr. Abhishek","Dr. Ajay","Dr. Ranveer",'Dr. Irfan','Dr. John','Dr. Sanjay','Dr. Shahid'],
                    "DEPARTMENT":["Cardiologist","Cardiologist","Psychitrist","Psychitrist","Otolaryngonologist","Otolaryngonologist","Rheumatologist","Rheumatologist","Neurologist","Neurologist",'MI room','MI room','MI room','MI room'],
                    "ROOM NO.":[201,202,203,204,205,206,207,208,209,200,401,402,403,404]}
                    df=pd.DataFrame(l)
                    df=df.rename(index={0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:11,11:12,12:13,13:14})




                    while True:
                        print("""
                        

                           ========================
                           ||    OUT PATIENT     ||
                           ========================

                    ##====================================##  
                    ||                                    ||
                    || CHOOSE ONE OF THE GIVEN OPTION :-  ||
                    ||____________________________________||
                    ||                                    ||
                    || 1. Register patient                ||
                    || 2. Appointment                     ||
                    || 3. List of Doctors                 ||
                    || 4. Search your details             ||
                    || 5. Modify Patient data             ||
                    || 6. Delete Data                     ||
                    || 7. Back                            ||
                    ||                                    ||
                    ##====================================##
                    """)
                        x=int(input("""YOUR OPTION:-"""))
                        
                        
                        if x==1:
                            print(" ")
                            print(dat())
                                
                        
                        elif x==2:
                            print(" ")
                            print(ret())
                        
                            
                        elif x==3:
                            print(" ")
                            print("-----FOLLOWING DOCTORS ARE AVAILABLE-----")
                            print(" ")
                            print(df)
                            
                        
                        elif x==4:
                            print(" ")
                            print(search())
                           
                        
                            
                        elif x==5:
                            print(" ")

                        
                            while True:
                                print("""
                            __________________________      
                            |                        |
                            |SELECT WHAT TO CHANGE:- |
                            |------------------------|
                            |1.Name                  | 
                            |2.Age                   |
                            |3.Gender                |
                            |4.Phone no.             |
                            |5.Blood group           |
                            |6.Back                  | 
                            |________________________|
                                """)
                                            
                                s=int(input("ENTER YOUR CHOICE:-"))

                                if s==1:
                                    print(name())
                                    break

                                elif s==2:
                                    print(age())
                                    break

                                elif s==3:
                                    print(gen())
                                    break

                                elif s==4:
                                    print(ph())
                                    break 
                                
                                elif s==5:
                                    print(bg())
                                    
                                elif s==6:
                                    break
                                
                                else:
                                    print(" ")
                                    print("""~!~!~!~WRONG CHOICE PLEASE ENTER VALID VALUE~!~!~!~""")
                                
                            

                        elif x==6:
                            print(" ")
                            print(delete())


                        elif x==7:
                            break
                        
                        
                        else:
                            print(" ")
                            print("~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")
   
            elif g=="2":
                while True:
                        print("""

                          ========================
                          ||    IN PATIENT      ||
                          ========================
                        
                    ##====================================##  
                    ||                                    ||
                    || CHOOSE ONE OF THE GIVEN OPTION :-  ||
                    ||____________________________________||
                    ||                                    ||
                    || 1. Register patient                ||
                    || 2. Patient Status                  ||
                    || 3. Search patient details          ||
                    || 4. Modify patient data             ||
                    || 5. Delete patient data             ||
                    || 6. Back                            ||
                    ||                                    ||
                    ##====================================##
                    """)
                        x=input("""YOUR OPTION:-""")
                        
                        
                        if x=="1":
                            print(" ")
                            print(dat1())
                        elif x=="2":
                            print(" ")
                            print(ret1())
                        elif x=="3":
                            print(" ")
                            print(search1())
                        elif x=="4":
                            print(" ")
                            while True:
                                print("""
                            __________________________      
                            |                        |
                            |SELECT WHAT TO CHANGE:- |
                            |------------------------|
                            |1.Name                  | 
                            |2.Age                   |
                            |3.Gender                |
                            |4.Phone no.             |
                            |5.Blood group           |
                            |6.Back                  | 
                            |________________________|


                                """)
                                            
                                s=int(input("ENTER YOUR CHOICE:-"))

                                if s==1:
                                    print(name1())
                                    break

                                elif s==2:
                                    print(age1())
                                    break

                                elif s==3:
                                    print(gen1())
                                    break

                                elif s==4:
                                    print(ph1())
                                    break 
                                
                                elif s==5:
                                    print(bg1())
                                    
                                elif s==6:
                                    break
                                
                                else:
                                    print(" ")
                                    print("""~!~!~!~WRONG CHOICE PLEASE ENTER VALID VALUE~!~!~!~""")
                                


                        elif x=="5":
                            print(' ')
                            print(delete1())

                        elif x=="6":
                            break
                        
                        
                        else:
                            print(" ")
                            print("~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")

            elif g=="3":
                break

            else:
                print("~~~~~~~~~~SELECT 1,2,or 3~~~~~~~~~~~~~~")

    
    elif e=="2":
        d={"NAME OF PATIENT":["Amit","Sanjay","Vipul","Sayeed"],"AGE":[23,34,27,26],
           "APPOINTMENT NO.":[64,52,12,56]}
        d1=pd.DataFrame(d)
        d1=d1.rename(index={0:1,1:2,2:3,3:4})

        g={"NAME OF PATIENT":["Ankit","Sanjeev","Vikas","Shoib",'Rehan','Suarav','Ganpat'],"AGE":[12,45,21,23,34,27,26],
        "APPOINTMENT NO.":[3,82,12,31,54,39,46]}
        d2=pd.DataFrame(g)
        d2=d2.rename(index={0:1,1:2,2:3,3:4,4:5,5:6,6:7})

        f={"NAME OF PATIENT":["Tanay","Ajay","Akaash","Shakib","Rohan",'Raju','Farhan','Bhuvan'],"AGE":[42,58,32,67,23,34,27,26],
        "APPOINTMENT NO.":[43,23,61,32,21,43,56,31]}
        d3=pd.DataFrame(f)
        d3=d3.rename(index={0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8})

        h={"NAME OF PATIENT":["Ashish","Joy","Jayesh","Somesh","Rahul",'Arham','Bhanu','Danish'],"AGE":[42,58,32,67,23,34,27,26],
        "APPOINTMENT NO.":[43,23,61,32,21,43,56,31]}
        d4=pd.DataFrame(h)
        d4=d4.rename(index={0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8})

        s={"NAME OF PATIENT":["Manav","Dheeraj","Kamal","Sohrab","Yash"],"AGE":[12,23,34,27,26],
        "APPOINTMENT NO.":[64,57,22,12,56]}
        d5=pd.DataFrame(s)
        d5=d5.rename(index={0:1,1:2,2:3,3:4,4:5})

        i={"NAME OF PATIENT":["Umesh",'Kamal','Pankaj','Dhyanesh','Arnav'],"AGE":[12,23,34,27,26],
        "APPOINTMENT NO.":[64,57,22,12,56]}
        d6=pd.DataFrame(i)
        d6=d6.rename(index={0:1,1:2,2:3,3:4,4:5})

        while True:
            print('')
            e=input("ENTER YOUR ID NO. (press enter to exit):-")
            print(" ")
            if e=="1":
                w=7001
                pswd=int(input('ENTER PASSWORD:'))
                if pswd==w:
                    t=datetime.datetime.now()
                    l=t.strftime("%p")
                    if l=="PM":
                    
                        print("|||   GOOD EVENING MR. VARUN   |||")
                    
                    else:
                        print("|||   GOOD MORNING MR. VARUN   |||")
                    print(" ")
                    print(""" YOU HAVE APPOINTMENT WITH FOLLOWING PATIENTS:-""")
                    print("")
                    q=(d1,d2,d3,d4,d5,d6)
                    o=rd.choice(q)
                    print(o)
                else:
                    print('~!~!~!~~PASSWORD OR ID IS WRONG~~!~!~!~')

            elif e=='2':
                w=7002
                pswd=int(input('ENTER PASSWORD:'))
                if pswd==w: 
                    t=datetime.datetime.now()
                    l=t.strftime("%p")
                    if l=="PM":
                        print("|||   GOOD EVENING MR. HRITHIK   |||")
                    
                    else:
                        print("|||   GOOD MORNING MR. HRITHIK   |||")
                    print(" ")    
                    print(" YOU HAVE APPOINTMENT WITH FOLLOWING PATIENTS:-")
                    print("")
                    q=(d1,d2,d3,d4,d5,d6)
                    o=rd.choice(q)
                    print(o)    
                else:
                    print('~!~!~!~~PASSWORD OR ID IS WRONG~~!~!~!~')

                
            elif e=='3':
                z=7003
                pswd=int(input('ENTER PASSWORD:'))
                if pswd==z: 
                    t=datetime.datetime.now()
                    l=t.strftime("%p")
                    if l=="PM":
                        print("|||   GOOD EVENING MR. SALMAN   |||")
                    
                    else:
                        print("|||   GOOD MORNING MR. SALMAN    |||")
                    print(" ")    
                    print(" YOU HAVE APPOINTMENT WITH FOLLOWING PATIENTS:-")
                    print("")
                    q=(d1,d2,d3,d4,d5,d6)
                    o=rd.choice(q)
                    print(o)  
                else:
                    print('~!~!~!~~PASSWORD OR ID IS WRONG~~!~!~!~')  

            elif e=='4':
                z=7004
                pswd=int(input('ENTER PASSWORD:'))
                if pswd==z: 
                    t=datetime.datetime.now()
                    l=t.strftime("%p")
                    if l=="PM":
                        print("|||   GOOD EVENING MR. SHAHRUKH   |||")
                        
                    else:
                        print("|||   GOOD MORNING MR. SHAHRUKH   |||")
                    print(" ")    
                    print(" YOU HAVE APPOINTMENT WITH FOLLOWING PATIENTS:-")
                    print("")
                    q=(d1,d2,d3,d4,d5,d6)
                    o=rd.choice(q)
                    print(o)    
                else:
                    print('~!~!~!~~PASSWORD OR ID IS WRONG~~!~!~!~')  
        
                
            elif e=='5':
                z=7005
                pswd=int(input('ENTER PASSWORD:'))
                if pswd==z: 
                    t=datetime.datetime.now()
                    l=t.strftime("%p")
                    if l=="PM":
                        print("|||   GOOD EVENING MR. AKSHAY   |||")
                        
                    else:
                        print("|||   GOOD MORNING MR. AKSHAY   |||")
                    print(" ")    
                    print(" YOU HAVE APPOINTMENT WITH FOLLOWING PATIENTS:-")
                    print("")
                    q=(d1,d2,d3,d4,d5,d6)
                    o=rd.choice(q)
                    print(o)
                else:
                    print('~!~!~!~~PASSWORD OR ID IS WRONG~~!~!~!~')  
        
                
            elif e=='6':
                z=7006
                pswd=int(input('ENTER PASSWORD:'))
                if pswd==z: 
                    t=datetime.datetime.now()
                    l=t.strftime("%p")
                    if l=="PM":
                        print("|||   GOOD EVENING MR. AMIR   |||")
                        
                    else:
                        print("|||   GOOD MORNING MR. AMIR    |||")
                    print(" ")    
                    print(" YOU HAVE APPOINTMENT WITH FOLLOWING PATIENTS:-")
                    print("")
                    q=(d1,d2,d3,d4,d5,d6)
                    o=rd.choice(q)
                    print(o)  
                else:
                    print('~!~!~!~~PASSWORD OR ID IS WRONG~~!~!~!~')  
                
            elif e=='7':
                z=7007
                pswd=int(input('ENTER PASSWORD:'))
                if pswd==z: 
                    t=datetime.datetime.now()
                    l=t.strftime("%p")
                    if l=="PM":
                        print("|||   GOOD EVENING MR. SIDHARTH   |||")
                        
                    else:
                        print("|||   GOOD MORNING MR. SIDHARTH   |||")
                    print(" ")    
                    print(" YOU HAVE APPOINTMENT WITH FOLLOWING PATIENTS:-")
                    print("")
                    q=(d1,d2,d3,d4,d5,d6)
                    o=rd.choice(q)
                    print(o)
                else:
                    print('~!~!~!~~PASSWORD OR ID IS WRONG~~!~!~!~') 
                
            elif e=='8':
                z=7008
                pswd=int(input('ENTER PASSWORD:'))
                if pswd==z: 
                    t=datetime.datetime.now()
                    l=t.strftime("%p")
                    if l=="PM":
                        print("|||   GOOD EVENING MR. ABHISHEK   |||")
                        
                    else:
                        print("|||   GOOD MORNING MR. ABHISHEK   |||")
                    print(" ")    
                    print(" YOU HAVE APPOINTMENT WITH FOLLOWING PATIENTS:-")
                    print("")
                    q=(d1,d2,d3,d4,d5,d6)
                    o=rd.choice(q)
                    print(o)
                else:
                    print('~!~!~!~~PASSWORD OR ID IS WRONG~~!~!~!~') 
                
            elif e=='9':
                z=7009
                pswd=int(input('ENTER PASSWORD:'))
                if pswd==z: 
                    t=datetime.datetime.now()
                    l=t.strftime("%p")
                    if l=="PM":
                        print("|||   GOOD EVENING MR. AJAY   |||")
                        
                    else:
                        print("|||   GOOD MORNING MR. AJAY   |||")
                    print(" ")    
                    print(" YOU HAVE APPOINTMENT WITH FOLLOWING PATIENTS:-")
                    print("")
                    q=(d1,d2,d3,d4,d5,d6)
                    o=rd.choice(q)
                    print(o)
                else:
                    print('~!~!~!~~PASSWORD OR ID IS WRONG~~!~!~!~')
                
            elif e=='10':
                z=7010
                pswd=int(input('ENTER PASSWORD:'))
                if pswd==z: 
                    t=datetime.datetime.now()
                    l=t.strftime("%p")
                    if l=="PM":
                        print("|||   GOOD EVENING MR. RANVEER   |||")

                    else:
                        print("|||   GOOD MORNING MR. RANVEER   |||")
                    print(" ")    
                    print(" YOU HAVE APPOINTMENT WITH FOLLOWING PATIENTS:-")
                    print("")
                    q=(d1,d2,d3,d4,d5,d6)
                    o=rd.choice(q)
                    print(o)
                else:
                    print('~!~!~!~~PASSWORD OR ID IS WRONG~~!~!~!~')
                
            elif e=='11':
                z=7011
                pswd=int(input('ENTER PASSWORD:'))
                if pswd==z: 
                    t=datetime.datetime.now()
                    l=t.strftime("%p")
                    if l=="PM":
                        print("|||   GOOD EVENING MR. IRFAN   |||")
                        
                    else:
                        print("|||   GOOD MORNING MR. IRFAN   |||")
                    print(" ")            
                    print(" YOU HAVE APPOINTMENT WITH FOLLOWING PATIENTS:-")
                    print("")
                    q=(d1,d2,d3,d4,d5,d6)
                    o=rd.choice(q)
                    print(o) 
                else:
                    print('~!~!~!~~PASSWORD OR ID IS WRONG~~!~!~!~')
                
            elif e=='12':
                z=7012
                pswd=int(input('ENTER PASSWORD:'))
                if pswd==z: 
                    t=datetime.datetime.now()
                    l=t.strftime("%p")
                    if l=="PM":
                        print("|||   GOOD EVENING MR. JOHN   |||")
                        
                    else:
                        print("|||   GOOD MORNING MR. JOHN   |||")
                    print(" ")    
                    print(" YOU HAVE APPOINTMENT WITH FOLLOWING PATIENTS:-")
                    print("")
                    q=(d1,d2,d3,d4,d5,d6)
                    o=rd.choice(q)
                    print(o)
                else:
                    print('~!~!~!~~PASSWORD OR ID IS WRONG~~!~!~!~')
                
            elif e=='13':
                z=7013
                pswd=int(input('ENTER PASSWORD:'))
                if pswd==z: 
                    t=datetime.datetime.now()
                    l=t.strftime("%p")
                    if l=="PM":
                        print("|||   GOOD EVENING MR. SANJAY   |||")
                        
                    else:
                        print("|||   GOOD MORNING MR. SANJAY   |||")
                    print(" ")    
                    print(" YOU HAVE APPOINTMENT WITH FOLLOWING PATIENTS:-")
                    print("")
                    q=(d1,d2,d3,d4,d5,d6)
                    o=rd.choice(q)
                    print(o) 
                else:
                    print('~!~!~!~~PASSWORD OR ID IS WRONG~~!~!~!~')
                
            elif e=='14':
                z=7014
                pswd=int(input('ENTER PASSWORD:'))
                if pswd==z: 
                    t=datetime.datetime.now()
                    l=t.strftime("%p")
                    if l=="PM":
                        print("|||   GOOD EVENING MR. SHAHID   |||")
                        
                    else:
                        print("|||   GOOD MORNING MR. SHAHID   |||")
                    print(" ")    
                    print(" YOU HAVE APPOINTMENT WITH FOLLOWING PATIENTS:-")
                    print("")
                    q=(d1,d2,d3,d4,d5,d6)
                    o=rd.choice(q)
                    print(o)
                else:
                    print('~!~!~!~~PASSWORD OR ID IS WRONG~~!~!~!~')
            
            else:
                break    
         
                        
    elif e=="3":
            print(" ")
            print("\n"
                "      \n"
                "   ##======================================================##\n"
                "   || _____        ___                          ___        ||\n"
                "   ||   |   |   | |   | |\   | |  /      |   | |   | |   | ||\n"
                "   ||   |   |___| |___| | \  | |_/       |___| |   | |   | ||\n"
                "   ||   |   |   | |   | |  \ | | \           | |   | |   | ||\n"
                "   ||   |   |   | |   | |   \| |  \       ___| |___| |___| ||\n"
                "   ##======================================================##\n"
                "\n")
            
            print("  ")
            print("  ")
            print("  ")
            print("~!~!~Project By S.Pradish Vaidya and Rupaneesh~!~!~")
            print("  ")
            print("  ")
            print("  ")
            break 
        
    
    else:
        print(" ")
        print("~~~~PLEASE ENTER 1,2 OR 3~~~~")
        con.close()



            

