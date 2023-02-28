from Tabu import Tabu
import time
import matplotlib.pyplot as plt
import numpy as np

#Read from file and convert to tsp matrix 

def get_matrix(file_path):
    #read
    file = open(file_path, "r")
    lines = file.readlines()
    edges = list()
    nodes_num = 0  # number of nodes
    for string in lines:
        edges.append(list(string.rstrip().split(' ')))  # parse input to list
        edges[-1] = [int(edges[-1][0]), int(edges[-1][1]), int(edges[-1][2])]
        nodes_num = max(nodes_num, max(edges[-1][0], edges[-1][1]))  # find the num of nodes
    file.close()

    #convert
    matrix = list()  # matrix of distances
    for i in range(nodes_num):
        matrix.append(list())
        for j in range(nodes_num):
            matrix[i].append(0)
    for edge in edges:
        matrix[edge[0] - 1][edge[1] - 1] = edge[2]
        matrix[edge[1] - 1][edge[0] - 1] = edge[2]
    return  nodes_num - 1, matrix


def tabu_tsp(file_path, iterations, tabu_size, mode):
    nodes_count, data = get_matrix(file_path)
    tsp = Tabu(data , iterations, tabu_size)  
    s_init = tsp.generate_initial_solution(nodes_count, mode) # mode = "greedy"  or "random"

    print('init route : ' , s_init)
    print('init distance : ' , tsp.get_route_distance(s_init))

    best_route , routes = tsp.tabu_search(s_init)     # tabu search

    print('best route : ' , best_route)
    print('best best_distance : ' , tsp.get_route_distance(best_route))
    #graf
    results=[]
    for i in routes:
        results.append(tsp.get_route_distance(i))    
    plt.plot(np.arange(len(results)) , results, marker='o', linestyle='dashed')
    plt.title(f"Tabu TSP '{mode}-way', {nodes_count + 1} nodes, {tabu_size} tabu size")
    plt.xlabel('Iterations')
    plt.ylabel('Cost of route')
    plt.show()
   
