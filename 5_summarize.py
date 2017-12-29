import glob
import errno
import os
import numpy as np

#AFTER COMPLETING THIS, RUN 6_csv_creator.py

"""This script summarizes the sentiment and final scores of the sum of all song per state, per year. 
A binary sentiment is given as well to judge whether a particular category is viewed as positive or negative by a 
particular state from a particular year. 
There are different variations of the script below running as well to filter out unnecessary data for different, more focused data sets."""

#SAVE EVERYTHING
try:
    os.makedirs('final/complete/no_year/')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

for file in glob.glob('data/' + "*.npy"):
    ne_chunk = np.load(file).item()
    filestate = ne_chunk['state'].replace(' ', '').lower()
    check = 'final/complete/no_year/' + str(ne_chunk['year']) + filestate + '_' + ne_chunk['category'] + '.npy'
    file_list = list(set(ne_chunk['song']))
    ne_chunk['diff_files'] = len(file_list)

    ne_chunk['score'] = round((ne_chunk['diff_files'] / 100) * ne_chunk['hits'], 2)
    del ne_chunk['song']
    del ne_chunk['artist']
    del ne_chunk['line']
    ne_chunk['sentiment_score'] = round(ne_chunk['sentiment'] / ne_chunk['diff_files'], 2)
    if ne_chunk['sentiment'] >=  -0.1:
        ne_chunk['sentiment'] = 'Positive'
        ne_chunk['se_short'] = 'POS'
    else:
        ne_chunk['sentiment'] = 'Negative'
        ne_chunk['se_short'] = 'NEG'

    print(ne_chunk)
    np.save(check, ne_chunk)

for file in glob.glob('final/complete/no_year/' + "*.npy"):
    ne_chunk = np.load(file).item()
    filestate = ne_chunk['state'].replace(' ', '').lower()
    check = 'final/complete/yearly/' + str(ne_chunk['year']) + '/' + str(ne_chunk['year']) + filestate + '_' + ne_chunk['category'] + '.npy'
    try:
        os.makedirs('final/complete/yearly/' + str(ne_chunk['year']) + '/')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    np.save(check, ne_chunk)
    print(ne_chunk)


#SAVE ALCOHOL
try:
    os.makedirs('final/alcohol/no_year/')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

for file in glob.glob('data/' + "*.npy"):
    ne_chunk = np.load(file).item()
    filestate = ne_chunk['state'].replace(' ', '').lower()
    check = 'final/alcohol/no_year/' + str(ne_chunk['year']) + filestate + '_' + ne_chunk['category'] + '.npy'
    file_list = list(set(ne_chunk['song']))
    ne_chunk['diff_files'] = len(file_list)

    ne_chunk['score'] = round((ne_chunk['diff_files'] / 100) * ne_chunk['hits'], 2)
    del ne_chunk['song']
    del ne_chunk['artist']
    del ne_chunk['line']
    ne_chunk['sentiment_score'] = round(ne_chunk['sentiment'] / ne_chunk['diff_files'], 2)
    if ne_chunk['sentiment'] >=  -0.1:
        ne_chunk['sentiment'] = 'Positive'
        ne_chunk['se_short'] = 'POS'
    else:
        ne_chunk['sentiment'] = 'Negative'
        ne_chunk['se_short'] = 'NEG'

    print(ne_chunk)
    if ne_chunk['category'] == 'Alcohol':
        np.save(check, ne_chunk)

for file in glob.glob('final/alcohol/no_year/' + "*.npy"):
    ne_chunk = np.load(file).item()
    filestate = ne_chunk['state'].replace(' ', '').lower()
    check = 'final/alcohol/yearly/' + str(ne_chunk['year']) + '/' + str(ne_chunk['year']) + filestate + '_' + ne_chunk['category'] + '.npy'
    try:
        os.makedirs('final/alcohol/yearly/' + str(ne_chunk['year']) + '/')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    np.save(check, ne_chunk)
    print(ne_chunk)

#SAVE HARD DRUGS AND BUSINESS
try:
    os.makedirs('final/grind/no_year/')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

for file in glob.glob('data/' + "*.npy"):
    ne_chunk = np.load(file).item()
    filestate = ne_chunk['state'].replace(' ', '').lower()
    check = 'final/grind/no_year/' + str(ne_chunk['year']) + filestate + '_' + ne_chunk['category'] + '.npy'
    file_list = list(set(ne_chunk['song']))
    ne_chunk['diff_files'] = len(file_list)

    ne_chunk['score'] = round((ne_chunk['diff_files'] / 100) * ne_chunk['hits'], 2)
    del ne_chunk['song']
    del ne_chunk['artist']
    del ne_chunk['line']
    ne_chunk['sentiment_score'] = round(ne_chunk['sentiment'] / ne_chunk['diff_files'], 2)
    if ne_chunk['sentiment'] >=  -0.1:
        ne_chunk['sentiment'] = 'Positive'
        ne_chunk['se_short'] = 'POS'
    else:
        ne_chunk['sentiment'] = 'Negative'
        ne_chunk['se_short'] = 'NEG'

    print(ne_chunk)
    if ne_chunk['category'] == 'Hard' or ne_chunk['category'] == 'Business':
        np.save(check, ne_chunk)

for file in glob.glob('final/grind/no_year/' + "*.npy"):
    ne_chunk = np.load(file).item()
    filestate = ne_chunk['state'].replace(' ', '').lower()
    check = 'final/grind/yearly/' + str(ne_chunk['year']) + '/' + str(ne_chunk['year']) + filestate + '_' + ne_chunk['category'] + '.npy'
    try:
        os.makedirs('final/grind/yearly/' + str(ne_chunk['year']) + '/')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    np.save(check, ne_chunk)
    print(ne_chunk)

#SAVE PRESCRIPTION DRUGS
try:
    os.makedirs('final/meds/no_year/')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

for file in glob.glob('data/' + "*.npy"):
    ne_chunk = np.load(file).item()
    filestate = ne_chunk['state'].replace(' ', '').lower()
    check = 'final/meds/no_year/' + str(ne_chunk['year']) + filestate + '_' + ne_chunk['category'] + '.npy'
    file_list = list(set(ne_chunk['song']))
    ne_chunk['diff_files'] = len(file_list)

    ne_chunk['score'] = round((ne_chunk['diff_files'] / 100) * ne_chunk['hits'], 2)
    del ne_chunk['song']
    del ne_chunk['artist']
    del ne_chunk['line']
    ne_chunk['sentiment_score'] = round(ne_chunk['sentiment'] / ne_chunk['diff_files'], 2)
    if ne_chunk['sentiment'] >=  -0.1:
        ne_chunk['sentiment'] = 'Positive'
        ne_chunk['se_short'] = 'POS'
    else:
        ne_chunk['sentiment'] = 'Negative'
        ne_chunk['se_short'] = 'NEG'

    print(ne_chunk)
    if ne_chunk['category'] == 'Prescription':
        np.save(check, ne_chunk)

for file in glob.glob('final/meds/no_year/' + "*.npy"):
    ne_chunk = np.load(file).item()
    filestate = ne_chunk['state'].replace(' ', '').lower()
    check = 'final/meds/yearly/' + str(ne_chunk['year']) + '/' + str(ne_chunk['year']) + filestate + '_' + ne_chunk['category'] + '.npy'
    try:
        os.makedirs('final/meds/yearly/' + str(ne_chunk['year']) + '/')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    np.save(check, ne_chunk)
    print(ne_chunk)