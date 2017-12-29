import numpy as np
import glob
import csv
import os
import errno

#create csv files for every data set

#SAVE EVERYTHING
try:
    os.makedirs('csv/complete/yearly')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
for year in range (1980, 2018):
    path = 'final/complete/yearly/' + str(year) + '/'
    try:
        os.makedirs('csv/complete/yearly/')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    with open('csv/complete/yearly/' + str(year) + 'COMPLETE.csv', 'w', newline='') as csvfile:
        fieldnames = ['year', 'state', 'category', 'sub_cat', 'score', 'sentiment', 'sentiment_score', 'se_short',
                      'hits', 'diff_files', 'latitude', 'longitude', 'alt_latitude', 'alt_longitude']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        #loop through all items in output/
        for file in glob.glob(path + "*.npy"):
            ne_chunk = np.load(file).item()
            print(ne_chunk)

            writer.writerow({'year': ne_chunk['year'], 'state': ne_chunk['state'], 'category': ne_chunk['category'],
                             'sub_cat': ne_chunk['sub_cat'], 'score': ne_chunk['score'],
                             'sentiment_score': ne_chunk['sentiment_score'], 'sentiment': ne_chunk['sentiment'],
                             'se_short': ne_chunk['se_short'], 'hits': ne_chunk['hits'],
                             'diff_files': ne_chunk['diff_files'], 'latitude': ne_chunk['latitude'],
                             'longitude': ne_chunk['longitude'], 'alt_latitude': ne_chunk['alt_latitude'],
                             'alt_longitude': ne_chunk['alt_longitude']})

path = 'final/complete/no_year/'
try:
    os.makedirs('csv/complete/full/')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
