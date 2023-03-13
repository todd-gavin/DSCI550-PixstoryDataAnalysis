# imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../final_dataset.tsv", sep='\t')

df_hate_speech = df[df["Hate Speech Flag"] == 1.0]

gender_data = df_hate_speech["Gender"]
gender_counts = gender_data.value_counts()

age_data = df_hate_speech["Age"]
age_counts = age_data.value_counts()
age_average = age_data.mean()
age_range = (age_data.min(), age_data.max())

# create a pie chart of the gender counts
fig, ax = plt.subplots()
ax.pie(gender_data.value_counts(), labels=gender_data.value_counts().index, autopct="%1.1f%%")
ax.set_title(f"Gender Distribution for Hate Speech")

# show the plot
fig.savefig(f"visualisations/Gender_Dist_HateSpeech.png", bbox_inches="tight")

# create boxplot
fig, ax = plt.subplots()
sns.boxplot(x=age_data)
ax.set_title(f"Age Distribution for Hate Speech")
fig.savefig(f"visualisations/Age_Dist_HateSpeech.png", bbox_inches="tight")
