# -*- coding: utf-8 -*-
"""
ProductHunt.com JSON Results

Use this script to download ProductHunt.com Tech category
results and export attributes to CSV

Created on Sat Jul 16 2016
@author: DWolf
"""

import requests
import pandas

# ENTER THE NUMBER OF DAYS THAT YOU WANT TO SEARCH
# E.g. Entering 5 will return all results from 5 days ago up through yesterday
days = 50

posts = pandas.DataFrame()
for i in range(1, days+1):
    
    URL = 'https://posts.producthunt.com/posts/currentUser?page=' + str(i)
    request = requests.get(URL)
    data = request.json()
    df = pandas.DataFrame.from_dict(data['posts'])
    # Filter to tech only (Remove this line if you want all categories)
    df = df.loc[df['category_slug'] == 'tech']
    # Append the results from this day to the other days
    posts = posts.append(df)

# Output to CSV
posts.to_csv('producthunt-tech.csv', encoding='utf-8')

