# importing the module
import imdb
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pylab as plt
from  matplotlib.colors import LinearSegmentedColormap
import sys

plt.style.use("seaborn")
data = []
max_number_episodes = 0;

# creating instance of IMDb
ia = imdb.IMDb() 

code = str(sys.argv[1])
print("Code: " + code)

# Getting series data
series = ia.get_movie(code)
 
# Adding new info set
ia.update(series, 'episodes')
 
# Getting episodes of the series
episodes = series.data['episodes']
 
# Printing the object name
print(series)

print("=========")

for i in episodes.keys():
    
    print(" ")
    # printing season number
    print("Season " + str(i))
     
    episodes_rating = []

    max_number_episodes = max(max_number_episodes, len(episodes[i]))
    print("Number of episodes in this season: " + str(len(episodes[i])))

    # Traversing season i
    for j in episodes[i]:

        # Getting title of episode
        title = episodes[i][j]['title']

        if episodes[i][j].get('rating') is None:
        	episodes_rating.append(0)
        else:
            # Getting rating of episode
            ep_rating = episodes[i][j]['rating']
            episodes_rating.append(round(ep_rating,1))

            # Print the title
            print(title + " - " + str(ep_rating))

    if len(episodes_rating) < max_number_episodes:
        for x in range(len(episodes_rating), max_number_episodes):
        	episodes_rating.append(0)

    data.append(episodes_rating)
    
c = ["darkred","red","lightcoral", "palegreen","green","darkgreen"]
v = [0,.15,.4,0.6,.9,1.]
l = list(zip(v,c))
cmap_color = LinearSegmentedColormap.from_list('rg',l, N=256)

xlabels = range(1, len(episodes.keys()) + 1)
ylabels = range(1, max_number_episodes +1)

# Plot the heatmap
plt.figure(figsize=(max_number_episodes,11))
df = pd.DataFrame(data, index = xlabels, columns = ylabels)
heat_map = sns.heatmap(df, cmap=cmap_color, linewidth = 1 , annot = True, mask=(df==0), vmin = 0, vmax = 10, xticklabels=1, yticklabels=1)
plt.title(str(series) + " - Ratings by IMDb" )
plt.xlabel('Episodes')
plt.ylabel('Seasons')
plt.savefig(str(series).lower().replace(" ","")+'_imdbratings.png', bbox_inches='tight')
plt.show()