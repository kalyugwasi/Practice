abstract class Test{
    abstract void f();
}
class base extends Test{
    void show(){}
    public static void main(String args[]){
        base b=new base();
        b.show();
        //Test t=new Test();
    }
}
