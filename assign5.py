import pandas as pd

ds1=pd.read_csv('movie_metadata.csv',encoding="ISO-8859-1")

ds1.head()

ds1.shape

ds1.info()

ds1.imdb_score.describe()

ds1['movie_title']   

ds1['duration'][:10] 
 
ds1[['budget','gross']] 

ds1[ds1['duration'] > 120] 


ds1.country=ds1.country.fillna('') 
ds1.duration=ds1.duration.fillna(ds1.duration.mean()) 
ds1.dropna() 
ds1.dropna(how='all') 
ds1.dropna(thresh=5) 
ds1.dropna(subset=['title_year'])  

ds1.dropna(axis=1, how='all') 
ds1.dropna(axis=1, how='any')


ds1=pd.read_csv('movie_metadata.csv',dtype={'duration':int})
ds1=pd.read_csv('movie_metadata.csv',dtype={'title_year':str})

ds1['movie_title'].str.upper()

ds1['movie_title'].str.strip()#to remove the trailing spaces


#reverse column

ds2=ds1.rename(columns={'title_year':'release_date','movie_facebook_likes':'facebook_likes'})

#save your result

