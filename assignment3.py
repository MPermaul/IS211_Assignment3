from csv import reader
from datetime import datetime
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import argparse
import re


def download_csv(url):
    """
    Function that takes in a url with a csv file, opens it, and returns the data back to caller as string
    :param url: argument for the url that contains the csv file
    :return html: the string data of the csv file
    """
    # retrieve csv file via url, read the data, decode data from byte to unicode
    with urlopen(url) as response:
        html = response.read().decode('utf-8')

    # return html to caller
    return html


def process_csv(csvfile):
    """
    Function that will take in string data from a csv url, process it to a list, and return it to the caller.
    :param csvfile: argument representing the string csv data
    :return csvlist: a list containing the processed data of csvfile
    """
    # empty list to store csv data
    csvlist = []

    # initialize csv reader and pass string data, splitting it by lines
    csvreader = reader(csvfile.splitlines())

    # create loop to iterate through the csvreader
    for row in csvreader:

        # create indexes for each column, converting accessinfo  to datetime
        filepathinfo = row[0]
        accessinfo = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
        browserinfo = row[2]
        statusinfo = row[3]
        sizeinfo = row[4]

        # append each column as a list to csvlist
        csvlist.append([filepathinfo, accessinfo, browserinfo, statusinfo, sizeinfo])

    # return list to caller
    return csvlist


def search_image(csvlist):
    """
    Function that takes in a list and checks for website hits that are for pictures.
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
    percentage = (counter / (len(csvlist))) * 100

    # return to caller percentage
    return len(csvlist), counter, percentage


def search_browser(csvlist):
    """
    Function that checks User Agent for browser type.
    :param csvlist: argument that contains data from csv file in the form of a list
    :return:
    """
    # variables that will store how many of each were used for the hits
    chrome = 0
    firefox = 0
    explorer = 0
    safari = 0

    # loop that will iterate through the csv list
    for row in csvlist:
        # if statements to check what browser was used and increment it's counter
        if re.search(r'Chrome/[\d]{2}\.[\d.]\.[\d]{4}?\.[\d]', row[2]):
            chrome += 1
        elif re.search(r'Firefox/[\d]{2}?\.[\d]', row[2]):
            firefox += 1
        elif re.search(r'MSIE [\d][\d]?\.[\d];', row[2]):
            explorer += 1
        elif re.search(r'\) Version/[\d]\.[\d]\.[\d] Safari/[a-zA-z0-9]{9}', row[2]):
            safari += 1

    # return the count for each browser used
    return chrome, firefox, explorer, safari


def search_time_of_hits(csvlist):
    """
    Function that returns list of hits to a website based on hour of the hit.
    :param csvlist: argument that contains data from csv file in the form of a list
    :return: hourlist: list that contains the number of hits with list index being the hour
    """

    # empty list to store hits count by the hour, hour will be the index
    hourlist = []

    # counter that will determine if while loop should run
    counter = 0

    # while loop that will run and check each hour ending with hour 23
    while counter <= 23:

        # the variable that will store the number of hits per hour
        sum = 0

        # loop through the csvlist
        for row in csvlist:
            # for each row, check the datetime object hour value
            if row[1].hour == counter:
                # increment sum if we have a hit on the hour
                sum +=1

        # append sum for the hour to list and increment counter for the next hour
        hourlist.append(sum)
        counter += 1

    # return list of hours
    return(hourlist)


def main():
    """Function that is called when script executes """

    # initialize argument parser, add arguments, and then parse into script
    parser = argparse.ArgumentParser(description='Script that downloads csv data from URL')
    parser.add_argument('url', type=str, help='Url that contains a csv file.')
    args = parser.parse_args()

    # call download_csv function and pass in the url arg, print message to screen if there is an issue and exit
    try:
        csv_file = download_csv(args.url)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request. Please check your url!')
        print('Error code: ', e.code)
    except URLError as e:
        print('We are unable to reach the server. Please check your url!')
        print('Reason: ', e.reason)
    else:
        # try to pass the data to process_csv function, print message to screen and exit if issue
        try:
            csv_list = process_csv(csv_file)
        except:
            print('The application is unable to finish because the data from the url can\'t be processed.\n'
                  'Please check that the url contains a csv file with the proper setup.')
            exit()
        else:

            # call function to search for images
            image_stats = search_image(csv_list)

            print('File Request Stats:\n------------------\nOut of a total of {} requests, {} were image requests.\n'
                  'This accounts for {}% of all requests.\n'.format(image_stats[0],image_stats[1],image_stats[2]))

            # call function to search for browsers
            browser_stats = search_browser(csv_list)

            # set a maxbrowser variable to the browser that has the most usage
            if browser_stats[0] == max(browser_stats):
                maxbrowser = 'Chrome'
                browsercount = browser_stats[0]
            elif browser_stats[1] == max(browser_stats):
                maxbrowser = 'Firefox'
                browsercount = browser_stats[1]
            elif browser_stats[2] == max(browser_stats):
                maxbrowser = 'Internet Explorer'
                browsercount = browser_stats[2]
            else:
                maxbrowser = 'Safari'
                browsercount = browser_stats[3]

            print('Browser Stats:\n------------------\n{} was the most popular browser with {} users using it.'.format(maxbrowser, browsercount))

            # call function to check the hits per hour
            timelist = search_time_of_hits(csv_list)

            # create counter to represent index of list
            listcounter = 0

            print('\nHourly Hit Stats:')
            print('------------------')

            # loop through timelist, and print out message based on the listcounter and item for it
            for item in timelist:
                print('During hour {}, there were {} hits.'.format(listcounter, item))
                listcounter += 1


if __name__ == '__main__':

    # call main function to run program
    main()