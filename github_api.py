import github

"""
Creates the Github repos and invites collaborators
(Currently using a dictionary because I don't know what the output from the CSV will look like)
example dictionary
{
    "host_username": string,
    "host_auth_key": string,
    "teams": [
        {
            "team_name": string,
            "team_members": [
                string,
                string,
                ...
            ]
        },
        {
            "team_name": string,
            "team_members": [
                string,
                string,
                ...
            ]
        },
        ...
    ]
}
"""

test_dict = {
    "host_username": "Abdeet",
    "host_auth_key": "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",
    "teams": [
        {
            "team_name": "team1",
            "team_members": [
                "Abdeet",
                "jackiecattell",
            ]
        },
        {
            "team_name": "team2",
            "team_members": [
                "03npan",
                "cattellj"
            ]
        },
        {
            "team_name": "team3",
            "team_members": [
                "Dede-mi",
                "summerw1015"
            ]
        }
    ]
}

def create_github_repos(info_dict):
    host_instance = github.Github(info_dict["host_auth_key"])
    host_user = host_instance.get_user()
    for team in info_dict["teams"]:
        try:
            repo = host_user.create_repo(team["team_name"])
            print(f"Created repo {repo.full_name}")
            for member in team["team_members"]:
                try:
                    repo.add_to_collaborators(member)
                    print(f"Added user {member} to {repo.full_name}")
                except:
                    print(f"User {member} does not correspond to a GitHub account")
            print(f"Link to repo: {repo.html_url}")
        except:
            print(f"Unable to create Github repository {team['team_name']}")


create_github_repos(test_dict)