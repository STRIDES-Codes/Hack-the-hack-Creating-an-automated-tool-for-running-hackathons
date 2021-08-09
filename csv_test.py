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

print('\n')
for row in rows:
    
    print(', '.join(col for col in row))
