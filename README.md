# DSCI550-PixstoryDataAnalysis

Collaborators: Jai Agrawal, Daniil Abbruzzese, Todd Gavin, Tania Dawood

1. Project Title: Mental health online activity 

2. Project Description: 

We have compiled a large dataset containing data provided from Pixstory, as well as additional data sources of various MIME types to perform an analysis on how the COVID pandemic has affected people's usage of social media. 

3. Implementation

The additional datasets all have detailed notebooks on their use, running each notebook file should give the outputs required. The dataset directories follow Dataset[num]_[title] formats. Further, the additional columns that needed to be added are also in detailed notebooks within directories. These directories follow [letter]_[col name] formats. The ‘1_Apache_Tika_Analysis’ directory contains detailed instructions how to run the Tika similarity like we did. The “Report_Questions” directory has separate .py files which were used to make visualizations used in the report to illustrate certain findings. 

4. Additional Datasets Added:

Additional Dataset #1 - Snapchat Daily Average Users Data: 
MIME Type: test/CSV 

We selected this dataset so we are able to compare the number of snapchats DAU's to the daily posts on Pixstory to explore our research question. This dataset includes date, Snapchat's Daily Average Users and Revenue, Snapchat Stock data (Open, High, Low, Close, Adjacent Close and Volume)

In order to create this dataset, we obtained Snachat’s quarterly revenue and daily average users from Statista and its daily stock value from Yahoo Finance. Our data ranges from 2020-2022 as that is the range of data we have available for the Pixstory dataset. For the Snapchat dataset, the features we will be using for analysis are: 

Feature 1: Daily Average Users
Feature 2: Stock Price
Feature 3: Revenue

Source:  https://www.statista.com/statistics/552694/snapchat-quarterly-revenue/, https://finance.yahoo.com/quote/SNAP/, https://www.statista.com/statistics/545967/snapchat-app-dau/

Additional Dataset #2 - Daily COVID Data: 
MIME Type: application/JSON 

We decided to use a COVID API to keep track of the number of daily covid cases, deaths and vaccinations to see how these correlate to the number of Pixstory posts, Snapchat DAU's and number of likes/ views on the daily trending YouTube videos. This dataset includes the date, number of deaths, number of cases and number of vaccinations. 

    Feature 1: New daily deaths due to COVID in INdia 

        This feature was derived from taking data on cumulative deaths in India on a daily basis (source: (https://covid19api.com) and finding the difference from the prior day

    Feature 2: New daily COVID cases in India 
        
        This feature was derived from taking data on cumulative COVID cases in India on a daily basis (source: (https://covid19api.com) and finding the difference from the prior day

    Feature 3: New vaccinations against COVID in India
        
        This feature was derived from taking data on the cumulative vaccinations in India on a daily basis (source: https://github.com/owid/covid-19-data) and finding the difference from the prior day

        Note: this data set only had data available as early as 1/15/2021, which listed India as having 0 vaccinations against COVID. Because the Pixstory data set starts 1/12/2020, we decided to and this missing dates and input 0's for all vaccinations. This was justified because according to this data set India hadn't had any vaccinations until 1/16/2021.  
 
Source: https://api.covid19api.com/country/india?from=2020-01-01T00:0

Additional Dataset #3 - YouTube Daily Trending Videos:
MIME Type: Video/ MP4

Similar to the Snapchat DAU dataset, we wanted to see if there was any correlation between the number of likes and views to Pixstory posts and COVID cases. This dataset includes data on video ID, title	published at, channel ID, channel title, category ID trending date, tags, view count, likes, dislikes and comment count

This is a dataset of the top trending videos on YouTube on any particular day. The MIME Type of this dataset is Video/ MP4. The data ranges from 2020 - 2022 and the features of this include: 

Feature #1: highest trending video name, 
Feature #2: highest trending video channel, 
Feature #3: highest trending video category, 
Feature #4: highest trending video views,  
Feature #5: highest trending video likes 

Source: https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset?select=US_youtube_trending_data.csv

Sports Datasets: 
https://www.topendsports.com/events/calendar-{year}

Film Festivals: 
https://www.film-fest-report.com/home/film-festivals-2022

https://www.screendaily.com/news/2021-film-festivals-and-markets-latest-dates-postponements-and-cancellations/5155284.article

https://www.filmfestivaldatabase.com

Hate Speech Dataset: 
https://www.adl.org/resources/hate-symbols/search?keywords=&sort_by=title&page=

Sarcasm Dataset: 
https://nlds.soe.ucsc.edu/sarcasm1

Note: all datasets were combined using the date column. 
