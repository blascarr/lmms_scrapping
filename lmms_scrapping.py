import urllib.request
import requests
from bs4 import BeautifulSoup
import wget

base_url = 'https://lmms.io'
page_begin = 548
page_end = 19000
for i in range(page_begin, page_end):

	url = 'https://lmms.io/lsp/?action=show&file='+str(i)
	data = urllib.request.urlopen( url ).read().decode()
	soup = BeautifulSoup( data ,features="lxml")
	tags = soup('a')

	for tag in tags:
		
		if(  tag.get('href') != None and ( tag.get('href').endswith('.mmpz') or tag.get('href').endswith('.ogg') or tag.get('href').endswith('.xpf') ) ) :
			
			print( 'Archive N: '+str(i) )
			archive_url = base_url + tag.get('href')
			print( archive_url )
			r = requests.get(archive_url)
			if( r.status_code != 404) :
				filename = wget.download( archive_url, 'lmms', bar=None)
			else:
				print('Error 404')

