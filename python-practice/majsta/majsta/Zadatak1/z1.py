import datetime
from datetime import datetime
from prettytable import PrettyTable
import os.path
from os import path



format = "%Y-%m-%d %H:%M"


working = True


def CheckInputTypes(start_work_str,end_work_str):
            while True:
                try:
                    datetime.strptime(start_work_str, format)
                    datetime.strptime(end_work_str, format)
                    break
                except ValueError:
                     print("Invalid input format. Please provide format of <%Y-%m-%d %H:%M>")
                     start_work_str = input("When did you start working on the task? Please provide format of <%Y-%m-%d %H:%M>")
                     end_work_str = input("When did you finish the task? Please provide format of <%Y-%m-%d %H:%M>")
            return start_work_str, end_work_str
def work():
    
    while working == True:
        print("Write the begining, endtime and the description of the project.")
        start_work_str = input("When did you start working on the task? Please provide format of <%Y-%m-%d %H:%M>")
        end_work_str = input("When did you finish the task? Please provide format of <%Y-%m-%d %H:%M>")
        start_work_str, end_work_str = CheckInputTypes(start_work_str, end_work_str)
        did_on_project = input("Napisite molim vas sta ste radili u projektu")
        

        finished = input("Are you done? ANSWER WITH YES OR NO")
        if finished.lower() == "yes":
              break
        else:
              continue
        
           # 1 if da proveraava da li datoteka postoji, ako ne postoji, da kreira i prosledi mu taj field, ako postoji da ga ignorise, da upise samo row
    if os.path.exists("Zadatak1/worklog.txt"):    
        with open("Zadatak1/worklog.txt", "r") as f:
            with open("Zadatak1/worklog.txt", "a+") as f:
                f.write(f"\n{start_work_str} " + " "  f"{end_work_str}" + " " f"{did_on_project}")
                    
    else:        
        with open("Zadatak1/worklog.txt", "w") as f:            
            data_header  = ["Start Time", "EndTime", "Description"]      
            f.write(f"{data_header[0]} {data_header[1]} {data_header[2]}")
            f.write(f"\n{start_work_str} " + " "  f"{end_work_str}" + " " f"{did_on_project}")  
            

work()  

#pricta fajl, ako ne postoji taj fajl, kreiraj fajl i ispisi prvu liniju, ako postoji fajl, nemoj ispisati field names
    
            


# time = []



# user_time = input("Please enter your work hours")
# user_description = input("Please give me the description of your work")
# i u novom redu nek ti bude prvo ponudjeno vreme: 
# ti upisi tacno vreme u formatu 2023-02-01 9:30 - 2023-02-01 11:30 
# ( ako se ne unese tako, trazi da se ponovo upise ispravno), 
# a nakon toga i opis sta si radio ( to nek bude bilo kakav string i ne mora da se proveravaju karakteri) 
# i zatim upisi u fajl.






