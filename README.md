# IS211_Assignments3
Week 3 Assignment 3

Author: Moses Permaul, moses.permaul13@spsmail.cuny.edu

Application Details:

1) This application is designed to run via command line and will try to read a csv file via a url.

2) The script requires a url argument when running. Entering no argument will exit the script.
    
	python assignment3.py http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv
		
	python assignment3.py
		
		Message displayed:
			usage: assignment3.py [-h] url
			assignment3.py: error: the following arguments are required: url

3) The application will try to open a url, read the csv data to memory, process the csv data, and then display some stats.


