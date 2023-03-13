# imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../final_dataset.tsv", sep='\t')

# print(df["Account Created Date"])

# convert "Account Created Date" column to datetime format
df["Account Created Date"] = pd.to_datetime(df["Account Created Date"])
df["Hour"] = df["Account Created Date"].dt.hour.map({
    0: "12am", 1: "1am", 2: "2am", 3: "3am", 4: "4am", 5: "5am",
    6: "6am", 7: "7am", 8: "8am", 9: "9am", 10: "10am", 11: "11am",
    12: "12pm", 13: "1pm", 14: "2pm", 15: "3pm", 16: "4pm", 17: "5pm",
    18: "6pm", 19: "7pm", 20: "8pm", 21: "9pm", 22: "10pm", 23: "11pm"
})
hour_counts = df["Hour"].value_counts()


# create a horizontal bar chart of the top topics
fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(hour_counts.index, hour_counts.values, color="b")

# add labels and title
ax.set_xlabel("Count")
ax.set_ylabel("Hour")
ax.set_title("Hour Posted Counts")


fig.savefig("visualisations/hour_counts.png", bbox_inches="tight")
