import requests
from lxml import html
import numpy as np
import regex as re
import os
import errno
from rappersstates import *

#START WITH THIS SCRIPT AND MOVE TO 2_genius.py

#use this website as the source of all chart-topping songs
site = "http://www.billboard.com/charts/r-b-hip-hop-songs"

#all dates used to loop through the billboard webpages
file = open("weekdatesall.txt", "r")
data = file.read()
data = data.split('\n')

print(data)


for day in range(0, len(data)):
    date = data[day]
    date = re.sub(r"\t", '', date)
    year = date[0:4]
    print(year)
    week = date[5:10]

    #get the webpage which is equal to the union of the to variables
    page = requests.get(site+"/"+date)

    #just get the text from the HTML and search specifically for song and artist headers
    tree = html.fromstring(page.text)
    songs = tree.xpath('//h2[@class="chart-row__song"]/text()')
    artists = tree.find_class("chart-row__artist")

#basically one big regex process
    for song in range(0, len(songs)):
        songs[song] = re.sub(" [(].*", '', songs[song])

    for i in range(0, len(artists)):
        prep = artists[i].text_content()
        schoon = prep.replace('\n', '')
        schooner = schoon.replace('  ', '')
        artists[i] = schooner

    for i in range(0, len(songs)):
        entry = {'artist': artists[i], 'song': songs[i], 'year': year}
        fileartist = re.sub("feat.*", '', artists[i], flags=re.IGNORECASE)
        fileartist = re.sub("['-.,!?/\<>*|:\"]", '', fileartist)
        fileartist = re.sub(" and.*", '', fileartist, flags=re.IGNORECASE)
        fileartist = re.sub(" &.*", '', fileartist)
        fileartist = re.sub(" with.*", '', fileartist, flags=re.IGNORECASE).replace(" ", "")

        filesong = songs[i].replace(" ", "")
        filesong = re.sub("[.,!'?/\<>*|:\"]", '', filesong)
        filename = fileartist.upper()+filesong.lower()
        path = 'input/'+str(year)

        #make a directory if one is not created yet
        try:
            os.makedirs(path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

#loop through all the states to check whether an artist is contained in one of the lists
#if yes, save the song, artist, year, state, latitude and longitude as a python dict with Numpy
        print(fileartist)
        if fileartist.upper() in alabama:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Alabama'
            entry['latitude'] = 32.31823
            entry['longitude'] = -86.90230
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in arizona:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Arizona'
            entry['latitude'] = 34.04893
            entry['longitude'] = -111.09373
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in arkansas:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Arkansas'
            entry['latitude'] = 35.20105
            entry['longitude'] = -91.83183
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in california:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'California'
            entry['latitude'] = 36.77826
            entry['longitude'] = -119.41793
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in connecticut:
            print('YES')
            print("---", fileartist, filesong, "---")
            entry['state'] = 'Conneticut'
            entry['latitude'] = 41.60322
            entry['longitude'] = -73.08775
            entry['country'] = 'United States'
            np.save(path + "/" + str(year) + filename, entry)
        elif fileartist.upper() in florida:
            print('YES')
            print("---", fileartist, filesong, "---")
            entry['state'] = 'Florida'
            entry['latitude'] = 27.66483
            entry['longitude'] = -81.51575
            entry['country'] = 'United States'
            np.save(path + "/" + str(year) + filename, entry)
        elif fileartist.upper() in georia:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Georgia'
            entry['latitude'] = 32.16562
            entry['longitude'] = -82.90008
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in illinois:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Illinois'
            entry['latitude'] = 40.63312
            entry['longitude'] = -89.39853
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in iowa:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Iowa'
            entry['latitude'] = 41.87800
            entry['longitude'] = -93.09770
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in kansas:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Kansas'
            entry['latitude'] = 39.01190
            entry['longitude'] = -98.48425
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in kentucky:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Kentucky'
            entry['latitude'] = 37.83933
            entry['longitude'] = -84.27002
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in louisiana:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Louisiana'
            entry['latitude'] = 30.98430
            entry['longitude'] = -91.96233
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in maine:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Maine'
            entry['latitude'] = 45.25378
            entry['longitude'] = -69.44547
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in maryland:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Maryland'
            entry['latitude'] = 39.04575
            entry['longitude'] = -76.64127
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in massachusetts:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Massachusetts'
            entry['latitude'] = 42.40721
            entry['longitude'] = -71.38244
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in michigan:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Michigan'
            entry['latitude'] = 44.31484
            entry['longitude'] = -85.60236
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in minnesota:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Minnesota'
            entry['latitude'] = 46.72955
            entry['longitude'] = -94.68590
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in mississippi:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Mississippi'
            entry['latitude'] = 32.35467
            entry['longitude'] = -89.39853
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in missouri:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Missouri'
            entry['latitude'] = 37.96425
            entry['longitude'] = -91.83183
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in nebraska:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Nebraska'
            entry['latitude'] = 41.49254
            entry['longitude'] = -99.90181
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in nevada:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Nevada'
            entry['latitude'] = 38.80261
            entry['longitude'] = -116.41939
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in newjersey:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'New Jersey'
            entry['latitude'] = 40.05832
            entry['longitude'] = -74.40566
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in newyork:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'New York'
            entry['latitude'] = 43.29943
            entry['longitude'] = -74.21793
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in northcarolina:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'North Carolina'
            entry['latitude'] = 35.75957
            entry['longitude'] = -79.01930
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in ohio:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Ohio'
            entry['latitude'] = 40.41729
            entry['longitude'] = -82.90712
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in oregon:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Oregon'
            entry['latitude'] = 43.80413
            entry['longitude'] = -120.55420
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in pennsylvania:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Pennsylvania'
            entry['latitude'] = 41.20332
            entry['longitude'] = -77.19452
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in rhodeisland:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Rhode Island'
            entry['latitude'] = 41.58009
            entry['longitude'] = -71.47743
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in southcarolina:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'South Carolina'
            entry['latitude'] = 33.83608
            entry['longitude'] = -81.16372
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in tennessee:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Tennessee'
            entry['latitude'] = 35.51749
            entry['longitude'] = -86.58045
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in texas:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Texas'
            entry['latitude'] = 31.96860
            entry['longitude'] = -99.90181
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in virginia:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Virginia'
            entry['latitude'] = 37.43157
            entry['longitude'] = -78.65689
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in washington:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Washington'
            entry['latitude'] = 47.75107
            entry['longitude'] = -120.74014
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in westvirginia:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'West Virginia'
            entry['latitude'] = 38.59763
            entry['longitude'] = -80.45490
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        elif fileartist.upper() in wisconsin:
            print('YES')
            print("---",fileartist, filesong,"---")
            entry['state'] = 'Wisconsin'
            entry['latitude'] = 43.78444
            entry['longitude'] = -88.78787
            entry['country'] = 'United States'
            np.save(path+"/"+str(year)+filename, entry)
        else: pass