import urllib.request
import requests
from bs4 import BeautifulSoup
import wget

import argparse
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir", default='',
	help="Directory to save")
ap.add_argument("-f", "--from", default=0, type=int,
	help="From begin number")
ap.add_argument("-t", "--to", default=19000, type=int,
	help="To end number")

args = vars(ap.parse_args())

directory = format(args["dir"])


base_url = 'https://lmms.io'
page_begin = format(args["from"])
page_end = format(args["to"])


for i in range( int(page_begin), int(page_end) ):

	url = 'https://lmms.io/lsp/?action=show&file='+str(i)
	data = urllib.request.urlopen( url ).read().decode()
	soup = BeautifulSoup( data ,features="lxml")
	tags = soup('a')

	for tag in tags:
		
		if(  tag.get('href') != None and ( tag.get('href').endswith('.mmpz') or tag.get('href').endswith('.ogg') or tag.get('href').endswith('.xpf') ) ) :
			
			print( 'LMMS Resource N: '+str(i) )
			archive_url = base_url + tag.get('href')
			print( archive_url )
			r = requests.get(archive_url)
			if( r.status_code != 404) :
				filename = wget.download( archive_url, directory, bar=None)
			else:
				print('Error 404')

