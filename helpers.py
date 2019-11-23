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
    '''
    Inputs: the dataframe from FAO, the list of attributes we are interested in:
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


# Dataset Preparation for Plot 


