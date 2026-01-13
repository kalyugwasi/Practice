#include <iostream>
#include <set>

using namespace std;

int setcover(set<int> sets[], int numSets, set<int>& universe) {
    set<int> uncovered = universe;
    int count = 0;
    
    while (!uncovered.empty()) {
        int bestSet = -1;
        int maxCovered = 0;
        
        // Find set that covers most uncovered elements
        for (int i = 0; i < numSets; i++) {
            int covered = 0;
            for (int elem : sets[i]) {
                if (uncovered.count(elem)) {
                    covered++;
                }
            }
            if (covered > maxCovered) {
                maxCovered = covered;
                bestSet = i;
            }
        }
        
        if (bestSet == -1) break;
        
        // Remove covered elements
        for (int elem : sets[bestSet]) {
            uncovered.erase(elem);
        }
        count++;
    }
    
    return count;
}

int main() {
    set<int> sets[4] = {
        {1, 2, 3},
        {2, 4},
        {3, 4, 5},
        {5, 6}
    };
    
    set<int> universe = {1, 2, 3, 4, 5, 6};
    
    int result = setcover(sets, 4, universe);
    cout << "Minimum sets needed: " << result << endl;
    
    return 0;
}
