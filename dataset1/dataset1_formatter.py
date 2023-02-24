'''
This Python file is used to format the raw datasets used to create our dataset 1, which illustrates the daily active
users (DAUs) of Facebook, Twitter and Snapchat
'''

import pandas as pd

# function to format the datasets
def format_dataset(df, name):
    df = df.drop(index=range(4))
    df = df.drop(columns=df.columns[0])
    df.columns = ["Quarters", f"{name}_DAUs"]
    df = df.iloc[-12:, :].reset_index(drop=True)
    return df


# raw dataset filenames
path = "raw_files"
fb_data_filename = "statistic_id346167_facebook_-number-of-daily-active-users-worldwide-2011-2022.xlsx"
twitter_data_filename = "statistic_id970911_twitter_-number-of-monetizable-daily-active-us-users-2017-2022.xlsx"
snap_data_filename = "statistic_id545967_daily-active-users-of-snapchat-2014-2022.xlsx"
sheet_name = "Data"

# lists
filenames = [fb_data_filename, twitter_data_filename, snap_data_filename]
names = ["Facebook", "Twitter", "Snap"]
new_datasets = list()

# looping through each dataset and formatting using our function
for i in range(len(filenames)):
    file_path = path + "/" + filenames[i]
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    dataset = format_dataset(df, names[i])
    new_datasets.append(dataset)

# merging newly formatted datasets
merged_df = pd.merge(new_datasets[0], new_datasets[1], on='Quarters')
merged_df = pd.merge(merged_df, new_datasets[2], on='Quarters')

# splitting quarter and year
merged_df[['Quarter', 'Year']] = merged_df['Quarters'].str.split(" ", expand=True)
merged_df['Year'] = "20" + merged_df['Year'].str.replace("'", "")
merged_df = merged_df.drop(columns="Quarters")

merged_df.to_csv("dataset1.csv", index=False)