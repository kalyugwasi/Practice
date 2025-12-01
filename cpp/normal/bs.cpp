#include<iostream>
using namespace std;
int bs(int nums[],int low,int high,int target){
    if (low > high){
        return -1;
    }
    int mid = (low+high)/2;
    if (nums[mid] == target)
        return mid+1;
    else if( nums[mid] > target)
        return bs(nums,low,mid-1,target);
    else
        return bs(nums,mid+1,high,target);
}
int main(){
    int n,target;
    cout<<"Enter len of array: ";
    cin>>n;
    int nums[n];
    cout<<"Enter the elements in sorted order: ";
    for (int i=0;i<n;i++){
        cin>>nums[i];
    }
    
    cout<<"Enter the target element: ";
    cin>>target;
    int res = bs(nums,0,n-1,target);
    if (res == -1){
        cout<<"Element not found";
    } else {
        cout<<"Element found at "<<res;
    }

}