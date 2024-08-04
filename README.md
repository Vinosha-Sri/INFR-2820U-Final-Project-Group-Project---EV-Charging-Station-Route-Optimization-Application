# INFR-2820U-Final-Project-Group-Project---EV-Charging-Station-Route-Optimization-Application
# Introduction:

The objective of this project is to develop an application that, given a starting point, will be able to find the shortest path to each EV charging point in a network of nodes, thus choosing the most efficient route based on distance and other relevant information. 

# Features:

- Uses an array of edges to represent the graph then converts it to an array of edges. 
- Use the Dijikstra’s algorithm to calculate the shortest path from a starting node to all other nodes.
- Results in the recommendation of the nearest charging station based on the distances. 

# Setup: 

- Ensure that you have Python 3 installed on your device. 
- Clone this repository or download and use this source code on your Python compiler.

# Execution:

The program will result in the graph representation through an adjacency list, the shortest distances from the start node to any other node, and the recommended nearest charging station and the distance between. 

# Code Overview: 

- graphcreation(edges): Is used to convert the array of the edges into a graph represented as an adjacency list. 
- dijkstra(graph, start): Is used to implement Dijkstra’s algorithm to find the shortest path from the starting node.
- recommendedroute(distances, chargingstations): Analyzes and recommends the nearest charging station based on the calculated distances.
