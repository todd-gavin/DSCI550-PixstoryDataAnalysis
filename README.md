# DSCI550-PixstoryDataAnalysis

Collaborators: Jai Agrawal, Daniil Abbruzzese, Todd Gavin, Tania Dawood

1. Project Title: Mental health online activity 

2. Project Description: 

We have compiled a large dataset containing data provided from Pixstory, as well as additional data sources of various MIME types to perform an analysis on how the COVID pandemic has affected people's behavior online, with a focus on mental health. 

3. Additional Datasets Added:

Additional Dataset #1 - Snapchat Daily Average Users Data: test/CSV MIME type


Additional Dataset #2 - Daily COVID Data: application/JSON MIME type

    Feature 1: New daily deaths due to COVID in INdia 

        This feature was derived from taking data on cumulative deaths in India on a daily basis (source: (https://covid19api.com) and finding the difference from the prior day

    Feature 2: New daily COVID cases in India 
        
        This feature was derived from taking data on cumulative COVID cases in India on a daily basis (source: (https://covid19api.com) and finding the difference from the prior day

    Feature 3: New vaccinations against COVID in India
        
        This feature was derived from taking data on the cumulative vaccinations in India on a daily basis (source: https://github.com/owid/covid-19-data) and finding the difference from the prior day

        Note: this data set only had data available as early as 1/15/2021, which listed India as having 0 vaccinations against COVID. Because the Pixstory data set starts 1/12/2020, we decided to and this missing dates and input 0's for all vaccinations. This was justified because according to this data set India hadn't had any vaccinations until 1/16/2021. 


Additional Dataset #3 - YouTube Daily Trending Videos: 