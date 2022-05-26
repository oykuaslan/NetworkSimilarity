#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 12:51:42 2022

@author: apple
"""
#distance between same object in different timestamp
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
for i in range(data.shape[0]):
    for k in range(len(dist)):
      G1 = nx.from_numpy_array(data[i][0])
      G2 = nx.from_numpy_array(data[i][1])
      d = dist[k].dist(G1, G2)
      if(k==0):
        distMeasure = 'Hamming'
      if(k==1):
        distMeasure = 'DegreeDivergence'
      if(k==2):
        distMeasure = 'dkSeries'
      if(k==3):
        distMeasure = 'Jaccard'
      
      distResults.append({
          'index':i,
          'dist_measure':distMeasure,
          'distance':d
      })
      print(d)
      with open("/cta/users/zaslan/NetSci/DA_similarity_subjectbased.jsons", 'a') as fl:
        fl.write('{}\n'.format(json.dumps(distResults[-1])))
