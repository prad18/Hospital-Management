from functions import *
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
                        
                    ##====================================##  
                    ||                                    ||
                    || CHOOSE ONE OF THE GIVEN OPTION :-  ||
                    ||____________________________________||
                    ||                                    ||
                    || 1. Register patient                ||
                    || 2. Appointment                     ||
                    || 3. List of Doctors                 ||
                    || 4. Search your details             ||
                    || 5. To modify data                  ||
                    || 6. Back                            ||
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
                            break
                        
                        
                        else:
                            print(" ")
                            print("~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")
   
            elif g=="2":
                while True:
                        print("""
                        
                    ##====================================##  
                    ||                                    ||
                    || CHOOSE ONE OF THE GIVEN OPTION :-  ||
                    ||____________________________________||
                    ||                                    ||
                    || 1. Register patient                ||
                    || 2. Patient Status                  ||
                    || 3. Search patient details          ||
                    || 4. Modify patient data             ||
                    || 5. Back                            ||
                    ||                                    ||
                    ##====================================##
                    """)
                        x=int(input("""YOUR OPTION:-"""))
                        
                        
                        if x==1:
                            print(" ")
                            print(dat1())
                                
                        
                        elif x==2:
                            print(" ")
                            print(ret1())
                        
                            
                        elif x==3:
                            print(" ")
                            print(search1())
                        
                           
                        
                            
                        elif x==4:
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
                                
                            
                        elif x==5:
                            break
                        
                        
                        else:
                            print(" ")
                            print("~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")

            else:
                break


    else:
        print("  ")
        print("  ")
        print("  ")
        print("~!~!~Project By S.Pradish Vaidya and Rupaneesh~!~!~")
        print("  ")
        print("  ")
        print("  ")
        break
    
            