with open('csv/complete/full/FULLCOMPLETE.csv', 'w', newline='') as csvfile:
    fieldnames = ['year', 'state', 'category', 'sub_cat', 'score', 'sentiment', 'sentiment_score', 'se_short', 'hits',
                  'diff_files', 'latitude', 'longitude', 'alt_latitude', 'alt_longitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    #loop through all items in output/
    for file in glob.glob(path + "*.npy"):
        ne_chunk = np.load(file).item()

        writer.writerow({'year': ne_chunk['year'], 'state': ne_chunk['state'], 'category': ne_chunk['category'],
                         'sub_cat': ne_chunk['sub_cat'], 'score': ne_chunk['score'],
                         'sentiment_score': ne_chunk['sentiment_score'], 'sentiment': ne_chunk['sentiment'],
                         'se_short': ne_chunk['se_short'], 'hits': ne_chunk['hits'],
                         'diff_files': ne_chunk['diff_files'], 'latitude': ne_chunk['latitude'],
                         'longitude': ne_chunk['longitude'], 'alt_latitude': ne_chunk['alt_latitude'],
                         'alt_longitude': ne_chunk['alt_longitude']})


#SAVE ESSENTIALS
try:
    os.makedirs('csv/simple/yearly')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
for year in range (1980, 2018):
    path = 'final/complete/yearly/' + str(year) + '/'
    try:
        os.makedirs('csv/simple/yearly/')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    with open('csv/simple/yearly/' + str(year) + 'SIMPLE.csv', 'w', newline='') as csvfile:
        fieldnames = ['year', 'state', 'category', 'score', 'sentiment', 'se_short',
                      'hits', 'diff_files', 'latitude', 'longitude']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        #loop through all items in output/
        for file in glob.glob(path + "*.npy"):
            ne_chunk = np.load(file).item()
            print(ne_chunk)

            writer.writerow({'year': ne_chunk['year'], 'state': ne_chunk['state'], 'category': ne_chunk['category'],
                             'score': ne_chunk['score'], 'sentiment': ne_chunk['sentiment_score'], 'se_short': ne_chunk['se_short'], 'hits': ne_chunk['hits'],
                             'diff_files': ne_chunk['diff_files'], 'latitude': ne_chunk['alt_latitude'],
                             'longitude': ne_chunk['alt_longitude']})

path = 'final/complete/no_year/'
try:
    os.makedirs('csv/simple/full/')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
with open('csv/simple/full/FULLSIMPLE.csv', 'w', newline='') as csvfile:
    fieldnames = ['year', 'state', 'category', 'score', 'sentiment', 'se_short',
                  'hits', 'diff_files', 'latitude', 'longitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    #loop through all items in output/
    for file in glob.glob(path + "*.npy"):
        ne_chunk = np.load(file).item()

        writer.writerow({'year': ne_chunk['year'], 'state': ne_chunk['state'], 'category': ne_chunk['category'],
                         'score': ne_chunk['score'], 'sentiment': ne_chunk['sentiment_score'], 'se_short': ne_chunk['se_short'], 'hits': ne_chunk['hits'],
                         'diff_files': ne_chunk['diff_files'],'latitude': ne_chunk['alt_latitude'],
                         'longitude': ne_chunk['alt_longitude']})


#SAVE ALCOHOL
try:
    os.makedirs('csv/alcohol/yearly')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
for year in range (1980, 2018):
    path = 'final/alcohol/yearly/' + str(year) + '/'
    try:
        os.makedirs('csv/alcohol/yearly/')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    with open('csv/alcohol/yearly/' + str(year) + 'ALCOHOL.csv', 'w', newline='') as csvfile:
        fieldnames = ['year', 'state', 'category', 'score', 'sentiment', 'se_short',
                      'hits', 'diff_files', 'latitude', 'longitude']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        #loop through all items in output/
        for file in glob.glob(path + "*.npy"):
            ne_chunk = np.load(file).item()
            print(ne_chunk)

            writer.writerow({'year': ne_chunk['year'], 'state': ne_chunk['state'], 'category': ne_chunk['sub_cat'],
                             'score': ne_chunk['score'], 'sentiment': ne_chunk['sentiment_score'], 'se_short': ne_chunk['se_short'], 'hits': ne_chunk['hits'],
                             'diff_files': ne_chunk['diff_files'], 'latitude': ne_chunk['alt_latitude'],
                             'longitude': ne_chunk['alt_longitude']})

path = 'final/alcohol/no_year/'
try:
    os.makedirs('csv/alcohol/full/')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
with open('csv/alcohol/full/FULLALCOHOL.csv', 'w', newline='') as csvfile:
    fieldnames = ['year', 'state', 'category', 'score', 'sentiment', 'se_short', 'hits',
                  'diff_files', 'latitude', 'longitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    #loop through all items in output/
    for file in glob.glob(path + "*.npy"):
        ne_chunk = np.load(file).item()

        writer.writerow({'year': ne_chunk['year'], 'state': ne_chunk['state'], 'category': ne_chunk['sub_cat'], 'score': ne_chunk['score'],
                         'sentiment': ne_chunk['sentiment_score'], 'se_short': ne_chunk['se_short'], 'hits': ne_chunk['hits'],
                         'diff_files': ne_chunk['diff_files'], 'latitude': ne_chunk['alt_latitude'],
                         'longitude': ne_chunk['alt_longitude']})


#SAVE HARD DRUGS AND BUSINESS
try:
    os.makedirs('csv/grind/yearly')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
for year in range (1980, 2018):
    path = 'final/grind/yearly/' + str(year) + '/'
    try:
        os.makedirs('csv/grind/yearly/')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    with open('csv/grind/yearly/' + str(year) + 'GRIND.csv', 'w', newline='') as csvfile:
        fieldnames = ['year', 'state', 'category', 'score', 'sentiment', 'se_short',
                      'hits', 'diff_files', 'latitude', 'longitude']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        #loop through all items in output/
        for file in glob.glob(path + "*.npy"):
            ne_chunk = np.load(file).item()
            print(ne_chunk)

            writer.writerow({'year': ne_chunk['year'], 'state': ne_chunk['state'], 'category': ne_chunk['sub_cat'],
                             'score': ne_chunk['score'], 'sentiment': ne_chunk['sentiment_score'], 'se_short': ne_chunk['se_short'], 'hits': ne_chunk['hits'],
                             'diff_files': ne_chunk['diff_files'], 'latitude': ne_chunk['alt_latitude'],
                             'longitude': ne_chunk['alt_longitude']})

path = 'final/grind/no_year/'
try:
    os.makedirs('csv/grind/full/')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
with open('csv/grind/full/FULLGRIND.csv', 'w', newline='') as csvfile:
    fieldnames = ['year', 'state', 'category', 'score', 'sentiment', 'se_short', 'hits',
                  'diff_files', 'latitude', 'longitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    #loop through all items in output/
    for file in glob.glob(path + "*.npy"):
        ne_chunk = np.load(file).item()

        writer.writerow({'year': ne_chunk['year'], 'state': ne_chunk['state'], 'category': ne_chunk['sub_cat'], 'score': ne_chunk['score'],
                         'sentiment': ne_chunk['sentiment_score'], 'se_short': ne_chunk['se_short'], 'hits': ne_chunk['hits'],
                         'diff_files': ne_chunk['diff_files'], 'latitude': ne_chunk['alt_latitude'],
                         'longitude': ne_chunk['alt_longitude']})


#SAVE MEDS
try:
    os.makedirs('csv/meds/yearly')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
for year in range (1980, 2018):
    path = 'final/meds/yearly/' + str(year) + '/'
    try:
        os.makedirs('csv/meds/yearly/')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    with open('csv/meds/yearly/' + str(year) + 'GRIND.csv', 'w', newline='') as csvfile:
        fieldnames = ['year', 'state', 'category', 'score', 'sentiment', 'se_short',
                      'hits', 'diff_files', 'latitude', 'longitude']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        #loop through all items in output/
        for file in glob.glob(path + "*.npy"):
            ne_chunk = np.load(file).item()
            print(ne_chunk)

            writer.writerow({'year': ne_chunk['year'], 'state': ne_chunk['state'], 'category': ne_chunk['sub_cat'],
                             'score': ne_chunk['score'], 'sentiment': ne_chunk['sentiment_score'], 'se_short': ne_chunk['se_short'], 'hits': ne_chunk['hits'],
                             'diff_files': ne_chunk['diff_files'], 'latitude': ne_chunk['alt_latitude'],
                             'longitude': ne_chunk['alt_longitude']})

path = 'final/meds/no_year/'
try:
    os.makedirs('csv/meds/full/')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
with open('csv/meds/full/FULLGRIND.csv', 'w', newline='') as csvfile:
    fieldnames = ['year', 'state', 'category', 'score', 'sentiment', 'se_short', 'hits',
                  'diff_files', 'latitude', 'longitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    #loop through all items in output/
    for file in glob.glob(path + "*.npy"):
        ne_chunk = np.load(file).item()

        writer.writerow({'year': ne_chunk['year'], 'state': ne_chunk['state'], 'category': ne_chunk['sub_cat'], 'score': ne_chunk['score'],
                         'sentiment': ne_chunk['sentiment_score'], 'se_short': ne_chunk['se_short'], 'hits': ne_chunk['hits'],
                         'diff_files': ne_chunk['diff_files'], 'latitude': ne_chunk['alt_latitude'],
                         'longitude': ne_chunk['alt_longitude']})