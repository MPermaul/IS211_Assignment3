import argparse
import csv
import requests
from datetime import datetime


def download_csv_data(url):
    # open a request session with passed in url
    with requests.Session() as s:
        download = s.get(url)
    
    # decode the url to unicode utf-8 and return to caller
    decoded_url = download.content.decode('utf-8')


def process_csv_data(data):
    # initialize csv reader and pass in url data, split by lines wiith delimiter set to comma
    csv_reader = csv.reader(decoded_content.splitlines(), delimiter=',')
    csv_list = list(csv_reader)

    for row in csv_list:
        print(row)


# url to test the application
url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'

# call function to download csv data
csv_data = download_csv_data(url)

# call function to process the csv data
process_csv_data(csv_data)



# initialize a parser, add param url, and parse param as an argument
#parser = argparse.ArgumentParser(description='Data Url CSV Processor')
#parser.add_argument('url', type=str, help='Url where CSV file is stored')
#args = parser.parse_args()
