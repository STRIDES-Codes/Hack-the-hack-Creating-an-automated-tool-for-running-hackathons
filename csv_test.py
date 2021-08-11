import csv, random, github, sys

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
            
            # make the teams and repositories
            teams = make_teams(fields, rows)
            create_github_repos(teams)
        else:
            print("Error: missing required fields. Headers of csv file must include: 'name', 'email', and 'github'. Optional headers include: 'project'.")

# function to create randomized teams and save into JSON objects
def random_teams(fields, rows, num_teams):
    # print("rand teams") # debug
    num_people = len(rows)
    temp_list = rows.copy() # list of people left
    i = 1 # team counter
    
    # JSON object that stores everything
    final_object = {
        "host": {
            "github_username": "",
            "github_auth_key": ""
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
    # print(final_object) # debug
    return final_object
    
# function to group teams based on project/other specification
def make_teams(fields, rows):
    # JSON object that stores everything
    final_object = {
        "host": {
            "github_username": "",
            "github_auth_key": ""
        },
        "teams": [

        ]
    }
    
    # check if the hackathon creator has already assigned projects to participants
    if "project" in fields:
        project_index = fields.index("project") # get column used for project in csv
        
        # create team object for those not assigned a project - loop below needs at least one team to search
        team_object = {
            "team_name": "",
            "members": [

            ]
        }
        final_object["teams"].append(team_object)
        
        # loop through rest of people
        for row in rows:
            found = False
            # make team member object
            member_object = {
                "name": row[fields.index("name")],
                "email": row[fields.index("email")],
                "github_username": row[fields.index("github")]
            }
            # if (row[project_index] == ""):
                #print("empty")
            # check each team in list of teams
            for team in final_object["teams"]:
                # if team already exists, add to team
                if row[project_index] == team["team_name"]:
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
                team_object["members"].append(member_object)
                final_object["teams"].append(team_object)
        # print(final_object) # debug
        
        # make sure there are other teams besides unassigned people
        if len(final_object["teams"]) > 1:        
            # values for tracking smallest team size and index of that team
            min = sys.maxsize
            min_index = 0
                    
            # loop through unassigned people to add them to smallest teams
            for member in final_object["teams"][0]["members"]:
                # loop through all teams and track smallest team
                for i in range(1, len(final_object["teams"])):
                    if len(final_object["teams"][i]["members"]) < min:
                        min = len(final_object["teams"][i]["members"])
                        min_index = i
                # add member to smallest team and reset tracking variables
                final_object["teams"][min_index]["members"].append(member)
                min = sys.maxsize
                min_index = 0
            
            final_object["teams"].pop(0) # remove team of unassigned people
        # no one was actually assigned a project
        else:
            # inform that project column was empty and project header should be removed
            # prompt for num of teams?
            num_teams = 3 # temp placeholder
            final_object = random_teams(fields, rows, num_teams)
    # no projects pre-assigned, teams will be randomized
    else:
        # prompt for num of teams?
        num_teams = 3 # temp placeholder
        final_object = random_teams(fields, rows, num_teams)
    return final_object
        
# field value validator - make sure necessary headers are in csv file
def val_check(vals):
    if "name" in vals and "email" in vals and "github" in vals:
        return True
    return False

# create github repositories for each team and invites collaborators
def create_github_repos(info_dict):
    host_instance = github.Github(info_dict["host"]["github_auth_key"])
    host_user = host_instance.get_user()
    for team in info_dict["teams"]:
        try:
            repo = host_user.create_repo(team["team_name"])
            print(f"Created repo {repo.full_name}")
            for member in team["members"]:
                try:
                    repo.add_to_collaborators(member['github_username'])
                    print(f"Added user {member} to {repo.full_name}")
                except:
                    print(f"User {member} does not correspond to a GitHub account")
            print(f"Link to repo: {repo.html_url}")
        except:
            print(f"Unable to create Github repository {team['team_name']}")

# parse_csv("test.csv") # test the parser

def delete_teamnum_repos(repos_to_delete = ["team_1", "team_2", "team_3", "team_4", "team_5"]):
    host_instance = github.Github("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")
    host_user = host_instance.get_user()
    for repo in host_user.get_repos():
        #print(repo.name)
        if repo.name in repos_to_delete:
            print(repo.name)
            repo.delete()

# delete_teamnum_repos()


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
