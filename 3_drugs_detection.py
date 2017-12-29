import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
import numpy as np
import glob
import errno
import regex as re
from wordlist import *
import copy
import os
java_path = "C:\Program Files (x86)\Java\jre1.8.0_151"
os.environ['JAVAHOME'] = java_path
songs = 'output/'

#RUN 4_sum_ne.py AFTER THIS

#loop through the years+1 you're interested in
for year in range(1980,2018):
    print(year)
    location = songs + str(year) + '/'
    print(location)

    #loop through everything in the directory
    for item in glob.glob(location + "*.npy"):
        print(item)
        info = np.load(item).item()
        song_title = info['song']
        artist_name = info['artist']
        lyrics = info['lyrics']
        print(info['song'], info['artist'])
        for zin in range(0, len(lyrics)):
            zin_split = lyrics[zin].split()
            for loopie in range(0, len(zin_split)):
                word = zin_split[loopie].lower()
                word = re.sub("[\u200b'-.,/\?!:\"]", '', word).replace(" ", "")
                #make word chunks in order to detect words such as Mary Jane or Remy Martin
                chunk = 'nonsense'
                if loopie > 0:
                    old_word = zin_split[loopie-1].lower()
                    old_word = re.sub("[\u200b'-.,/\?!:\"]", '', old_word).replace(" ", "")
                    chunk = old_word + ' ' + word
                #create a whole new python dict that will eventually summarize all results per year, per state
                drugs = {}
                drugs['category'] = None
                drugs['hits'] = None
                drugs['sentiment'] = None
                drugs['year'] = year
                drugs['artist'] = [info['artist']]
                drugs['song'] = [info['song']]
                print(info['state'])
                drugs['state'] = info['state']
                filestate = info['state'].replace(' ', '').lower()
                drugs['latitude'] = info['latitude']
                drugs['longitude'] = info['longitude']
                filename = item[16:-4]
                print(filename)
                path = 'results/' + str(year) +'/'

                try:
                    os.makedirs(path)
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        raise

                #in short: per word/word chunk: loop through all lists containing potential drug references until a hit is made
                #if no hit is made, then move on
                #if a hit is made, add the category, number of hits, calculated sentiment of the sentence, the sentince itself and the alternative coordinates
                #save the file as YEARstateFILENAME_Drugcategory.npy
                #check whether such a file already exists
                #if so, add +1 hits, add the sentiment, add the line and save it
                for i in crack:
                    if chunk == i:
                        drugs['category'] = 'Crack'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude'] + 0.3
                        drugs['alt_longitude'] = drugs['longitude']
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']

                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'
                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)
                    elif word == i:
                        drugs['category'] = 'Crack'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude'] + 0.3
                        drugs['alt_longitude'] = drugs['longitude']
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']

                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'
                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)

                for i in drug_business:
                    if chunk == i:
                        drugs['category'] = 'Business'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            drugs['alt_latitude'] = drugs['latitude'] - 0.3
                            drugs['alt_longitude'] = drugs['longitude']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)
                    elif word == i:
                        drugs['category'] = 'Business'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude'] - 0.3
                        drugs['alt_longitude'] = drugs['longitude']
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)

                for i in weed:
                    if chunk == i:
                        drugs['category'] = 'Marijuana'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude']
                        drugs['alt_longitude'] = drugs['longitude'] - 0.3
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)
                    elif word == i:
                        drugs['category'] = 'Marijuana'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude']
                        drugs['alt_longitude'] = drugs['longitude'] - 0.3
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)

                for i in cocaine:
                    if chunk == i:
                        drugs['category'] = 'Cocaine'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude']
                        drugs['alt_longitude'] = drugs['longitude'] + 0.3
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)
                    elif word == i:
                        drugs['category'] = 'Cocaine'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude']
                        drugs['alt_longitude'] = drugs['longitude'] + 0.3
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)

                for i in hard_drugs:
                    if chunk == i:
                        drugs['category'] = 'Hard'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude'] + 0.3
                        drugs['alt_longitude'] = drugs['longitude'] + 0.3
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)
                    elif word == i:
                        drugs['category'] = 'Hard'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude'] + 0.3
                        drugs['alt_longitude'] = drugs['longitude'] + 0.3
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)

                for i in party_drugs:
                    if chunk == i:
                        drugs['category'] = 'Party'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude'] + 0.3
                        drugs['alt_longitude'] = drugs['longitude'] - 0.3
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)
                    elif word == i:
                        drugs['category'] = 'Party'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude'] + 0.3
                        drugs['alt_longitude'] = drugs['longitude'] - 0.3
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)

                for i in psychedelic:
                    if chunk == i:
                        drugs['category'] = 'Psychedelic'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude'] - 0.3
                        drugs['alt_longitude'] = drugs['longitude'] - 0.3
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)
                    elif word == i:
                        drugs['category'] = 'Psychedelic'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude'] - 0.3
                        drugs['alt_longitude'] = drugs['longitude'] - 0.3
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)

                for i in codeine:
                    if chunk == i:
                        if year > 1993:
                            drugs['category'] = 'Codeine'
                            drugs['hits'] = 1
                            drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                            drugs['line'] = [lyrics[zin]]
                            drugs['alt_latitude'] = drugs['latitude'] - 0.3
                            drugs['alt_longitude'] = drugs['longitude'] + 0.3
                            save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                            check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                            if os.path.isfile(check):
                                load = np.load(check).item()
                                load['hits'] += 1
                                load['sentiment'] += drugs['sentiment']
                                load['line'] += drugs['line']
                                np.save(save_it, load)
                                print(load)
                            else:
                                np.save(save_it, drugs)
                    elif word == i:
                        if year > 1993:
                            drugs['category'] = 'Codeine'
                            drugs['hits'] = 1
                            drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                            drugs['line'] = [lyrics[zin]]
                            drugs['alt_latitude'] = drugs['latitude'] - 0.3
                            drugs['alt_longitude'] = drugs['longitude'] + 0.3
                            save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                            check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                            if os.path.isfile(check):
                                load = np.load(check).item()
                                load['hits'] += 1
                                load['sentiment'] += drugs['sentiment']
                                load['line'] += drugs['line']
                                np.save(save_it, load)
                                print(load)
                            else:
                                np.save(save_it, drugs)

                for i in prescription_drugs:
                    if chunk == i:
                        drugs['category'] = 'Prescription'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude'] + 0.5
                        drugs['alt_longitude'] = drugs['longitude']
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)
                    elif word == i:
                        drugs['category'] = 'Prescription'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude'] + 0.5
                        drugs['alt_longitude'] = drugs['longitude']
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)

                for i in beer:
                    if chunk == i:
                        drugs['category'] = 'Beer'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude']
                        drugs['alt_longitude'] = drugs['longitude']
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)
                    elif word == i:
                        drugs['category'] = 'Beer'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude']
                        drugs['alt_longitude'] = drugs['longitude']
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)

                for i in wine:
                    if chunk == i:
                        drugs['category'] = 'Wine'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude']
                        drugs['alt_longitude'] = drugs['longitude']
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)
                    elif word == i:
                        drugs['category'] = 'Wine'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude']
                        drugs['alt_longitude'] = drugs['longitude']
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)

                for i in cognac:
                    if chunk == i:
                        drugs['category'] = 'Cognac'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude']
                        drugs['alt_longitude'] = drugs['longitude']
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)
                    elif word == i:
                        drugs['category'] = 'Cognac'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude']
                        drugs['alt_longitude'] = drugs['longitude']
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)

                for i in drinks:
                    if chunk == i:
                        drugs['category'] = 'Drinks'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude']
                        drugs['alt_longitude'] = drugs['longitude']
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)
                    elif word == i:
                        drugs['category'] = 'Drinks'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude']
                        drugs['alt_longitude'] = drugs['longitude']
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)

                for i in vodka:
                    if chunk == i:
                        drugs['category'] = 'Vodka'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude']
                        drugs['alt_longitude'] = drugs['longitude']
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)
                    elif word == i:
                        drugs['category'] = 'Vodka'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude']
                        drugs['alt_longitude'] = drugs['longitude']
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)

                for i in alcohol:
                    if chunk == i:
                        drugs['category'] = 'Alcohol'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude']
                        drugs['alt_longitude'] = drugs['longitude']
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)
                            print(drugs)
                    elif word == i:
                        drugs['category'] = 'Alcohol'
                        drugs['hits'] = 1
                        drugs['sentiment'] = analyzer.polarity_scores(lyrics[zin])['compound']
                        drugs['line'] = [lyrics[zin]]
                        drugs['alt_latitude'] = drugs['latitude']
                        drugs['alt_longitude'] = drugs['longitude']
                        save_it = path + str(year) + filestate + filename + '_' + drugs['category']
                        check = path + str(year) + filestate + filename + '_' + drugs['category'] + '.npy'

                        if os.path.isfile(check):
                            load = np.load(check).item()
                            load['hits'] += 1
                            load['sentiment'] += drugs['sentiment']
                            load['line'] += drugs['line']
                            np.save(save_it, load)
                            print(load)
                        else:
                            np.save(save_it, drugs)
                            print(drugs)

#calculate an average sentiment score for each category per song
for year in range(1980, 2018):
    loc = "results/" + str(year) + '/'
    for info in glob.glob(loc + "*.npy"):
        ne_chunk = np.load(info).item()
        print(ne_chunk)
        ne_chunk['sentiment'] = ne_chunk['sentiment'] / ne_chunk['hits']
        check = info[13:]
        np.save(loc+check, ne_chunk)