import pandas as pd
import numpy as np
import folium
from sklearn import preprocessing
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.colors as colors
import re
import itertools

import plotly.express as px
import plotly.graph_objects as go


# Features Selection

def features(df, Area=False, Item=False, Element=False, plot=False):
    '''Inputs: the dataframe from FAO, the list of attributes we are interested in:
            Area, Item, Element: insert list of values we want to keep
    Output: the dataframe containing just the selected attributes
    '''

    # Preparation
    if Area:
        df = df[df.Area.isin(Area)]
    if Item:
        df = df[df.Item.isin(Item)]
    if Element:
        df = df[df.Element.isin(Element)]

    df = df.drop(columns=["Area Code","Item Code","Element Code","Unit"])
    
    df = df.melt(id_vars = ["Area","Item","Element"])\
            .rename(columns={"variable":"Year"}) \
            .pivot_table(index="Year",columns=["Area","Item","Element"], \
                      values="value") \
    
    df.reset_index(inplace=True)

    # Plot
    if plot:
        fig = go.Figure()
        for comb in list(itertools.product(Area,Item,Element)):
            fig.add_trace(go.Scatter(x=df.Year, y=df[comb], name=str(comb)))
        fig.update_layout(title_text='Time Series with Rangeslider',
                        xaxis_rangeslider_visible=True)
        fig.show()
    return df


def compare_different_country(df, country=False, feature=False, plot = False):
    ''' Given in input a df and the features we want to compare, it returns a time series plot
        IMPORTANT! Check the name of the columns to adapt the code
    '''
    if country:
        df = df[df.Area.isin(country)]
    if feature:
        df = df[["Year","Area"] + feature]
    
    df = df.melt(id_vars = ["Year","Area"], value_vars = feature). \
        pivot_table(index="Year",columns=["Area","variable"], values = "value", aggfunc="first")
    df.reset_index(inplace=True)
    
    # Plot
    if plot:
        fig = go.Figure()
        for comb in list(itertools.product(country,feature)):
            fig.add_trace(go.Scatter(x=df.Year, y=df[comb], name=str(comb)))
        fig.update_layout(title_text='Time Series with Rangeslider',
                        xaxis_rangeslider_visible=True)
        fig.show()
    return df



