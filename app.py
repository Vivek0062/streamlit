import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt

pd.read_csv('Iris.csv')

data_path = "data/"

df = pd.read_csv(data_path+"Iris.csv")

st.dataframe(df)