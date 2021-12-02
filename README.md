# All-Tme-Olympic-Games-Analysis
In depth analysis of Olympic games of all time.

Dataset used can be found here- [Olympics Dataset](https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results)

This project is deployed on Heroku and can be accessed here - [Olympic games analysis](https://olympics-analysis-all-time.herokuapp.com/)

# About the Dataset

Dataset used for this project contains detailed information of Olympic games held from 1896 to 2020. Once in the history of Olympic games, Olympic were hosted in year 1904 , 1906 and 1908. That is, it was the only time when Olympic games were held after 2 years of another olympic games. Due to this, IOC (International Olympic Committee) currently does not recognize Athens 1906 as Olympic Games. So, all the rows with Year = 1906 have been dropped from the dataset. There are minor discrepancies present for few countries in the dataset due to some exceptions in Olympic games rules.

# Tools and Libraries used

* Pandas and Numpy - Used to read and manipulate dataset to transform it into the desired format for analysis.

* Plotly - Used for plotting various interractive plots such as Line plot, Pie chart, Scatter plot and Distribution plot.

* Streamlit - Framework used to build web application

* Heroku - Web application is deployed on Heroku.

# Web Application Overview

Web application can be accessed from here -  [Olympic games analysis](https://olympics-analysis-all-time.herokuapp.com/)

Four modes of analysis are provided and can be selected from sidebar as shown in images below.

Below snippet explaines content of each mode/window.

**1. Meddal Tally**

* Medal tally of selected country for selected year. If none is selected, medal tally for all the countries for all years will be displayed

![image](https://user-images.githubusercontent.com/82905366/140706531-84d2bf2b-0eb7-46bf-b3aa-1472ab0ea6bd.png)

2. Overall Analysis

* Top statistics of olympic games such as number of hosting countries, number of events, number of sports played in Olympic games, number of athletes etc.
* Plot representing Number of participating Nations over the years.
* Plot representing Number of events over the years.
* Plot representing Number of athletes participated over the years.

![image](https://user-images.githubusercontent.com/82905366/140707118-8647f027-4173-42e9-bed2-add392d8e9bc.png)

3. Country-wise Analysis

* Plot representing Number of medals won by selected country over the years (Default selected country is India).
* Pie chart and table representing top 5 medal winning sports of selected country.
* Table representing top 15 medal winning athletes of selected country.

![image](https://user-images.githubusercontent.com/82905366/140707553-c6da3bd3-19af-4878-affc-5487426a071d.png)

4. Athlete-wise Analysis

* Line plot representing Number of mens and womens participated in Olympic games over the years.
* Distribution plot representing age distribution of gold medal winners for popular sports. (Popular sports are the sports in which at least 5 gold medals are won)
* Scatter plot representing distribution of Gold, Silver, Bronze and no medals on the basis of Weight and Height.

![image](https://user-images.githubusercontent.com/82905366/140708344-7a559bff-eeec-4bbc-ab8a-acd5c7e394fe.png)




