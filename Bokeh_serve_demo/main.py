# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 00:33:36 2021

@author: Yunpeng Cheng

@Github: https://github.com/ycheng22

Reference:
"""
#I will focus on coding in notebook before coding python scripts

import sys
sys.path.insert(0, './scripts')
import pandas as pd
#import numpy as np

# Bokeh basics 
from bokeh.io import curdoc, show
from bokeh.models import Tabs, Column, Row

# Each tab is drawn by one script
from scripts.histogram import histogram_tab
from scripts.density import density_tab
from scripts.table import table_tab
from scripts.draw_map import map_tab
from scripts.routes import route_tab

# Using included state data from Bokeh for map
from bokeh.sampledata.us_states import data as states

# Load in flights and inspect
flights = pd.read_csv('./data/Hou_flights.csv', 
                    index_col=0).dropna()

# map_data = pd.read_csv('./data/arr_delay.csv', 
#                     index_col=0).dropna()
map_data = pd.read_csv('./data/arr_delay.csv').dropna()                    

# Create each of the tabs
tab_hist = histogram_tab(flights)
tab_density = density_tab(flights)
tab_table = table_tab(flights)
tab_map = map_tab(map_data, states)
tab_route = route_tab(flights)

# Put all the tabs into one application
tabs = Tabs(tabs = [tab_hist, tab_density, tab_table, tab_map, tab_route])
#show(tabs)
# Put the tabs in the current document for display
curdoc().add_root(tabs)

#in the app_demo folder, activate python env, run bokeh serve --show main.py
