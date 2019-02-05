# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 22:40:17 2019

@author: Zeyu Yan
"""

import os
import csv
import us_state_abbrev

class PyBoss():
    def __init__(self):
        """
        Initialization
        """
        self.__current_path = os.getcwd()
        self.__data_path = self.__current_path + "\data" + r"\employee_data.csv"
    
    def read_analyze_and_write_data(self):
        with open(self.__current_path + r"\output.csv", 'w', newline='') as outcsv:
            writer = csv.writer(outcsv)
            writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
            
            with open(self.__data_path, 'r') as incsv:
                reader = csv.reader(incsv)
                next(reader)
                for row in reader:
                    Emp_ID = row[0]
                    Full_Name = row[1]
                    First_Name, Last_Name = Full_Name.split(" ")
                    DOB = row[2]
                    year, month, day = DOB.split("-")
                    DOB_reformated = month + '/' + day + '/' + year
                    SSN = row[3]
                    SSN_reformated = "***-**-" + SSN[8:]
                    State = row[4]
                    State_abbrev = us_state_abbrev.us_state_abbrev[State]
                    
                    writer.writerow([Emp_ID, First_Name, Last_Name, DOB_reformated, SSN_reformated, State_abbrev])
                    
if __name__ == '__main__':
    py_boss = PyBoss()
    py_boss.read_analyze_and_write_data()     
            
        
                    
                    
                    
            