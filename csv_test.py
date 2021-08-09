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

# function to create randomized teams and write the information for each team to a separate csv file
def random_teams(num_teams):
    num_people = len(rows)
    temp_list = rows.copy()
    i = 1
    while num_people > 0 and num_teams > 0:
        team = random.sample(temp_list, int(num_people/num_teams))
        for x in team:
            temp_list.remove(x)
        num_people -= int(num_people/num_teams)
        num_teams -= 1
        print(team)
        with open('team_' + str(i) + '.csv', 'w') as file:
            writer = csv.writer(file, lineterminator = '\n')
            writer.writerow(fields)
            writer.writerows(team)
        i += 1
