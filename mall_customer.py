import pandas as pd  
import streamlit as st  
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

df = pd.read_csv('cluster.csv')
st.header('Mall Customers')
st.write(df)