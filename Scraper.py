import requests
from bs4 import BeautifulSoup
import os

# URL of the webpage you want to access
url = "https://msd.govt.nz/about-msd-and-our-work/publications-resources/statistics/benefit/index.html"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the content of the request with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <a> tags with href attributes that contain the specific string
a_tags = soup.find_all('a', href=lambda x: x and "/publications-resources/statistics/benefit" in x)

# Loop through the found a_tags
for a_tag in a_tags:
    file_url = a_tag['href']
    
    # Check if the file_url is a relative path
    if file_url.startswith("/"):
        file_url = "https://msd.govt.nz" + file_url

    # Send a GET request to the file url
    file_response = requests.get(file_url)

    # Get the file name by splitting the file_url on the last slash
    file_name = file_url.split("/")[-1]

    # Open the file to write as binary - replace 'wb' with 'w' if you're downloading a text file
    if ('nzs-and-vp-tables' in file_name):
        with open(file_name, 'wb') as f:
            f.write(file_response.content)
            print(file_name)
