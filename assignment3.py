import argparse
import csv
import re
import urllib.request


def download_csv(url):

    # retrieve csv file via URL and store it in a temporary location
    tempfile, headers = urllib.request.urlretrieve(url)

    # open the file, return contents to the caller
    html = open(tempfile)

    return html


def process_csv(localfile):

    # list to store csv data
    csvlist = []
    
    # initialize csv reader and pass in the temp file opened 
    csvreader = csv.reader(localfile, delimiter=',')

    # loop through the reader and add each row to the csv list
    for row in csvreader:
        csvlist.append(row)

    return csvlist


def search_image(csvlist):

    counter = 0

    for row in csvlist:
        if re.search(r'jpg|JPG\.$', row[0]):
            counter += 1

    print(counter)


def search_browse(csvlist):
    pass

def search_time_of_hits(csvlist):
    pass


# url to test the application
url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'

# call function to download csv data
csv_file = download_csv(url)

# call function to process the csv data
csv_list = process_csv(csv_file)

# call function to search for images
search_image(csv_list)
