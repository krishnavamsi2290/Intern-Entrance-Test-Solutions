#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df_links= pd.read_csv(r"C:\Users\Naidu krishna vamsi\Downloads\movie_data\links.csv")
df_movies = pd.read_csv(r"C:\Users\Naidu krishna vamsi\Downloads\movie_data\movies.csv")
df_rating = pd.read_csv(r"C:\Users\Naidu krishna vamsi\Downloads\movie_data\ratings.csv")
df_tags= pd.read_csv(r"C:\Users\Naidu krishna vamsi\Downloads\movie_data\tags.csv")


# In[2]:


df_link=pd.read_csv("links.csv")


# ## What is the shape of "movies.csv"?
# 

# In[3]:


df_link.shape


# In[4]:


df_movies = pd.read_csv("movies.csv")


# ## What is the shape of "movies.csv"?
# 

# In[5]:


df_movies.shape


# In[6]:


df_ratings= pd.read_csv("ratings.csv")


# ## What is the shape of "ratings.csv"?

# In[7]:


df_ratings.shape


# In[8]:


df_tags=pd.read_csv("tags.csv")


# In[9]:


df_tags.shape


# In[ ]:





# In[ ]:





# In[12]:


df_ratings.head()


# In[13]:


df_link.head()


# ## How many unique "userId" are available in "ratings.csv"?

# In[14]:


df_ratings['userId'].nunique()


# In[15]:


df_movies.columns


# In[16]:


df_ratings.columns


# In[17]:


df_ratings['rating'].unique()


# In[18]:


merged_movie_rating = pd.merge(df_movies, df_ratings, on='movieId')


# ## What is the shape of "ratings.csv"?
# 

# In[19]:


merged_movie_rating.shape


# In[20]:


merged_movie_rating.head()


# ## Which movie has recieved maximum number of user ratings?

# In[21]:


group= merged_movie_rating.groupby('title')['userId'].count()


# In[22]:


max_rated_movie = group.idxmax()


# In[23]:


max_rated_movie


# In[24]:


print(merged_movie_rating[merged_movie_rating['movieId'] == max_rated_movie]['title'].unique())


# In[25]:


merged_movie_rating[merged_movie_rating['movieId'] == max_rated_movie]['title']


# In[ ]:





# In[27]:


grp = merged_movie_rating.groupby('title')['userId']


# In[28]:


grp.get_group('Forrest Gump (1994)').count()


# In[29]:


grp.get_group('Black Butler: Book of the Atlantic (2017)').count()


# In[30]:


merged_movie_rating[merged_movie_rating['title'] == "Black Butler: Book of the Atlantic (2017)"]


# In[31]:


merged_movie_rating.head()


# In[32]:


df_tags.columns


# In[33]:


df_movies.columns


# In[34]:


merged_movie_tags = pd.merge(df_movies,df_tags,on = "movieId")


# In[35]:


merged_movie_tags.head()


# In[36]:


merged_movie_tags.shape


# ## Select all the correct tags submitted by users to "Matrix, The (1999)" movie?

# In[37]:


merged_movie_tags[merged_movie_tags['title']=="Matrix, The (1999)"]['tag'].unique()


# In[39]:


merged_movie_rating['title'].value_counts()


# In[40]:


a=merged_movie_rating[merged_movie_rating['userId'].duplicated()]


# In[41]:


a['title'].value_counts()


# In[42]:


merged_movie_tags.head()


# In[43]:


merged_movie_rating.head()


# In[44]:


df_link[df_link['tmdbId'].isnull()]


# In[45]:


df_movies.isnull().sum()


# In[46]:


df_ratings.isnull().sum()


# In[47]:


df_tags.isnull().sum()


# In[48]:


merged_movie_rating.columns


# In[49]:


merged_movie_rating.head()


# ## What is the average user rating for movie named "Terminator 2: Judgment Day (1991)"?

# In[50]:


merged_movie_rating[merged_movie_rating['title']=="Terminator 2: Judgment Day (1991)"]['rating'].mean()


# In[51]:


merged_movie_rating.shape


# In[52]:


dist=merged_movie_rating[merged_movie_rating['title']=='Fight Club (1999)']['rating'].tolist()


