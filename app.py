import streamlit as st
import os
import pandas as pd
from generate_df import generate_df
from plot_figs import plot_figs
from prepro import prepro
from generate_xtrain import generate_x_train
from model import lstm
from plot_pred import plot_pred

st.write("Projet Trading")



add_selectbox = st.selectbox(
    'Quelle entreprise vous intéresse?',
    ('NVDA', 'AMD', 'INTC'))

st.write("Voici les données récupérés par l'API")

df = generate_df(add_selectbox) 
df

st.write("Les données préalablement récupérer nous décrit donc cette courbe")

st.set_option('deprecation.showPyplotGlobalUse', False)
graph = plot_figs(df)
st.pyplot()

scaled_close_data, training_data_len, close_dataset, close_data, df = prepro(df)

x_train, y_train, df = generate_x_train(scaled_close_data, training_data_len, close_dataset, close_data, df)

st.write("En nous basant sur ces données et par le moyen d'une entraînement nous pouvons effectuer une prédiction par rapport à notre dataset")

valid, predictions, rmse, train, df = lstm(x_train, training_data_len, close_dataset, close_data, df, y_train)
valid

st.write("Ainsi il est aisé de constater que notre algorithme de prédiction respecte assez bien les tendances")

plot_pred(valid, predictions, rmse, train, df)
st.pyplot()





