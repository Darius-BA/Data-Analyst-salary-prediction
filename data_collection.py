# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 23:24:42 2020

@author: kevin
"""
import glassdoor_scrapper as gs
import pandas as pd

path = "K:/Personal/Data Analyst salary prediction/chromedriver"
df = gs.get_jobs("data analyst", 950, False, path, 15)