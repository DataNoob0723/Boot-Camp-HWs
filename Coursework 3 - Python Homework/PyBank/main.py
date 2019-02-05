# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 18:25:29 2019

@author: Zeyu Yan
"""

import os
import csv

"""
Don't want to load all of the data and save them into a list, in case the data set is large.
"""

class PyBank():
    def __init__(self):
        """
        Initialization
        """
        self.__current_path = os.getcwd()
        self.__data_path = self.__current_path + "\data" + r"\budget_data.csv"
        self.__month_counter = 0
        self.__net_profit = 0
        self.__g_increase = 0
        self.__g_decrease = 0
        self.__g_increase_date = ''
        self.__g_decrease_date = ''
        self.__average_change_in_profit = 0
    
    def __read_and_analyze_data(self):
        with open(self.__data_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader) # Skip the header
            for line in csv_reader:
                date = line[0]
                profit = float(line[1])
                self.__month_counter += 1
                self.__net_profit += profit
                if profit > self.__g_increase:
                    self.__g_increase = profit
                    self.__g_increase_date = date
                elif profit < self.__g_decrease:
                    self.__g_decrease = profit
                    self.__g_decrease_date = date
            
            self.__average_change_in_profit = self.__net_profit / self.__month_counter
    
    def print_and_save_conclusions(self):
        self.__read_and_analyze_data()
        """
        Print conclusions
        """
        print(f"Total Months: {self.__month_counter}")
        print(f"Total: {self.__net_profit:.2f}")
        print(f"Average Change: ${self.__average_change_in_profit:.2f}")
        print(f"Greatest Increase in Profits: {self.__g_increase_date} (${self.__g_increase:.2f})")
        print(f"Greatest Increase in Profits: {self.__g_decrease_date} (${self.__g_decrease:.2f})")
        """
        Save conclusions to a text file
        """
        with open(self.__current_path + r"\conclusion.txt", 'w') as f:
            nl = '\n'
            f.write(f"Total Months: {self.__month_counter}{nl}")
            f.write(f"Total: {self.__net_profit:.2f}{nl}")
            f.write(f"Average Change: ${self.__average_change_in_profit:.2f}{nl}")
            f.write(f"Greatest Increase in Profits: {self.__g_increase_date} (${self.__g_increase:.2f}){nl}")
            f.write(f"Greatest Increase in Profits: {self.__g_decrease_date} (${self.__g_decrease:.2f})")
            
                
if __name__ == '__main__':
    py_bank = PyBank()
    py_bank.print_and_save_conclusions()
            
          
        