# In[53]:


import matplotlib.pyplot as plt


# ## How does the data distribution of user ratings for "Fight Club (1999)" movie looks like?

# In[54]:


plt.hist(dist, bins=10)
plt.title('Distribution of User Ratings for Fight Club (1999)')
plt.xlabel('Rating')
plt.ylabel('Frequency')


# In[55]:


# Summary stats
print(f"Mean rating: {merged_movie_rating['rating'].mean()}")
print(f"Median rating: {merged_movie_rating['rating'].median()}")
print(f"Mode rating: {merged_movie_rating['rating'].mode()[0]}") 
print(f"Standard deviation: {merged_movie_rating['rating'].std()}")


# In[56]:


a=merged_movie_rating[merged_movie_rating['title']=='Fight Club (1999)']


# In[57]:


a['rating'].mean()


# In[58]:


ratings_group = merged_movie_rating.groupby('movieId')['rating'].agg(['count','mean'])


# In[59]:


ratings_group


# In[60]:


ratings_group = ratings_group[ratings_group['count'] > 50]


# In[61]:


ratings_group


# In[62]:


movie_data = merged_movie_rating.merge(ratings_group, left_on='movieId', right_index=True)


# In[63]:


movie_data


# In[64]:


movie_data = movie_data[movie_data['count'] > 50]


# In[65]:


movie_data


# In[66]:


movie_data['mean'].max()


# In[ ]:





# In[67]:


df_movies.head()


# In[68]:


movies_data= pd.merge(df_movies,ratings_group,left_on="movieId",right_index=True)


# In[69]:


movies_data.shape


# In[70]:


movies_data.head()


# In[71]:


movies_data['mean'].max()


# In[72]:


movies_data[movies_data['mean']=='4.429022']


# ## Which movie is the most popular based on  average user ratings?
# 

# In[73]:


movies_data.sort_values('mean', ascending=False).head(1)


# In[74]:


top_movies = movies_data.sort_values('count', ascending=False).head(5)


# ## Select all the correct options which comes under top 5 popular movies based on number of user ratings.

# In[75]:


top_movies


# In[77]:


Sci = movies_data[movies_data['genres'].str.contains("Sci-Fi")]


# In[78]:


Sci = Sci.sort_values('count',ascending=False)


# In[79]:


Sci


# In[80]:


S_title = Sci.iloc[2]


# ## Which Sci-Fi movie is "third most popular" based on the number of user ratings?

# In[81]:


S_title['title']


# In[82]:


df_link.head()


# In[83]:


link_data = pd.merge(movies_data,df_link,on="movieId")


# In[84]:


link_data


# In[85]:


link_data[link_data['movieId']==47]


# In[86]:


link_data['imdbId'].max()


# In[87]:


df_ratings


# In[88]:


df_link


# In[89]:


df_tags


# In[90]:


movies_data


# In[91]:


df_link


# In[92]:


import requests


# In[93]:


import numpy as np
from bs4 import BeautifulSoup


# In[94]:


URL= "https://www.imdb.com/title/tt0113497/ratings/?ref_=tt_ov_rt"


# In[95]:


request_header={'content-type': 'text/plain;charset=UTF-8',
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                'Accept-Encoding': 'gzip, deflate, br'}


# In[96]:


response= requests.get(URL,headers=request_header)


# In[97]:


print(response.status_code)


# In[98]:


response.headers


# In[99]:


html_code=response.text


# In[100]:


html_code


# In[101]:


type(html_code)


# In[102]:


soup=BeautifulSoup(html_code)


# In[103]:


soup


# In[ ]:





# In[ ]:





# In[104]:


print(soup.prettify())


# In[ ]:


sc-5931bdee-1 gVydpF


# In[105]:


rating= soup.find('span',attrs={'class':'sc-5931bdee-1 gVydpF'})


# In[106]:


rating.text


# In[ ]:


df_link


# In[107]:


URLS = []
for i in link_data['imdbId']:
    URL = f"https://www.imdb.com/title/tt0{i}/ratings/?ref_=tt_ov_rt"
    URLS.append(URL)


# In[108]:


for i in URLS:
    url = i
    print(url)


# In[109]:


