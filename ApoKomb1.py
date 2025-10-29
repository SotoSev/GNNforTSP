# -*- coding: utf-8 -*-
"""
Created on Thu May 25 22:27:48 2023

@author: Sotiris
"""
from haversine import haversine
import numpy as mp


def sindet(lats_c, lngs_c):
    coords = mp.column_stack((lats_c, lngs_c))
    return coords



def apostasis(node_citys, coords):
    
    distances =  [] 
    #mp.zeros(len(edge_index))
    #mp.zeros((len(node_citys),len(node_citys)))
    for i in range(len(node_citys)):
        for j in range(i+1,len(node_citys)):
            if i != j:
                distances.append(haversine(coords[i], coords[j]))
                #distances.append(haversine(coords[j], coords[i]))    
            
    return distances



def apostasis_test(node_citys, coords):
    
    distances =  mp.zeros((len(node_citys),len(node_citys)))
    t=0
    for i in range(len(node_citys)):
        for j in range(len(node_citys)):
            if haversine(coords[i], coords[j]) != 0:
                distances[i, j] = haversine(coords[i], coords[j])
    return distances



def  edge_index(node_citys):
    edge_index = []
    for i in range(len(node_citys)):
        for j in range(i+1, len(node_citys)):
            if i != j:
                #edge_index.extend([(i, j), (j, i)])
                edge_index.extend([(i, j)])
    return edge_index


def apostasis_training(coords):
    
    distances_train= []

    for t in range(len(coords)):
        distances =  []
        for i in range(len(coords[t])):
            for j in range(i+1,len(coords[t])):
                if i != j:
                    #if haversine(coords[t][i], coords[t][j]) != 0:
                    distances.append(haversine(coords[t][i], coords[t][j]))
        for i in range(len(coords[t])):
            for j in range(i+1,len(coords[t])):
                if i != j:
                    if haversine(coords[t][i], coords[t][j]) != 0:
                        distances.append(haversine(coords[t][i], coords[t][j]))

        distances_train.append(distances)
        #print(distances_train)
    
    return distances_train


def apostasis_test_train(node_citys, coords):
    
    distances_train= []

    for t in range(len(coords)):
        
        distances =  mp.zeros((len(node_citys),len(node_citys)))
    
        for i in range(len(node_citys)):
            for j in range(len(node_citys)):
                 if i != j:
                    distances[i, j] = haversine(coords[t][i], coords[t][j])
        distances_train.append(distances)  
        
    return distances_train


def  edge_index_training(node_citys):
    
    edge_index_training = []
    for t in range(len(node_citys)):
        edge_index = []
        for i in range(len(node_citys[t])):
            for j in range(i+1, len(node_citys[t])):
                if i != j:
                    edge_index.extend([(i, j)])
                    
        for i in range(len(node_citys[t])):
            for j in range(i+1, len(node_citys[t])):
                if i != j:
                    edge_index.extend([(j, i)])
                    
        edge_index_training.append(edge_index)
        
   
        
        
    return edge_index_training

