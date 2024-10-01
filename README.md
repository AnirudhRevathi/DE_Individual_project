1. What dataset did I choose and why?

NZ superannuation and Veteran's pension.

Pension data plays a vital role in ensuring the financial stability of the elderly population, informing policy decisions, and assessing future risks and opportunities. It is a key component of New Zealand’s social security system.

The pension system in New Zealand primarily consists of two types of pensions: New Zealand Superannuation (NZS) and the Veteran's Pension (VP). The dataset offers insights on a quarterly basis, taking into account factors such as age, ethnicity, and gender. These elements are likely crucial in establishing pensions' eligibility and determining the payment amount.

Pension data is also essential for policy planning and analysis.



2. Data source:

https://www.msd.govt.nz/about-msd-and-our-work/publications-resources/statistics/benefit/index.html

3. About the dataset:

The dataset included multiple sheets in a CSV file. I focused on the sheet named "Recipient chars- over time." This sheet contains two tables that provide information on two types of pensions: "NZ Superannuation" and "Veteran's Pension." The columns present data for each quarter over the past five years, starting from March 2019 to March 2024.

Rows have values which categorise observations by Gender, Age group, ethnic group and recipient of additional support. 

4. Data scraping and Wrangling:

Data has been scraped from the data source using Python. Python packages such as "Beautifulsoup", "os", and "requests" were used to achieve the task. The script can be found in the repository under the Scraper.py

The Dataset has been wrangled into a certain format. The new data frame has five columns namely "DATE", "RECIPIENT CHARACTERISTIC", "TYPE", "SUBTYPE", and "OBSERVATION". Please refer to the metadata provided in the following link: http://13.211.229.32:5000/are154/dataapi/metadata

Data has been wrangled in Python. The script can be viewed in DE_function.py

5. Analysis and visualisation:

Analysis:

Trend Analysis:
- Plot the number of recipients over time to see if there are any noticeable trends or patterns.
- Analyze the trend of pension recipients based on the 'Type' and 'Subtype' categories over time.

Demographic Analysis:
- Break down the data by age, ethnicity, and gender to understand the demographic distribution of pension recipients.
- Compare the number of recipients for New Zealand Superannuation and Veteran's Pension based on these demographic factors.

Comparative Analysis:
- Compare the number of recipients between the two types of pensions (NZS and VP).
- Compare the number of recipients based on 'Type' and 'Subtype' categories.

Correlation Analysis:
- Check if there's a correlation between the different 'Type' and 'Subtype' categories and the number of recipients.

Visualizations you could create:

Time Series Plots:
- Plot the number of recipients over time for each type of pension.
- Plot the number of recipients over time based on 'Type' and 'Subtype' categories.

Bar Charts:
- Create bar charts to compare the number of recipients between different demographic groups or between the two types of pensions.

Pie Charts:
- Use pie charts to show the proportion of recipients based on 'Type' and 'Subtype' categories.



