# imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../final_dataset.tsv", sep='\t')

# define a function to count the number of sports events
def count_sports_events(s):
    try:
        return len(s.split(', '))
    except:
        return 0

# apply the function to each row of the dataframe and store the result in a new column
df['Number of Sports Events'] = df['Sports Events'].apply(count_sports_events)

sports_events_counts = df['Number of Sports Events'].value_counts()

more_sports_events = df[df['Number of Sports Events'] > 2]
sports_df = more_sports_events[more_sports_events['Interest'].str.contains('sports')]
non_sports_df = more_sports_events[~more_sports_events['Interest'].str.contains('sports')]


more_sports_posters = sports_df['User ID'].value_counts()
top_sports_posters = more_sports_posters.head(5)

more_non_sports_posters = non_sports_df['User ID'].value_counts()
top_non_sports_posters = more_non_sports_posters.head(5)


# create a horizontal bar chart of the top topics
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(top_sports_posters.index, top_sports_posters.values, color="b")

# add labels and title
ax.set_xlabel("User ID")
ax.set_ylabel("Num of Sports-Related Posts")
ax.set_title("Top Sports Posters")
fig.savefig("visualisations/top_sports_posters.png", bbox_inches="tight")

# create a horizontal bar chart of the top topics
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(top_non_sports_posters.index, top_non_sports_posters.values, color="b")

# add labels and title
ax.set_xlabel("User ID")
ax.set_ylabel("Num of Non-Sports-Related Posts")
ax.set_title("Top Non-Sports Posters")
fig.savefig("visualisations/top_non_sports_posters.png", bbox_inches="tight")

