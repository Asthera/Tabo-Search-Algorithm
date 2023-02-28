from itertools import combinations
import os,sys,copy
import numpy as np
import time
import TSP
import matplotlib.pyplot as plt


class Tabu():
    def __init__(self,disMatrix,max_iters=200,maxTabuSize=20):
        self.disMatrix = disMatrix
        self.maxTabuSize = maxTabuSize
        self.max_iters = max_iters
        self.tabu_list=[]

    def get_route_distance(self,route):   
        routes = [0] + route + [0]    # add the start and end point 
        total_distance = 0
        for i,n in enumerate(routes):
            if i != 0 :
                
                total_distance = total_distance +  self.disMatrix[last_pos][n] 
            last_pos = n
        return total_distance

    def exchange(self,s1,s2,arr):
        current_list = copy.deepcopy(arr)
        index1 , index2 = current_list.index(s1) , current_list.index(s2)  # get index
        current_list[index1], current_list[index2]= arr[index2] , arr[index1]
        return current_list

    def generate_initial_solution(self,num=10,mode='greedy'):
        if mode == 'greedy':
            route_init=[0]        
            for i in range(num):
                best_distance = 10000000
                for j in range(num+1):
                    if self.disMatrix[i][j] < best_distance and j not in route_init:  
                        best_distance = self.disMatrix[i][j]
                        best_candidate = j
                route_init.append(best_candidate)
            route_init.remove(0)
                     
        if mode == 'random':
            route_init = np.arange(1,num+1) 
            np.random.shuffle(route_init)  

        return list(route_init)

    def tabu_search(self,s_init):
        s_best = s_init
        
        bestCandidate = copy.deepcopy(s_best)
        routes , temp_tabu = [] , []   # init
        routes.append(s_best)
        
        while(self.max_iters):
            self.max_iters -= 1
            neighbors = copy.deepcopy(s_best)
            #combinations
            for s in combinations(neighbors, 2):
                sCandidate = self.exchange(s[0],s[1],neighbors)
            
                if s not in self.tabu_list and self.get_route_distance(sCandidate) < self.get_route_distance(bestCandidate):
                    bestCandidate = sCandidate
                    temp_tabu = s                           
            if self.get_route_distance(bestCandidate) < self.get_route_distance(s_best): # record the best solution
            
                s_best = bestCandidate
            if  temp_tabu not in self.tabu_list:
                self.tabu_list.append(temp_tabu)
            if len(self.tabu_list) > self.maxTabuSize : #FIFo
                self.tabu_list.pop(0)
            routes.append(bestCandidate)
        return s_best, routes
