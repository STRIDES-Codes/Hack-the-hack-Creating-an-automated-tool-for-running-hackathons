import csv, random

def parse_csv(filename):
    fields = []
    rows = []
    
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        fields = next(csv_reader)
        fields = [field.lower() for field in fields] # lowercase all fields
        
        # verify that necessary fields are present
        if val_check(fields):
            for row in csv_reader:
                rows.append(row)
                
            # debug statements
            # print("Total no. of rows: %d"%(csv_reader.line_num))
            # print('Field names are:' + ', '.join(field for field in fields))
            # print('')
            # for row in rows:
            #     print(', '.join(col for col in row))
            
            make_teams(fields, rows)
        else:
            print("Error: missing required fields. Header of csv file must contain: 'name', 'email', and 'github'.")

# function to create randomized teams and save into JSON objects
def random_teams(fields, rows, num_teams):
    # print("rand teams")
    num_people = len(rows)
    temp_list = rows.copy() # list of people left
    i = 1 # team counter
    
    # JSON object that stores everything
    final_object = {
        "host": {

        },
        "teams": [

        ]
    }
    
    # loop and keep making teams as long as there are people and teams left
    while num_people > 0 and num_teams > 0:
        team = random.sample(temp_list, int(num_people/num_teams)) # divide teams evenly and randomly
        for x in team:
            temp_list.remove(x) # remove people added to team from list of people available
        num_people -= int(num_people/num_teams) # keep track of num of people left
        num_teams -= 1 # keep track of num of teams left
        # print(team) # debug
        
        # object to store team info
        team_object = {
            "team_name": f"team_{i}",
            "members": [

            ]
        }
        
        # create object for each team member, include member info, and add to team
        for member in team:
            member_object = {
                "name": member[fields.index("name")],
                "email": member[fields.index("email")],
                "github_username": member[fields.index("github")]
            }
            team_object["members"].append(member_object)
        # add team to list of teams
        final_object["teams"].append(team_object)
        i += 1
    print(final_object) # debug
    
# function to group teams based on project
def make_teams(fields, rows):
    # JSON object that stores everything
    final_object = {
        "host": {

        },
        "teams": [

        ]
    }
    
    # check if the hackathon creator has already assigned projects to participants
    if "project" in fields:
        project_index = fields.index("project") # get column used for project in csv
        
        # create first team object and first member object - loop below needs at least one team to search
        team_object = {
            "team_name": rows[0][project_index],
            "members": [

            ]
        }
        member_object = {
            "name": rows[0][fields.index("name")],
            "email": rows[0][fields.index("email")],
            "github_username": rows[0][fields.index("github")]
        }
        # add member to team and team to list of teams
        team_object["members"].append(member_object)
        final_object["teams"].append(team_object)
        
        # loop through rest of people
        for row in rows[1:]:
            found = False
            # check each team in list of teams
            for team in final_object["teams"]:
                # if team already exists, create team member object and add to team
                if row[project_index] == team["team_name"]:
                    member_object = {
                        "name": row[fields.index("name")],
                        "email": row[fields.index("email")],
                        "github_username": row[fields.index("github")]
                    }
                    team["members"].append(member_object)
                    found = True
                    break
            # this person's team hasn't been created yet, create it and add them to the team
            if not found:
                team_object = {
                    "team_name": row[project_index],
                    "members": [
        
                    ]
                }
                member_object = {
                    "name": row[fields.index("name")],
                    "email": row[fields.index("email")],
                    "github_username": row[fields.index("github")]
                }
                team_object["members"].append(member_object)
                final_object["teams"].append(team_object)
        print(final_object) # debug
    # no projects pre-assigned, teams will be randomized
    else:
        # prompt for num of teams?
        num_teams = 3 # temp placeholder
        random_teams(fields, rows, num_teams)
        
# field value validator - make sure necessary headers are in csv file
def val_check(vals):
    if "name" in vals and "email" in vals and "github" in vals:
        return True
    return False

parse_csv("test.csv") # test the parser

# sample final JSON object

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
