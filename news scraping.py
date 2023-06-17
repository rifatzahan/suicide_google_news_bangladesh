import os

os.chdir('My_Directory')


import random
import time
from GoogleNews import GoogleNews
import pandas as pd


#### Extract google news ####

# set language and region
googlenews = GoogleNews()
googlenews = GoogleNews(lang="en", region="BD")

# set timeline of the news, unicode and keyword
googlenews.set_time_range('01/01/2020','06/14/2023')
googlenews.set_encode('utf-8')
googlenews.search('Suicide Bangladesh')

# set number of pages the news should be extracted from, sleep time, create dataframe to keep the results
for i in range(25):
    googlenews.getpage(i)
    result = googlenews.result()
    resultDF = pd.DataFrame(result)
    time.sleep(random.randint(2,30))

resultDFCSV = resultDF.to_csv('suicide news.csv')

# Remove duplicated rows based on multiple columns
df = df.drop_duplicates(subset=['title', 'date'])

#### Get full description of the news ####
import newspaper
import json


for index, row in df.iterrows():
    url = row['link']
    try:
        article = newspaper.Article(url=url, language='en')
        article.download()
        article.parse()
        article_data = {
        "title": str(article.title),
        "text": str(article.text),
        "authors": article.authors,
        "published_date": str(article.publish_date),
        "keywords": article.keywords,
        "summary": str(article.summary)
        }
        df.at[index, 'Summary'] = article_data["text"]
    except Exception as e:
        print(f"Error occurred while processing URL: {url}\n{str(e)}")


dfToCSV = df.to_csv('df.csv')
