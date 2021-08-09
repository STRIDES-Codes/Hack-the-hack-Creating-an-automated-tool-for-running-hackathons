# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv

filename = "test.csv"

fields = []
rows = []

with open(filename, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    fields = next(csv_reader)
  
    for row in csv_reader:
        rows.append(row)
  
    print("Total no. of rows: %d"%(csv_reader.line_num))
  
print('Field names are:' + ', '.join(field for field in fields))

# project_col = 2
# name_col = 0
# teams = []

print('\n')
for row in rows:
    #for col in row:   
        #print(col)
    #print("\n")
    
    print(', '.join(col for col in row))
    # print(row[project_col])
    
    # for x in range(len(teams)):
    #     if row[project_col] in teams[x]:
    #         teams.index(row[project_col]).append(row[name_col])
    #     else:
    #         teams.append([row[project_col]])
        
    # # for x in range(len(teams))
    # print(*teams)