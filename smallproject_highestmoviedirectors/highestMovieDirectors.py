from urllib.request import urlretrieve
from collections import namedtuple, defaultdict, Counter, deque
import os
import csv

movies_url = 'https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv'
movies_data = os.getcwd() + '\movie1.csv'
urlretrieve(movies_url, movies_data)


directors = namedtuple('directors', 'name year movie')


def gethighestratedirector(data=movies_data):
    imdbScore = defaultdict(list)
    directorRate = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                imdb = float(line['imdb_score'])
                year = int(line['title_year'])
            except ValueError:
                continue
            i = directors(name=director, year=year, movie=movie)
            directorRate[director].append(imdb)
            imdbScore[imdb].append(i)
    return directorRate

def average(arr):
    return sum(arr) / len(arr)

directorRate = gethighestratedirector()
cnt = Counter()
for i, j in directorRate.items():
    cnt[i] += average(j)
print(cnt.most_common(10))
