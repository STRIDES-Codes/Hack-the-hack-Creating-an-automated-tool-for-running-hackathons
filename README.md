# Hack-the-hack-Creating-an-automated-tool-for-running-hackathons

## What is it?
The hackathon (or codeathon) are events ran across the globe. They are used to bring people from all backgrounds and experience levels together to create computational and data science tools or pipelines. 

## What is the problem?
Hack(code)athon organizers have a lot of administrative duties to set up before an event. 
The aim of this project is to automate some of that administrative work. A previous version of this was written in HTML and JavaScript, but we decided to redo the program from scratch in Python. 

Automation can be used to:
 1) randomize and sort participants into teams
 2) create Google documents with dates, times, team names, and Github repos listed

## Why do this?
An automated system for this process would improve efficiency, speed, and ease of the event itself for all involved. 

## Diagram of processes
![alt text](https://docs.google.com/drawings/d/e/2PACX-1vTUZnEbbunInRaQ6JCAM62nry_Y4job_lOI_c5roBZ2BxGQUKSfUdgWM2LaX0PN1PS3nUgmlceM1rt_/pub?w=960&h=720)

## Instructions for use
The web application (see here*, created with Flask) feeds in a CSV file and generates teams, Github repos, and Google Docs. To use, open web application and use prompt to select a pre-made CSV file.

The event organizer will need to provide a CSV file with the following information:
- Name, email, and Github username of participants
- First line of CSV file must include the GitHub authentication key followed by the Google Drive access token
- Second line of CSV file must include "name", "email", and "github" (any order, case does not matter)
- *Optional*: project each participant is working on (header must also include "project" somewhere)
  - If multiple people are working on one project, the project name *must* be spelled the same for all individuals or they will be added to different repositories
  - If some individuals are not assigned a project, they will be placed into existing teams with the fewest members

In addition, the event organizer will need to provide their access token or refresh token for the Google Drive API. To achieve this. The user should go to OAuth 2.0 Playground (google.com), select Drive API, authorize the API, thereby providing access to the organizer’s Google Drive Account, and then exchange the authorization code provided for tokens. After scrolling down on the right side of the window, the user should see a part of the response formatted as follows:
{
  "access_token": "ya29.a0***",
  "scope": "https://www.googleapis.com/auth/drive https://www.googleapis.com/auth/documents",
  "token_type": "Bearer",
  "expires_in": 3599,
  "refresh_token": "1//04rt****"
}

In order to use the web application, the user should copy the access token on the first line into the web application. Please note that access tokens expire 24 hours after generation, so it may be necessary to regenerate access tokens and restore permissions to the Google Drive API.

Refer to the [example file](https://github.com/STRIDES-Codes/Hack-the-hack-Creating-an-automated-tool-for-running-hackathons/blob/main/example.csv) or the [raw file of the example](https://raw.githubusercontent.com/STRIDES-Codes/Hack-the-hack-Creating-an-automated-tool-for-running-hackathons/main/example.csv) if you need a guide.

## Code
[ManuscriptMaker.py](https://github.com/STRIDES-Codes/Hack-the-hack-Creating-an-automated-tool-for-running-hackathons/blob/main/ManuscriptMaker.py) combines the code for the different portions, making it the complete tool. 

[csv_test.py](https://github.com/STRIDES-Codes/Hack-the-hack-Creating-an-automated-tool-for-running-hackathons/blob/main/csv_test.py) is the code for the CSV parser to create teams

[github_api.py](https://github.com/STRIDES-Codes/Hack-the-hack-Creating-an-automated-tool-for-running-hackathons/blob/main/github_api.py) is the code for the Github repository generator.

## APIs used
 -Google Drive
 
 -Github
 
 -Flask

## Packages (Python)
certifi==2021.5.30

cffi==1.14.6

charset-normalizer==2.0.4

click==8.0.1

colorama==0.4.4

Deprecated==1.2.12

Flask==2.0.1

idna==3.2

importlib-metadata==4.6.3

itsdangerous==2.0.1

Jinja2==3.0.1

lxml==4.6.3

MarkupSafe==2.0.1

numpy==1.21.1

pandas==1.3.1

pycparser==2.20

PyGithub==1.55

PyJWT==2.1.0

PyNaCl==1.4.0

python-dateutil==2.8.2

python-docx==0.8.11

pytz==2021.1

requests==2.26.0

six==1.16.0

typing-extensions==3.10.0.0

urllib3==1.26.6

Werkzeug==2.0.1

wrapt==1.12.1

zipp==3.5.0

## Additional Functionality 
Originally, including the generation of Slack channels (#general, #help-desk, and #[team]) were going to be included in this project, but due to time constraints and problems with using the Slack API, it was excluded from this project for the time being. Future projects may consider incorporating the generation of Slack channels and listing them in the Google Docs associated with this project.

## Members  
- Jackie Cattell
- Nathan Pan
- Delight Nweneka
- Abhiraman Senthilkumar
- Amanda Taylor
- Brittany DuBose
<!--[image](https://user-images.githubusercontent.com/75758331/129243554-b7dc42fa-c66a-4679-9ae1-ec4819d1e2f6.png)-->
