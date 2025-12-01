#include <iostream>
#include <string>
using namespace std;

void naiveStringMatching(string text, string pattern) {
    int n = text.length();
    int m = pattern.length();
    
    for (int i = 0; i <= n - m; i++) {
        int j = 0;
        
        while (j < m && text[i + j] == pattern[j]) {
            j++;
        }
        
        if (j == m) {
            cout << "Pattern found at index: " << i << endl;
        }
    }
}

int main() {
    string text = "ABCCDDEFFGGHH";
    string pattern = "CD";
    
    cout << "Text: " << text << endl;
    cout << "Pattern: " << pattern << endl;
    cout << "\nMatches:" << endl;
    
    naiveStringMatching(text, pattern);
    
    return 0;
}