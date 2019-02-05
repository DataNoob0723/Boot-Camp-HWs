# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 11:24:48 2019

@author: Zeyu Yan
"""

import os
import re
import numpy as np


class PyParagraph():
    def __init__(self, doc_name):
        """
        Initialization
        doc_name's type is string, for example, a.txt
        """
        self.__current_path = os.getcwd()
        self.__data_path = self.__current_path + "\\raw_data" + "\\" + doc_name
        self.__word_counter = 0
        self.__sentence_counter = 0
        self.__letter_counter = 0
        self.__letter_count_per_word = 0
        self.__avg_sentence_len = 0
        self.__words_list_row = []

            
    def __read_and_analyze_data(self):
        with open(self.__data_path, 'r') as f:
            for row in f:
                if row != '\n':
                    """
                    Remove some of the punctuations
                    """
                    row_cleaned = re.sub(r'[,?!."]', "", row).strip('\n')
                    self.__words_list_row = row_cleaned.split(" ")
                    self.__word_counter += len(self.__words_list_row)
                    """
                    Use RegeX to match the EOS punctuations
                    """
                    pattern = re.compile(r'[?!.]')
                    self.__sentence_counter += len(pattern.findall(row))
                    
                    self.__word_num_list = [len(word) for word in self.__words_list_row]
                    self.__letter_counter += np.sum(self.__word_num_list)
            
            self.__letter_count_per_word = self.__letter_counter / self.__word_counter
            self.__avg_sentence_len = self.__word_counter / self.__sentence_counter

                                       
    def print_conclusions(self):
        self.__read_and_analyze_data()
        """
        Print conclusions
        """
        print("Paragraph Analysis")
        print("-----------------")
        print(f"Approximate Word Count: {self.__word_counter}")
        print(f"Approximate Sentence Count: {self.__sentence_counter}")
        print(f"Average Letter Count: {self.__letter_count_per_word:.1f}")
        print(f"Average Sentence Length: {self.__avg_sentence_len:.1f}")


if __name__ == '__main__':
    doc_name = input("Please type the name of the document which needs to be analyzed: ") 
    py_paragraph = PyParagraph(doc_name)
    py_paragraph.print_conclusions()
       