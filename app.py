from google.protobuf.symbol_database import Default
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.figure_factory as ff
from streamlit.proto.RootContainer_pb2 import SIDEBAR
import helper
import plotly.express as px


st.set_page_config(layout="wide") 

df = pickle.load(open('df.pkl','rb'))

st.sidebar.title("Olympics Analysis")
st.sidebar.image('https://stillmed.olympics.com/media/Images/OlympicOrg/IOC/The_Organisation/The-Olympic-Rings/Olympic_rings_TM_c_IOC_All_rights_reserved_1.jpg?interpolation=lanczos-none&resize=1400:660')


user_menu = st.sidebar.radio(

    'Select an option',
    ('Medal Tally' , 'Overall Analysis' , 'Country-wise Analysis' , 'Athlete-wise Analysis')

)

#Medal Tally




if user_menu == 'Medal Tally':
    years,countries = helper.year_country_list(df)

    st.sidebar.header("Medal Tally")
    year = st.sidebar.selectbox('Select the Year',
    (years)
    )

    country = st.sidebar.selectbox('Select the Country',
    (countries)
    )

    medal_tally = helper.modified_df(df,year,country)

    if year=='Overall' and country == 'Overall':
        st.title('Overall performance of all countries in Olympic games')
    elif year!='Overall' and country == 'Overall':
        st.title(f'Performance of all countries in {year} Olympic games')
    elif year == 'Overall' and country != 'Overall' :
        st.title(f'Overall performance of {country} in Olympic games')
    elif (year != 'Overall' and country != 'Overall'):
        st.title(f'Performance of {country} in {year} Olympic games')

    st.table(medal_tally)


#Overall Analysis

if user_menu == 'Overall Analysis':
    st.sidebar.header("Overall Analysis")

    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title("Top Statistics")  
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Host Countries")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Participating Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)


#Graph of Number of nations vs Olympic games 
    st.title("Number of participating Nations over the years")
    nations_over_time = helper.data_over_time(df,'region')
    fig = px.line(nations_over_time, x="Edition", y="region",
    
    labels={
                     "region" : "Number of Nations participated"
                 }
    )

    fig.update_layout(
     autosize=False,
     width=1300,
     height=600 
    )
    fig.update_traces(
        line=dict(color="Light Blue", width=5),
    )
    st.write(fig)
   


#Graph of Number of Events vs Olympic games 

    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x="Edition", y="Event",
    
    labels={
                     "Event" : "Number of events"
                 }
    )
    
    
    st.title("Events over the years")
    fig.update_layout(
     autosize=False,
     width=1300,
     height=600 
    )
    fig.update_traces(
        line=dict(color="Light Blue", width=5),
    )
    st.write(fig)



#Graph of Number of athletes vs Olympic games 

    athlete_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athlete_over_time, x="Edition", y="Name",
    labels={
                     "Name" : "Number of athletes participated ( 1k = 1000 )"
                 }
    )
    st.title("Number of athletes over the years")
    fig.update_layout(
     autosize=False,
     width=1300,
     height=600 
    )
    fig.update_traces(
        line=dict(color="Light Blue", width=5),
    )
    st.write(fig)

# Top 15 athletes (Most medals earnes) in selectes sport

    st.title(f'Top 15 athletes')
    sports = helper.sport_list(df)
    sport = st.selectbox('Select a sport',
    (sports)
    ) 
    
    top_aths = helper.top_aths(df,sport)
    st.table(top_aths)


#Country-wise Analysis
if user_menu == 'Country-wise Analysis':
    st.sidebar.title('Country-wise Analysis')

    countries = helper.country_medals_list(df)

    country = st.sidebar.selectbox('Select the Country',
    (countries),index=80
    )
    

    country_medals = helper.country_medals(df,country)

    if country_medals['Medal'].sum() == 0:
        st.warning('This country did not win any medal')
    else:
        st.title(f'Number of medals {country} won over the years')
        fig = px.line(country_medals, x="Year", y="Medal",
        labels={
                        "Medal" : "Number of Medals"
                    }
        )
        fig.update_layout(
        autosize=False,
        width=1300,
        height=600 
        )
        fig.update_traces(
            line=dict(color="Light Blue", width=5),
        )
        st.write(fig)


    # Pie chart for top 5 sports of country
    
    top_5_sports = helper.top_5_sports(df,country)

    
    if top_5_sports['Medal'].sum() != 0:
        st.title(f'Top 5 medal winning sports of {country}')
        if len(top_5_sports['Medal']) < 5:
            st.warning(f'{country} has won Medals in only {len(top_5_sports.Medal)} sports')
        
        fig = px.pie(top_5_sports, values='Medal', names='Sport')
        col1,col2,col3 = st.columns(3)
        with col1:
            st.write(fig)

        with col3:
            st.table(top_5_sports)


    # Top 15 athletes of country
    st.title(f'Top 15 athletes of {country}')
    top_aths_country = helper.top_aths_country(df,country)
    st.table(top_aths_country)


#Athlete wise analysis

if user_menu == 'Athlete-wise Analysis':
    gender_count = helper.gender_count(df)
    st.title('Number of Mens and Womens participated over the years')
    fig = px.line(gender_count, x="Year", y=['Male' , 'Female'],
        labels={
                        "value" : "Number of athletes"
                    }
        )
    fig.update_layout(
        autosize=False,
        width=1300,
        height=600 
        )
    fig.update_traces(
            line=dict( width=5),
        )

    st.write(fig)

    # Age dist plot of gold medal winner for selected sport

    st.title(f'Age distribution of Gold medal winners for popular sports')

    sport_list = helper.popular_sports(df)

    # sport = st.selectbox('Select a sport',
    # (sport_list)
    # )
    final_ages = []
    for i in sport_list:

        final_ages.append(helper.age_dist(df,i))

    fig = ff.create_distplot(final_ages,sport_list,show_hist=False,show_rug=False)

    fig.update_layout(
        xaxis_title="Age",
        autosize=False,
        width=1300,
        height=600 
        )
    fig.update_traces(
            line=dict( width=2),
        )

    st.write(fig)
    

    # Weight vs height scatter plot

    st.title('Height vs Weight')

    sport_list_hw = helper.sport_list(df)

    selected_sport_hw = st.selectbox('Select the sport',options = sport_list_hw)

    df_hw = helper.weight_v_height(df,selected_sport_hw)

    fig = px.scatter(df_hw, y="Weight", x="Height", color="Medal", symbol="Sex")

    fig.update_layout(
        xaxis_title="Height in Cm",
        yaxis_title = "Weight in Kg",
        autosize=False,
        width=1300,
        height=600 
        )

   

    st.write(fig)


        
    




