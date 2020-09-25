import streamlit as st
import os
import pandas as pd
from generate_df import generate_df

st.write("Projet Trading")



add_selectbox = st.selectbox(
    'Quelle entreprise vous intéresse?',
    ('Nvidia', 'AMD', 'INTEL'))

if add_selectbox == "Nvidia":
    df = pd.read_csv("NVDA.csv")
    df
elif add_selectbox == "AMD":
    df = pd.read_csv("AMD/AMD.csv")
    df
else:
    df = pd.read_csv("INTC/INTC.csv")
    df

add_selectbox = st.selectbox(
    'Quelle entreprise vous intéresse?',
    ('Nvidia', 'AMD', 'INTEL'))

if add_selectbox == "Nvidia":
    df = pd.read_csv("NVDA.csv")
    df
elif add_selectbox == "AMD":
    df = pd.read_csv("AMD/AMD.csv")
    df
else:
    df = pd.read_csv("INTC/INTC.csv")
    df

add_selectbox = st.selectbox(
    'Quelle entreprise vous intéresse?',
    ('Nvidia', 'AMD', 'INTEL'))

if add_selectbox == "Nvidia":
    df = pd.read_csv("NVDA.csv")
    df
elif add_selectbox == "AMD":
    df = pd.read_csv("AMD/AMD.csv")
    df
else:
    df = pd.read_csv("INTC/INTC.csv")
    df

