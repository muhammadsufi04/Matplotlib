import matplotlib.pyplot as plt
import pandas as pd
df= pd.read_csv("netflix_titles.csv")

df=df.dropna(subset=['type','release_year','rating','country','duration'])

type_counts=df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index,type_counts.values,color=['skyblue',"orange"])
plt.title("------NUMBER OF MOVIES AND TV SHOWS ON NETFLIX---")
plt.xlabel("type")
plt.ylabel("count")
plt.tight_layout()
plt.show()

rating_count=df["rating"].value_counts()

plt.figure(figsize=(8,6))
plt.pie(rating_count,labels=rating_count.index,autopct='%1.1f%%',startangle=90)
plt.title("------PERCENTAGE OF COUNT RATING---")
plt.tight_layout()
plt.show()

movie_df=df[df['type']=='Movie'].copy()
movie_df["duration_int"]=movie_df['duration'].str.replace('min',"").astype(int)
plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'],bins=30,color='purple',edgecolor='black')
plt.title("------DISTRIBUTION OF MOVIES DURATION---")
plt.xlabel("DURATION(minutes)")
plt.ylabel("NUMBER OF MOVIES")
plt.tight_layout()
plt.show()


release_count=df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_count.index,release_count.values,color='red')
plt.title("------RELEASE YEAR vs NUMBER OF SHOWS---")
plt.xlabel("RELEASE LABEL")
plt.ylabel("NUMBER OF SHOW")
plt.tight_layout()
plt.show()


country_count=df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_count.index,country_count.values,color='blue')
plt.title("------top 10 country by number of show---")
plt.xlabel("COUNTRY")
plt.ylabel("NUMBER OF SHOW")
plt.tight_layout()
plt.show()
   
content_by_year=df.groupby(['release_year','type']).size().unstack().fillna(0)
fig,ax=plt.subplots(1,2, figsize=(12,5))

ax[0].plot(content_by_year.index,content_by_year["Movie"],color='blue')
ax[0].set_title("movies RELEASE PER YEAR")
ax[0].set_xlabel('year')
ax[0].set_ylabel('number of movies')


ax[0].plot(content_by_year.index,content_by_year["TV Show"],color='orange')
ax[0].set_title("tv show RELEASE PER YEAR")
ax[0].set_xlabel('year')
ax[0].set_ylabel('number of tv show')



fig.suptitle("COMPARISON OF MOVIES AND TV SHOWS")
plt.show()