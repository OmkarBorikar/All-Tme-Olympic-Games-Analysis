import numpy as np
import pandas as pd
import streamlit as st


#Get list of unique years and countries
def year_country_list(df):
    years = df['Year'].unique().tolist()
    years = sorted(years)
    years.insert(0, 'Overall')

    countries = np.unique(df['region'].dropna().values).tolist()
    countries = sorted(countries)
    countries.insert(0, 'Overall')

    return years,countries

# Return modified dataframe based on selected year and selected country

def modified_df(df,year,country):
    medal_df = df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])

    flag = 0

    if year=='Overall' and country == 'Overall':
        temp_df = medal_df
    elif year!='Overall' and country == 'Overall':
        temp_df = medal_df[medal_df['Year']==year]
    elif year == 'Overall' and country != 'Overall' :
        temp_df = medal_df[medal_df['region']==country]
        flag = 1
    elif (year != 'Overall' and country != 'Overall'):
        temp_df = medal_df[(medal_df['region']==country) & (medal_df['Year']==year)]


    if flag == 0:
        x = temp_df.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()
    else:
        x = temp_df.groupby('Year').sum()[['Gold','Silver','Bronze']].sort_values('Year',ascending=False).reset_index()

    x['Total'] = x['Gold'] + x['Silver'] + x['Bronze']

    x['Gold'] = x['Gold'].astype('int')
    x['Silver'] = x['Silver'].astype('int')
    x['Bronze'] = x['Bronze'].astype('int')
    x['Total'] = x['Total'].astype('int')
    x.rename(columns = {'region' : 'Country'},inplace=True)
    x.index +=1
    return x


#user_menu = Overall Analysis
#returns dataframe with 2 columns 1. Year 2 . Number of entity for each year. 
# entity can be - region (i.e no. of countries participated each olympic game) etc.

def data_over_time(df,col):

    nations_over_time = df.drop_duplicates(['Year', col])['Year'].value_counts().reset_index().sort_values('index')
    nations_over_time.rename(columns={'index': 'Edition', 'Year': col}, inplace=True)
    return nations_over_time



# Top athletes in selected sport


def sport_list(df):
    sports = np.unique(df['Sport'].dropna().values).tolist()
    sports = sorted(sports)
    sports.insert(0, 'Overall')
    return sports

def top_aths(df,sport):
    temp_df = df.dropna(subset=['Medal'])
    
    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]
        
    temp_df = temp_df['Name'].value_counts().reset_index().head(15)
    temp_df.rename(columns = {'index' : 'Name' , 'Name' : 'Medal'},inplace=True)
    
    x = temp_df.merge(df,on='Name',how='left')[
        ['Name', 'Medal_x', 'Sport', 'region']].drop_duplicates('Name')

    x.rename(columns = {'Medal_x' : 'Total medals' , 'region' : 'Country'},inplace=True)

    x = x.reset_index(drop=True)
    x.index +=1
    return x

# Number of medals for specific country over the years
def country_medals_list(df):
    countries = np.unique(df['region'].dropna().values).tolist()
    countries = sorted(countries)
    return countries

def country_medals(df,country):
    temp = df.dropna(subset=['Medal'])
    temp = temp.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])
    temp = temp[temp['region'] == country]
    x = temp.groupby('Year').count()['Medal'].reset_index()

    return x

# Top 5 sports for selected country
def top_5_sports(df,country):
    temp = df.dropna(subset=['Medal'])
    temp = temp.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])
    temp = temp[temp['region'] == country]
    temp = temp.groupby('Sport').count()['Medal'].reset_index().sort_values('Medal',ascending=False)
    x = pd.DataFrame(temp.head().reset_index(drop=True))
    x.index +=1
    return x

#Top 15 athletes of Country

def top_aths_country(df,country):
    temp_df = df.dropna(subset=['Medal'])
    

    temp_df = temp_df[temp_df['region'] == country]
        
    temp_df = temp_df['Name'].value_counts().reset_index().head(15)
    temp_df.rename(columns = {'index' : 'Name' , 'Name' : 'Medal'},inplace=True)
    
    x = temp_df.merge(df,on='Name',how='left')[
        ['Name', 'Medal_x', 'Sport']].drop_duplicates('Name')

    x.rename(columns = {'Medal_x' : 'Total medals' , 'region' : 'Country'},inplace=True)

    x = x.reset_index(drop=True)
    x.index +=1
    return x

#Number of males and females participated

def gender_count(df):

    temp = df[df['Sex'] == 'M']
    male_count = temp.groupby('Year')['Name'].nunique()
    male_count = male_count.reset_index()
    male_count.rename(columns={'Name' : 'Male'},inplace=True)

    temp = df[df['Sex'] == 'F']
    x = temp.groupby('Year')['Name'].nunique()
    x = x.reset_index()
    x.rename(columns={'Name' : 'Female'},inplace=True)
    # temp = {'Year' : 1896 , 'Female' : 0}
    # female_count =x.append(temp,ignore_index=True)
    female_count = x.sort_values('Year').reset_index(drop=True)

    gender_count = male_count.merge(female_count,on='Year',how='left')
    return gender_count.fillna(0)


# Age distribution of Gold medal winners for selected sport

# get list of sports in which at lease 5 gold medals are scored
def popular_sports(df):
    temp = df.drop_duplicates(subset=['Name','region'])
    temp = temp[temp['Medal'] == 'Gold']
    temp = temp.groupby('Sport').count()['Medal']
    temp =temp.reset_index()
    temp = temp[temp['Medal'] > 5]
    sport_list1 = temp['Sport'].tolist()
    return sport_list1

def age_dist(df,sport):
    temp = df.drop_duplicates(subset=['Name','region'])
    temp = temp[temp['Sport'] == sport]
    ages = temp[temp['Medal'] == 'Gold']['Age'].dropna()

    
    return ages

# Weight vs Height scatter plot

def weight_v_height(df,sport):
   temp = df.drop_duplicates(subset=['Name','region'])
   temp['Medal'].fillna('No Medal', inplace=True)
   if sport != 'Overall':
       temp = temp[temp['Sport'] == sport]
       return temp
   else:
       return temp

 
    


 





