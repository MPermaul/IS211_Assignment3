import argparse
import csv
import re
import urllib.request


def download_csv(url):
    """Function that takes in a url to a csv file and downloads it.
    :param url: argument for the url that contains the csv file
    :return html: the data from the csv file
    """
    # retrieve csv file via url and store it in a temporary location
    tempfile, headers = urllib.request.urlretrieve(url)

    # open the file, return contents to the caller
    html = open(tempfile)
    return html


def process_csv(localfile):
    """Function that will take in data from a csv file, store it in a list, and return it to the caller.
    :param localfile: argument representing the csv data
    :return csvlist: a list containing the data of a csv file
    """
    # list to store csv data
    csvlist = []
    
    # initialize csv reader and pass in the temp file opened 
    csvreader = csv.reader(localfile, delimiter=',')

    # loop through the reader and add each row to the csv list before returning it to caller
    for row in csvreader:
        csvlist.append(row)
    return csvlist


def search_image(csvlist):
    """Function that takes in a list and checks for website hits that are for pictures.
    :param csvlist: argument that contains data from csv file in the form of a list
    :return tuple: the total hits, hits for images, and percentage of hit that are images
    """
    # variable that will store how many hits are for gif, jpg, or png files
    counter = 0

    # loop that will iterate through the csv list
    for row in csvlist:
        # if statement to check the first item of each row in list using regex
        if re.search(r'\.(gif|GIF|jpg|JPG|jpeg|png|PNG)', row[0]):
            # increment counter on each hit
            counter += 1

    # calculate the percentage of hits that are gif, jpg, or png files
    percentage = (counter/(len(csvlist)))*100

    # return to caller percentage
    return len(csvlist), counter, percentage


def search_browser(csvlist):
    pass

def search_time_of_hits(csvlist):
    pass

def main():
    """Function that is called when script executes """

    # url to test the application
    url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'

    # call function to download csv data
    csv_file = download_csv(url)

    # call function to process the csv data
    csv_list = process_csv(csv_file)

    # call function to search for images
    image_stats = search_image(csv_list)

    print(f'Out of {image_stats[0]} requests, {image_stats[1]} were image requests.\n'
          f'This accounts for {image_stats[2]}% of all requests')


if __name__ == '__main__':

    main()
