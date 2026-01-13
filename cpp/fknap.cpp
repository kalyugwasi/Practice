#include <iostream>
#include <algorithm>
using namespace std;

struct Item {
    double weight;
    double value;
    double ratio; // value to weight ratio
};

bool compare(Item a, Item b) {
    return a.ratio > b.ratio;
}

double fractionalKnapsack(Item items[], int n, double capacity) {
    // Sort items by value-to-weight ratio in descending order
    sort(items, items + n, compare);
    
    double totalValue = 0.0;
    
    for (int i = 0; i < n; i++) {
        if (capacity >= items[i].weight) {
            // Take the whole item
            totalValue += items[i].value;
            capacity -= items[i].weight;
        } else {
            // Take fractional part
            totalValue += items[i].ratio * capacity;
            capacity = 0;
            break;
        }
    }
    
    return totalValue;
}

int main() {
    int n;
    cout << "Enter number of items: ";
    cin >> n;
    
    Item items[100]; // Fixed size array
    
    cout << "Enter weight and value for each item:\n";
    for (int i = 0; i < n; i++) {
        cin >> items[i].weight >> items[i].value;
        items[i].ratio = items[i].value / items[i].weight;
    }
    
    double capacity;
    cout << "Enter knapsack capacity: ";
    cin >> capacity;
    
    double maxValue = fractionalKnapsack(items, n, capacity);
    cout << "Maximum value: " << maxValue << endl;
    
    return 0;
}
