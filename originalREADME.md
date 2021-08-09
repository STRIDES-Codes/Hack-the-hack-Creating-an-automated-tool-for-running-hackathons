# Hack-in-a-Box

## What It Does

This webapp allows you to automate the work that goes into running a codeathon. Simply provide information about your participants and follow the steps provided on the application to invite users to Calendar events, create Github repos, and create Slack channels. 

## How It Works

#### Spreadsheet

Users will have to provide a .CSV file with their participants information. The CSV has to follow a specific format, with the first four columns being "Name", "Email", "Project Name", and "Github Username". You can have any other columns after these, but make sure that these four are in the correct order or else the parser will not work.

To parse the CSV file, I used a javascript library called Papaparse to be able to go through the CSV. All of the API calls are made as a callback from the result of parsing the CSV file.

#### APIs

For this project, I used the Google Calendar, Github, and Slack APIs. Here are the references to the specific calls that are made:
- [Insert Event]
- [Update Event]
- [Create Repo]
- [Update Repo]




##  How To Run
This app is very easy to install and run on your browser. First, clone this git repository to your computer by running this command in a terminal.
```sh
$ git clone https://github.com/NIH-CIF/HackinaBox
```
Next, cd into the new directory and run the command to run the server.
```sh
$ cd HackinaBox
```
```sh
$ python -m http.server 8000
```

Last, navigate to http://localhost:8000/auth.html in your browser, and the app will be running locally on your computer!

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
[Insert Event]: <https://developers.google.com/calendar/v3/reference/events/insert>
[Update Event]: <https://developers.google.com/calendar/v3/reference/events/update>
[Create Repo]: <https://docs.github.com/en/free-pro-team@latest/rest/reference/repos#create-an-organization-repository>
[Update Repo]: <https://docs.github.com/en/free-pro-team@latest/rest/reference/repos#update-a-repository>

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>

## NIH Civic Digital Fellow
This project was completed by Ruben Cuevas, University of California San Diego (UCSD) Computer Science student, under the direction of his NIH mentor Dr. Allissa Dilman, Outreach Director in the Office of Data Science Strategy (ODSS). 
