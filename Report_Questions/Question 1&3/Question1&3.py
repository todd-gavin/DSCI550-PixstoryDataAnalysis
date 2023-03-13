# imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("final_dataset.tsv", sep='\t')

# split the values in the "Interest" column by commas and convert them to lists
df["Interest"] = df["Interest"].str.split(", ")

# explode the lists in the "Interest" column into separate rows
df = df.explode("Interest")

# count the occurrence of each topic within the "Interest" column
topic_counts = df["Interest"].value_counts()

# get the top 20 topics by count
top_topics = topic_counts.head(15)
top_interests = list(top_topics.index)

# create a horizontal bar chart of the top topics
fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(top_topics.index, top_topics.values, color="b")

# add labels and title
ax.set_xlabel("Count")
ax.set_ylabel("Topic")
ax.set_title("Top 15 Topics by Count")

# invert the y-axis to display topics in descending order
ax.invert_yaxis()

# display the chart
fig.savefig("visualisations/top_interests.png", bbox_inches="tight")

grouped_data = df.groupby("Interest")
# loop over the top interests
for interest in top_interests:
    print(f"Interest: {interest}")
    # find the users who have created this interest
    users = grouped_data.get_group(interest)["User ID"].unique()
    # get the gender and age data for these users
    gender_data = df[df["User ID"].isin(users)]["Gender"]
    age_data = df[df["User ID"].isin(users)]["Age"]

    # compute the summary statistics for gender and age
    gender_counts = gender_data.value_counts()
    gender_average = gender_data.value_counts(normalize=True)
    age_counts = age_data.value_counts()
    age_average = age_data.mean()
    age_range = (age_data.min(), age_data.max())

    # create a pie chart of the gender counts
    fig, ax = plt.subplots()
    ax.pie(gender_data.value_counts(), labels=gender_data.value_counts().index, autopct="%1.1f%%")
    ax.set_title(f"Gender Distribution for {interest}")
    # show the plot
    fig.savefig(f"visualisations/Gender_Dist_{interest}.png", bbox_inches="tight")

    # create boxplot
    fig, ax = plt.subplots()
    sns.boxplot(x=age_data)
    ax.set_title(f"Age Distribution for {interest}")
    fig.savefig(f"visualisations/Age_Dist_{interest}.png", bbox_inches="tight")

