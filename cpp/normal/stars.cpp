#include <iostream>
using namespace std;

int main() {
    int delimiter = 3;

    for (int i = 0; i < delimiter; i++) {
        for (int j = 0; j < delimiter; j++) {
            if (i == 0 || i == delimiter - 1 || j == 0 || j == delimiter - 1) {
                cout << "* ";
            } else{
                cout<<"  ";
            }
        }
        cout << endl;
    }
    return 0;
}
