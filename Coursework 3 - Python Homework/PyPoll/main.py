# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 18:25:51 2019

@author: Zeyu Yan
"""

import os
import csv
import numpy as np

class PyPoll():
    def __init__(self):
        """
        Initialization
        """
        self.__current_path = os.getcwd()
        self.__data_path = self.__current_path + "\data" + r"\election_data.csv"
        self.__vote_counter = 0
        self.__candidates_dict = dict()
        self.__winner = ""
           
    def __read_and_analyze_data(self):
        with open(self.__data_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader) # Skip the header
            for line in csv_reader:
                self.__vote_counter += int(line[0])
                if line[2] not in list(self.__candidates_dict.keys()):
                    self.__candidates_dict[line[2]] = int(line[0])
                else:
                    self.__candidates_dict[line[2]] += int(line[0])
            # Make sure the result is correct        
            assert self.__vote_counter == np.sum(list(self.__candidates_dict.values()))
            
            self.__winner = list(self.__candidates_dict.keys())[np.argmax(list(self.__candidates_dict.values()))]
    
    def print_and_save_conclusions(self):
        self.__read_and_analyze_data()
        """
        Print conclusions
        """
        print("Election Results")
        print("-------------------------")
        print(f"Total Votes: {self.__vote_counter}")
        print("-------------------------")
        for key in self.__candidates_dict.keys():
            print(f"{key}: {(self.__candidates_dict[key] / self.__vote_counter * 100):.3f}% ({self.__candidates_dict[key]})")
        print("-------------------------")
        print(f"Winner: {self.__winner}")
        print("-------------------------")
        """
        Save conclusions to a text file
        """
        with open(self.__current_path + r"\conclusion.txt", 'w') as f:
            nl = '\n'
            f.write(f"Election Results{nl}")
            f.write(f"-------------------------{nl}")
            f.write(f"Total Votes: {self.__vote_counter}{nl}")
            f.write(f"-------------------------{nl}")
            for key in self.__candidates_dict.keys():
                f.write(f"{key}: {(self.__candidates_dict[key] / self.__vote_counter * 100):.3f}% ({self.__candidates_dict[key]}){nl}")
            f.write(f"-------------------------{nl}")
            f.write(f"Winner: {self.__winner}{nl}")
            f.write("-------------------------")
            
            
if __name__ == '__main__':
    py_poll = PyPoll()
    py_poll.print_and_save_conclusions()               