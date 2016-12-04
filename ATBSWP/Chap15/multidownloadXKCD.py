#!/usr/bin/python3
# multidownloadXKCD.py - Downloads XKCD comics using multiple threads

import requests, os, bs4, threading
os.makedirs('XKCD', exist_ok=True) # store comics in ./XKCD

def downloadXKCD(startComic, endComic):
	for urlNumber in range(startComic, endComic):
		# Download the page.
		print('Downloading page http://xkcd.com/%s...' % (urlNumber))
		res = requests.get('http://xkcd.com/%s' % (urlNumber))
		res.raise_for_status()
		
		soup = bs4.BeautifulSoup(res.text)
		
		# Find the URL of the comic img
		comicElem = soup.select('#comic img')
		if comicElem == []:
			print('Could not find comic image %s.')
		else:
			comicUrl = ('http:' + comicElem[0].get('src'))
			# Download the image.
			print('Downloading image %s...' % (comicUrl))
			res = requests.get(comicUrl)
			res.raise_for_status()
			
			# Save image to ./XKCD
			imageFile = open(os.path.join('XKCD', (str(urlNumber) + '_' + os.path.basename(comicUrl))), 'wb')
			for chunk in res.iter_content(100000):
				imageFile.write(chunk)
			imageFile.close()
			
# Create and start the Thread objects.
downloadThreads = []		# a list of all the Thread objects
for i in range(1, 101, 10):	# loops 10 times, creates 10 objects
	downloadThread = threading.Thread(target=downloadXKCD, args=(i, i+10))
	downloadThreads.append(downloadThread)
	downloadThread.start()

# Wait for all the threads to end.
for downloadThread in downloadThreads:
	downloadThread.join()
print('Finished.')
