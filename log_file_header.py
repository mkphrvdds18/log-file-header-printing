
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 10:03:48 2018


# goto working dir 
# log_file_name.txt will be created if not pre-exist
# if the file exits 'a' will append new information to it

import time
import os 

# print current date and time to the top of log file

file = open('log_file_name.txt','a')
for i in range(1):
    file.write('#'*80)
    file.write('\n')
    file.write('Today\'s date is: ')
    #file.write(str(today))  #use casting as date object is not str
    file.write(time.ctime())
    file.write('\n')
    file.write('\n')

file.close()

