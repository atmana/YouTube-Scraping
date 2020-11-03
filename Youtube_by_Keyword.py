from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import pandas as pd
import numpy as np
import pprint 
import matplotlib.pyplot as plt
import datetime

DEVELOPER_KEY = "xxxx"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

keywords = ["telkomsel murah","telkomsel gratis"]

TanggalMulai=(datetime.datetime.now()-datetime.timedelta(weeks=4)).strftime('%Y-%m-%d')
HariIni=(datetime.datetime.now()).strftime('%Y-%m-%d')
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

max_results=10
order="viewCount"
publishedAfter=TanggalMulai+"T00:00:00Z"
#publishedAfter="2019-11-22T00:00:00Z"
token=None
location=None
location_radius=None

title = []
channelId = []
channelTitle = []
categoryId = []
videoId = []
pubDate = [] 
viewCount = []
likeCount = []
dislikeCount = []
commentCount = []
favoriteCount = []
category = []
tags = []
videos = []
keyword = []
url = []

for q in keywords:
    search_response = youtube.search().list(
    q=q,
    type="video",
    pageToken=token,
    order = order,
    part="id,snippet",  
    maxResults=max_results,
    location=location,
    publishedAfter=publishedAfter,
    locationRadius=location_radius).execute()


    for search_result in search_response.get("items", []):

        keyword.append(q)

        if search_result["id"]["kind"] == "youtube#video":

            title.append(search_result['snippet']['title']) 

            videoId.append(search_result['id']['videoId'])

            response = youtube.videos().list(
                part='statistics, snippet',
                id=search_result['id']['videoId']).execute()

            
            channelId.append(response['items'][0]['snippet']['channelId'])
            channelTitle.append(response['items'][0]['snippet']['channelTitle'])
            pubDate.append(response['items'][0]['snippet']['publishedAt'])
            categoryId.append(response['items'][0]['snippet']['categoryId'])
            favoriteCount.append(response['items'][0]['statistics']['favoriteCount'])
            viewCount.append(response['items'][0]['statistics']['viewCount'])
            #url.append("https://www.youtube.com/watch?v="+videoId[0])
            url.append("https://www.youtube.com/watch?v="+search_result['id']['videoId'])
            try:
                likeCount.append(response['items'][0]['statistics']['likeCount'])
            except:
                likeCount.append("NaN")

            try:
                dislikeCount.append(response['items'][0]['statistics']['dislikeCount'])     
            except:
                dislikeCount.append("NaN")

            if 'commentCount' in response['items'][0]['statistics'].keys():
                commentCount.append(response['items'][0]['statistics']['commentCount'])
            else:
                commentCount.append(0)

            if 'tags' in response['items'][0]['snippet'].keys():
                tags.append(response['items'][0]['snippet']['tags'])
            else:
                tags.append("No Tags")  

youtube_dict = {'pubDate': pubDate,'tags': tags,'channelId': channelId,'channelTitle': channelTitle,'categoryId':categoryId,'title':title,'videoId':videoId,'viewCount':viewCount,'likeCount':likeCount,'dislikeCount':dislikeCount,'favoriteCount':favoriteCount, 'commentCount':commentCount, 'keyword':keyword, 'url':url}
df = pd.DataFrame(youtube_dict)
df.sort_values(by='viewCount',ascending=False)

import sentimentYouTube as SYT
import comment_extract as CE
import pandas as pd

df['positive']=''
df['negative']=''

for i in df['videoId']:
    print(i)
    comments = CE.commentExtract(i,100)
    pos, neg = SYT.sentiment(comments)
    df.loc[df['videoId']==i,['positive']] = pos
    df.loc[df['videoId']==i,['negative']] = neg
    
df = df[(df['positive']!='') | (df['negative']!='')]
df.loc[:,'positive'] =df['positive'].astype(int)
df.loc[:,'negative'] =df['negative'].astype(int)

df.drop_duplicates(['videoId'])
df['pubDate'] = pd.to_datetime(df.pubDate)
df['publishedDate'] = df['pubDate'].dt.strftime('%d/%m/%Y')
df1 = df[['keyword','publishedDate','title','viewCount','channelTitle','commentCount','likeCount','dislikeCount','tags','favoriteCount','videoId','channelId','categoryId','url','positive','negative']]
df1.columns = ['keyword','publishedDate','Title','viewCount','channelTitle','commentCount','likeCount','dislikeCount','tags','favoriteCount','videoId','channelId','categoryId','URL','positive','negative']

export_csv = df1.to_csv (r'/home/YoutubeAPI/Result/youtube_search_keyword_{}.csv'.format(str(HariIni)), index = None, header=True) 
