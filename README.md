# IS211_Assignments3
Week 3 Assignment 3

Author: Moses Permaul - moses.permaul13@spsmail.cuny.edu

Application Details:

1) This application is designed to run via command line and will try to read a csv file via a url.

2) The script requires a url argument when running. Entering no argument will exit the script.
    
	python assignment3.py http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv
		
	python assignment3.py
		
		Message displayed:
			usage: assignment3.py [-h] url
			assignment3.py: error: the following arguments are required: url

3) The application will try to open a url, read the csv data to memory, process the csv data, and then display some stats.

4) A message will be displayed in the console if there are issues with the url.
	
	ex: 
		The url is invalid --> passed in https://s3.amazonaws.co
			Message displayed:
				"We are unable to reach the server. Please check your url!"

5) A message will be displayed in the console if the url is valid and there is nothing to process.

6) A message will be displayed in the console if the url is valid, but the csv data can't be process.

