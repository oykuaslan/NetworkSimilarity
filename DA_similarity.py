#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 12:51:42 2022

@author: apple
"""

import numpy as np
import networkx as nx
import netrd as nr
import json
import pandas as pd

data = np.load("/cta/users/zaslan/NetSci/DA_multisubject_dynamic_nw_series.npy")
data.shape

dist = [nr.distance.Hamming(), nr.distance.DegreeDivergence(), nr.distance.dkSeries(), nr.distance.JaccardDistance()]
distResults = list()
distMeasure = None
for i in range(data.shape[0]-1):
  for j in range(i+1,data.shape[0]):
    for k in range(len(dist)):
      G0_1 = nx.from_numpy_array(data[i][0])
      G0_2 = nx.from_numpy_array(data[j][0])
      d0 = dist[k].dist(G0_1, G0_2)

      G1_1 = nx.from_numpy_array(data[i][1])
      G1_2 = nx.from_numpy_array(data[j][1])
      d1 = dist[k].dist(G1_1, G1_2)
	
      if(k==0):
        distMeasure = 'Hamming'
      if(k==1):
        distMeasure = 'DegreeDivergence'
      if(k==2):
        distMeasure = 'dkSeries'
      if(k==3):
        distMeasure = 'Jaccard'
      
      distResults.append({
          'first_index':i,
          'second_index':j,
          'dist_measure':distMeasure,
          'distance_at_time0':d0,
	  'distance_at_time1':d1,
      })
      print(d0,d1)
      with open("/cta/users/zaslan/NetSci/DA_similarity.jsons", 'a') as fl:
        fl.write('{}\n'.format(json.dumps(distResults[-1])))
