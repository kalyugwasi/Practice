#include <bits/stdc++.h>
using namespace std;

struct Node {
    char ch;
    int freq;
    Node *left, *right;

    Node(char c, int f) {
        ch = c;
        freq = f;
        left = right = nullptr;
    }
};

struct Compare {
    bool operator()(Node* a, Node* b) {
        return a->freq > b->freq;
    }
};

void printCodes(Node* root, string code) {
    if (!root) return;

    if (!root->left && !root->right) {
        cout << root->ch << " : " << code << "\n";
    }

    printCodes(root->left, code + "0");
    printCodes(root->right, code + "1");
}

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    string text ;
    getline(cin,text);

    unordered_map<char, int> freq;
    priority_queue<Node*, vector<Node*>, Compare> pq;
    
    for (char c : text)
        freq[c]++;

    for (auto &p : freq) {
        pq.push(new Node(p.first, p.second));
    }

    while (pq.size() > 1) {
        Node* left = pq.top(); pq.pop();
        Node* right = pq.top(); pq.pop();

        Node* merged = new Node('$', left->freq + right->freq);
        merged->left = left;
        merged->right = right;

        pq.push(merged);
    }

    Node* root = pq.top();
    printCodes(root, "");
    
    return 0;
}