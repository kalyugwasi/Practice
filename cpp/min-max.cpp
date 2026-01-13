#include <Bits/stdc++.h>
using namespace std;

int main() {
    int arr[] = {34, 15, 88, 2, 45, 67, 23};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    int mini = INT_MAX, maxi = INT_MIN;

    for(int i = 0; i< n ; i++){
        if (mini > arr[i]){
            mini = arr[i];
        }
        if (maxi < arr[i]){
            maxi = arr[i]; 
        }
    }
    cout<<mini<<" "<<maxi;
    
    return 0;
}