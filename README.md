# DSCI550-PixstoryDataAnalysis

Collaborators: Jai Agrawal, Daniil Abbruzzese, Todd Gavin, Tania Dawood

1. Project Title: Mental health online activity 

2. Project Description: 

We have compiled a large dataset containing data provided from Pixstory, as well as additional data sources of various MIME types to perform an analysis on how the COVID pandemic has affected people's behavior online, with a focus on mental health. 

3. Additional Datasets Added:

Additional Dataset #1 - Snapchat Daily Average Users Data: test/CSV MIME type

In order to create this dataset, we obtained Snachat’s quarterly revenue and daily average users from Statista and its daily stock value from Yahoo Finance. Our data ranges from 2020-2022 as that is the range of data we have available for the Pixstory dataset. For the Snapchat dataset, the features we will be using for analysis are: 

Feature 1: Daily Average Users
Feature 2: Stock Price
Feature 3: Revenue

Additional Dataset #2 - Daily COVID Data: application/JSON MIME type


    Feature 1: New daily deaths due to COVID in INdia 

        This feature was derived from taking data on cumulative deaths in India on a daily basis (source: (https://covid19api.com) and finding the difference from the prior day

    Feature 2: New daily COVID cases in India 
        
        This feature was derived from taking data on cumulative COVID cases in India on a daily basis (source: (https://covid19api.com) and finding the difference from the prior day

    Feature 3: New vaccinations against COVID in India
        
        This feature was derived from taking data on the cumulative vaccinations in India on a daily basis (source: https://github.com/owid/covid-19-data) and finding the difference from the prior day

        Note: this data set only had data available as early as 1/15/2021, which listed India as having 0 vaccinations against COVID. Because the Pixstory data set starts 1/12/2020, we decided to and this missing dates and input 0's for all vaccinations. This was justified because according to this data set India hadn't had any vaccinations until 1/16/2021. 


Additional Dataset #3 - YouTube Daily Trending Videos: 

This is a dataset of the top trending videos on YouTube on any particular day. The MIME Type of this dataset is Video/ MP4. The data ranges from 2020 - 2022 and the features of this include: 

Feature #1: highest trending video name, 
Feature #2: highest trending video channel, 
Feature #3: highest trending video category, 
Feature #4: highest trending video views,  
Feature #5: highest trending video likes
