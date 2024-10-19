import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd 
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.title(" Covid-19 Data Tracker ")

df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\DA1 Project\Latest Covid-19 India Status.csv")

df

