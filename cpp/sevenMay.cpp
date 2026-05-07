#include <iostream>
using namespace std;
class Demo{
    int sum = 0;
    Demo(int a,int b=10){
        sum = a+b;
    }
    Demo(int a,int b){
        sum = a+b;
    }
    int out(){
        return sum;
    }
};

int main(){
    Demo d1(10);
    d1.out();
    return 0;
}