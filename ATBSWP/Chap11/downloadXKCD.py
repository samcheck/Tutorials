#! /usr/bin/python3
# downloadXKCD.py - Scrapes XKCD for all the comics

import requests, os, bs4

url = 'http://xkcd.com' # starting URL
os.makedirs('./XKCD', exist_ok=True)  # store comics in local XKCD folder

while not url.endswith('#'):    # last prev element directs to xkcd.com/#
    # Download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Find the URL of the comic img
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image')
    else:
        try:
            comicURL = 'http:' + comicElem[0].get('src')
            # Download the image
            print('Downloading image %s...' % (comicURL))
            res = requests.get(comicURL)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue

    # Save the img to ./XKCD
    imageFile = open(os.path.join('./XKCD', os.path.basename(comicURL)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # Get the Prev button's URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done')
