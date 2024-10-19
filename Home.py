import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd 
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.markdown('<h1 style="color: brown; text-align : center;background-color:white; border:2px solid red"> COVID-19 DATA TRACKER </h1>', unsafe_allow_html=True) 
st.markdown('<p style="color: black; text-align : center; margin-top: 20px"> In December 2019, COVID-19 coronavirus was first identified in the Wuhan region of China. By March 11, 2020, the World Health Organization (WHO) categorized the COVID-19 outbreak as a pandemic. A lot has happened in the months in between with major outbreaks in Iran, South Korea, and Italy. We know that COVID-19 spreads through respiratory droplets, such as through coughing, sneezing, or speaking. But, how quickly did the virus spread across the globe? And, can we see any effect from country-wide policies, like shutdowns and quarantines? Fortunately, organizations around the world have been collecting data so that governments can monitor and learn from this pandemic. Notably, the Johns Hopkins University Center for Systems Science and Engineering created a publicly available data repository to consolidate this data from sources like the WHO, the Centers for Disease Control and Prevention (CDC), and the Ministry of Health from multiple countries. In this notebook, you will visualize COVID-19 data from the first several weeks of the outbreak to see at what point this virus became a global pandemic. The COVID-19 Data Tracker is designed to provide real-time updates and comprehensive insights into the ongoing pandemic. This tool aims to visualize key metrics such as infection rates, recovery rates, and vaccination progress, enabling users to understand the impact of COVID-19 in various regions.</p>', unsafe_allow_html=True) 


st.image('assets\image001.jpg',use_column_width=True) 