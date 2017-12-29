import glob
import errno
import os
import numpy as np

#RUN 5_summarize.py AFTER THIS

try:
    os.makedirs('data/')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

#loop through all items in results/
for year in range(1980, 2018):
    loc = "results/" + str(year) + '/'
    print(loc)
    for info in glob.glob(loc + "*.npy"):
        ne_chunk = np.load(info).item()
        print(ne_chunk)
        #make subcategories
        ne_chunk['sub_cat'] = ne_chunk['category']
        if ne_chunk['category'] == 'Beer' or ne_chunk['category'] == 'Wine' or ne_chunk['category'] == 'Cognac' or ne_chunk['category'] == 'Drinks' or ne_chunk['category'] == 'Champagne' or ne_chunk['category'] == 'Vodka':
            ne_chunk['category'] = 'Alcohol'
        if ne_chunk['category'] == 'Crack':
            ne_chunk['category'] = 'Hard'
        if ne_chunk['category'] == 'Psychedelic':
            ne_chunk['category'] = 'Party'

        check = 'data/' + str(ne_chunk['year']) + ne_chunk['state'] + '_' + ne_chunk['category'] + '.npy'

        #check whether a file already exists in data/
        if os.path.isfile(check):
            #open the file in output/ and add {artist, song, hits, line, sentiment} to the file and save it
            load = np.load(check).item()
            load['artist'] += ne_chunk['artist']
            load['song'] += ne_chunk['song']
            load['hits'] += ne_chunk['hits']
            load['line'] += ne_chunk['line']
            load['sentiment'] += ne_chunk['sentiment']
            np.save(check, load)
        # if not
        else:
            #save the file as values of the check variable in output/
            np.save(check, ne_chunk)
