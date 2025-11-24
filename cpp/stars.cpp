#include<iostream>
using namespace std;

int main(){
    int delimiter = 5;
    for (int i = 0; i < delimiter; i++) {
        for (int j = 1; j < delimiter; j++) {
            if (i == 0 || i == delimiter - 1 || j == 1 || j == delimiter) {
                cout << "* ";
            }
        }
        cout << endl;
    }
    return 0;
}
