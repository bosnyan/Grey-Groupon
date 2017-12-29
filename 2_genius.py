import requests
from bs4 import BeautifulSoup
import numpy as np
import regex
import glob
import errno
import os

#AFTER THIS, CONTINUE WITH 3_drugs_detection.py

#all urls necessary for this script
base_url = "http://api.genius.com"
search_url = base_url + '/search?q='
#get your own token from the Genius API
headers = {'Authorization': 'token'}

#loop through the years+1 you're interested in
for year in range(1980, 2018):
    print(year)
    path = "input/"+str(year)+"/"
    print(path)
    for i in glob.glob(path+"*.npy"):
        #just keep the filename from the file you just opened
        file = (i[11:-4])
        print(file)
        ne_chunk = np.load(i).item()
        info = np.load(i).item()
        song_title = info['song']
        #REGEXXXX
        song_title = regex.sub("[(.*)]", "", song_title).lower()
        song_title = regex.sub("'s", 'is', song_title, flags=regex.IGNORECASE)
        song_title = regex.sub("isn't", 'is not', song_title, flags=regex.IGNORECASE)
        song_title = regex.sub("'re", 'are', song_title, flags=regex.IGNORECASE)
        search_title = regex.sub("aren't", 'are not', song_title, flags=regex.IGNORECASE)
        song_title = regex.sub("[\u200b'-.,/\?!:\"]", '', search_title).replace(" ", "")
        artist_name = info['artist']
        artist_name = regex.sub("[(.*)]", "", artist_name).lower()
        artist_name = regex.sub("'s", 'is', artist_name, flags=regex.IGNORECASE)
        artist_name = regex.sub("isn't", 'is not', artist_name, flags=regex.IGNORECASE)
        artist_name = regex.sub("'re", 'are', artist_name, flags=regex.IGNORECASE)
        artist_name = regex.sub("aren't", 'are not', artist_name, flags=regex.IGNORECASE)
        artist_name = regex.sub("feat.*", '', artist_name, flags=regex.IGNORECASE)
        artist_name = regex.sub(" and.*", '', artist_name, flags=regex.IGNORECASE)
        artist_name = regex.sub(" &.*", '', artist_name)
        artist_search = regex.sub(" with.*", '', artist_name, flags=regex.IGNORECASE)
        artist_name = regex.sub("[\u200b'-.,/\?!:\"]", '', artist_search).replace(" ", "")
        #mixing a bit of dutch out of sheer confusion and frustration, sorry.
        zoek_url = search_url + artist_search + "/" + search_title
        response = requests.get(zoek_url, headers=headers)
        json = response.json()
        #make the song_info none in order to prevent duplicate lyrics when no hit is found
        song_info = None
        #go through all the results..
        for hit in json["response"]["hits"]:
            genius_song = hit["result"]["title"]

            #regex it..
            genius_song = regex.sub("[(.*)]", "", genius_song).lower()
            genius_song = regex.sub("'s", 'is', genius_song, flags=regex.IGNORECASE)
            genius_song = regex.sub("isn't", 'is not', genius_song, flags=regex.IGNORECASE)
            genius_song = regex.sub("'re", 'are', genius_song, flags=regex.IGNORECASE)
            genius_song = regex.sub("aren't", 'are not', genius_song, flags=regex.IGNORECASE)
            genius_song = regex.sub("[\u200b'?!-/\.,()\"]",'',genius_song).replace(" ", "")

            #do the same with the artist name..
            genius_artist = hit["result"]["primary_artist"]["name"]
            genius_artist = regex.sub("[(.*)]", "", genius_artist).lower()
            genius_artist = regex.sub("'s", 'is', genius_artist, flags=regex.IGNORECASE)
            genius_artist = regex.sub("isn't", 'is not', genius_artist, flags=regex.IGNORECASE)
            genius_artist = regex.sub("'re", 'are', genius_artist, flags=regex.IGNORECASE)
            genius_artist = regex.sub("aren't", 'are not', genius_artist, flags=regex.IGNORECASE)
            genius_artist = regex.sub("feat.*", '', genius_artist, flags=regex.IGNORECASE)
            genius_artist = regex.sub("[\u200b'-.,/\?!:\"]", '', genius_artist)
            genius_artist = regex.sub(" and.*", '', genius_artist, flags=regex.IGNORECASE)
            genius_artist = regex.sub(" &.*", '', genius_artist)
            genius_artist = regex.sub(" with.*", '', genius_artist, flags=regex.IGNORECASE).replace(" ", "")
            print(genius_song, song_title, genius_artist, artist_name)

            #compare the result from genius to the song title retrieved from the file
            if genius_song == song_title:
                print(genius_song, song_title, genius_artist, artist_name)
                #if yes, save it and move on
                song_info = hit
                break
            else:
                song_info = None
        if song_info is not None:
            #get the ID of the song
            song_api_path = song_info["result"]["api_path"]
            song_url = base_url + song_api_path
            response = requests.get(song_url, headers=headers)
            json = response.json()
            path = json["response"]["song"]["path"]
            #add the ID to the base URL of genius.com/ and voila!
            page_url = "http://genius.com" + path
            page = requests.get(page_url)

            #parse the HTML and look for the lyrics contained in the p tag
            html = BeautifulSoup(page.text, "html.parser")
            lyrics = html.p.get_text()

            #regex of course, gotta make it clean
            lyrics = regex.sub("[\[].*[\]]", '', lyrics)
            lyrics = regex.sub(r'[^\x00-\x7F]+', '', lyrics)
            clean = lyrics.replace('lyrics', '')
            cleaner = clean.split('\n')
            cleanest = list(filter(None, cleaner))
            print(cleanest)
            info['lyrics'] = cleanest

            #now with the lyrics included, save all the song information again as a python dict
            np_path = "output/" + str(year)
            # save a .txt file if you want to read the lyrics easily
            txt_path = "justtxt/" + str(year) + '/'

            try:
                os.makedirs(txt_path)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

            try:
                os.makedirs(np_path)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

            np.save(np_path+'/'+file, info)

            text = open(txt_path+"/"+file+".txt", 'w+')
            text.write(clean)

            text.close()