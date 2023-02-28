import TSP
from generator import generate

if __name__ == '__main__':

    NumberPoints = 100 # Number of vertex
    File_Path = "/Users/volodimir/Downloads/input.txt" # Path to  new file with tsp
    Way = 'greedy' # Chose 'random' or 'greedy'(method for init route) for tabu search 
    Iterations = 50 # Iterations for tabu search 
    Tabu_Size = 5 # Size of tabu list  
    StartPrice = 10
    EndPrice = 150
    generate(NumberPoints,StartPrice,EndPrice)
    TSP.tabu_tsp(File_Path , Iterations , Tabu_Size , Way)
