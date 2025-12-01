#include<iostream>
using namespace std;
int main(){
    int n,target;
    cout<<"Enter number of elements: ";
    cin>>n;
    int nums[n];
    cout<<"Enter the elements saperated by space: ";
    for(int i=0;i<n;i++){
        cin>>nums[i];
    }
    cout<<"Enter the target element: ";
    cin>>target;
    for(int i=0;i<n;i++){
        if(nums[i]==target){
            cout<<"Element found at location: "<<i+1;
            break;
        }
    }
}