import numpy as np


# In[110]:


from tqdm import tqdm


# In[117]:


ratings_ = []
for i in tqdm(URLS):
    URL = i
    request_header={'content-type': 'text/plain;charset=UTF-8',
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                'Accept-Encoding': 'gzip, deflate, br'}
    response= requests.get(URL,headers=request_header)
    html_code=response.text
    soup = BeautifulSoup(html_code)
    containers = soup.find_all('div',attrs={'class':'sc-f056af46-3 dzYxjh'})
    for container in containers:
        rating= container.find('span',attrs={'class':'sc-5931bdee-1 gVydpF'})
        if rating is None:
            ratings_.append(np.NaN)
        else:
            ratings_.append(rating.text)  
            
tqdm.pandas()
#df['ratings'] = df['URL'].progress_apply(scrape_ratings)


# In[129]:


df_ratings = pd.Series(ratings_)


# In[130]:


df_rating = df_ratings.dropna()


# In[132]:


len(df_rating)


# In[133]:


Ratings = pd.read_csv("IDMD_rating.csv")


# In[138]:


Ratings.columns=["imdb_rating"]


# In[139]:


Ratings


# In[142]:


final_data =pd.concat([link_data,Ratings],axis=1)


# In[143]:


final_data


# In[145]:


final_data['imdb_rating'].value_counts()


# In[147]:


final_data[final_data['imdb_rating'].isnull()]


# ## Mention the movieId of the movie which has the highest IMDB rating.
# 

# In[149]:


final_data[final_data['movieId']==318]


# In[150]:


Sci = final_data[final_data['genres'].str.contains("Sci-Fi")]


# In[153]:


Sci.sort_values('imdb_rating',ascending=False)


# In[154]:


Sci[Sci['movieId']==79132]


# In[155]:


import requests
import numpy as np
from bs4 import BeautifulSoup


# In[162]:


def scrapper(imdbId):
    id = str(int(imdbId))
    n_zeroes = 7 - len(id)
    new_id = "0"*n_zeroes + id
    URL = f"https://www.imdb.com/title/tt{new_id}/"
    request_header = {'Content-Type': 'text/html; charset=UTF-8', 
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0', 
                      'Accept-Encoding': 'gzip, deflate, br'}
    response = requests.get(URL, headers=request_header)
    soup = BeautifulSoup(response.text)
    imdb_rating = soup.find('span', attrs={'class' : 'sc-5931bdee-1 gVydpF'})
    return imdb_rating.text if imdb_rating else np.nan


# In[163]:


scrapper(list1)


# In[160]:


list1=[]
for i in link_data['imdbId']:
    list1.append(i)


# In[168]:


import requests
from bs4 import BeautifulSoup

def scrapper(imdbId_list):
  
    ratings = []
  
    for imdbId in imdbId_list:
  
        id = str(int(imdbId))
        n_zeroes = 7 - len(id)
        new_id = "0"*n_zeroes + id
        url = f"https://www.imdb.com/title/tt{new_id}/"
    
        request_header = {'Content-Type': 'text/html; charset=UTF-8',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0', 
                      'Accept-Encoding': 'gzip, deflate, br'}
                      
        response = requests.get(url, headers=request_header)  
        soup = BeautifulSoup(response.text)
    
        rating = soup.find('span', attrs={'class': 'sc-5931bdee-1 gVydpF'})
    
        if rating:
            ratings.append(float(rating.text)) 
        else:
            ratings.append(np.nan)
      
    return ratings


# In[ ]:


scrapper(list1)


# In[ ]:


ratings_ = []
for i in tqdm(URLS):
    URL = i
    request_header={'content-type': 'text/plain;charset=UTF-8',
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                'Accept-Encoding': 'gzip, deflate, br'}
    response= requests.get(URL,headers=request_header)
    html_code=response.text
    soup = BeautifulSoup(html_code)
    containers = soup.find_all('div',attrs={'class':'sc-f056af46-3 dzYxjh'})
    for container in containers:
        rating= container.find('span',attrs={'class':'sc-5931bdee-1 gVydpF'})
        if rating is None:
            ratings_.append(np.NaN)
        else:
            ratings_.append(rating.text)  

