#include <iostream>
using namespace std;

#define MAX 100

int main() {
    int n, m;
    cout << "Enter number of vertices and edges: ";
    cin >> n >> m;
    
    int adj[MAX][MAX] = {0};
    int edges[MAX][2];
    
    cout << "Enter edges (u v):\n";
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1];
        adj[edges[i][0]][edges[i][1]] = 1;
        adj[edges[i][1]][edges[i][0]] = 1;
    }
    
    // Greedy approach for vertex cover
    bool covered[MAX] = {false};
    int vertexCover[MAX];
    int coverSize = 0;
    
    for (int i = 0; i < m; i++) {
        int u = edges[i][0];
        int v = edges[i][1];
        
        if (!covered[u] && !covered[v]) {
            vertexCover[coverSize++] = u;
            covered[u] = true;
            covered[v] = true;
        }
    }
    
    cout << "\nVertex Cover: ";
    for (int i = 0; i < coverSize; i++) {
        cout << vertexCover[i] << " ";
    }
    cout << "\nSize: " << coverSize << endl;
    
    return 0;
}