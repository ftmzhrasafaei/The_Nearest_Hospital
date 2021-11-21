# The Nearest Hospital
Using dijkstra algorithm, this program give the distance between the current node and the available hospitals

### inputs
1- a file named "graph.txt" which contains n+2 rows:
* first row: the total number of nodes
* second row: the number of hospital nodes
* 3rd through n+2th rows: binary adjacency matrix of nodes in the city
### output
The minimum distance of each node to the nearest hospital

### Example

"graph.txt" in this repo
- number of nodes = 5
- first, second, and third nodes are hospitals
- adjacency matrix = [
 0 1 0 0 0;
 1 0 1 0 0;
 0 1 0 1 1;
 0 0 1 0 1;
 0 0 1 1 0;
]

Output= 10001

