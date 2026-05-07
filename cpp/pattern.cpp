#include <iostream>
using namespace std;
int main(){
    int n;
    cout << "Enter no. of rows:- "; cin >> n;
    for (int i=1; i<=n; i++){
        for (int k=5; k>=i; k--){
            cout.width(3);
            cout << " ";
        }
        for (int j=1; j<=i; j++){
            cout.width(3);
            cout<<"*";
        }
        for (int j=2; j<=i; j++){
            cout.width(3);
            cout<<"*";
        }
        cout<<endl;
    }
    for (int h=1;h<=n;h++){
        for(int n=1;n<=h+1;n++){
            cout.width(3);
            cout<<" ";
        }
        for (int m=1;m<=n-h;m++){
            cout.width(3);
            cout<<"*";
        }
        for (int m=2;m<=n-h;m++){
            cout.width(3);
            cout<<"*";
        }
        cout<<endl;
    }
    return 0;
}