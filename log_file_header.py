
"""
# -*- coding: utf-8 -*-

# goto working dir os.chdir("dir path here")
# os.chdir("D:\\any_dir\\folder_for_logfile")

# log_file_name.txt will be created if not pre-exist
# if the file exits option 'a' will append new information to it
# if you like to make filename based on time, please check another post here

"""
import time
import os 

# print current date and time to the top of log file
# use file.write() to add more lines , information etc


file = open('log_file_name.txt','a')
for i in range(1):
    file.write('#'*80)
    file.write('\n')
    file.write('Today\'s date is: ')
    file.write(time.ctime())
    file.write('\n')
    file.write('\n')

file.close()


