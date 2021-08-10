import csv, random

filename = "test.csv"

fields = []
rows = []

with open(filename, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    fields = next(csv_reader)
    
    for row in csv_reader:
        rows.append(row)
  
    print("Total no. of rows: %d"%(csv_reader.line_num)) # debug
  
print('Field names are:' + ', '.join(field for field in fields)) # debug

print('\n')
for row in rows:
    print(', '.join(col for col in row)) # debug

# function to create randomized teams and write the information for each team to a separate csv file
def random_teams(num_teams):
    num_people = len(rows)
    temp_list = rows.copy()
    i = 1
    final_object = {
        "host": {

        },
        "teams": [

        ]
    }
    while num_people > 0 and num_teams > 0:
        team = random.sample(temp_list, int(num_people/num_teams))
        for x in team:
            temp_list.remove(x)
        num_people -= int(num_people/num_teams)
        num_teams -= 1
        print(team)
        team_object = {
            "team_name": f"team_{i}",
            "members": [

            ]
        }
        for member in team:
            member_object = {
                "name": member[0],
                "email": member[1],
                "github_username": member[2]
            }
            team_object["members"].append(member_object)
        final_object["teams"].append(team_object)
        i += 1
    print(final_object)

"""
{
    host: {
        ...
    }
    teams: [
        {
            "team_name": team1,
            "members": [
                {
                    "name": ,
                    "email": ,
                    "github_username": ,
                },
                {
                    "name": ,
                    "email": ,
                    "github_username": ,
                }
            ]
        },
        {
            "team_name": team2,
            "members": [
                {
                    ...
                },
                {
                    ...
                }
            ]
        }
    ]
}
"""
