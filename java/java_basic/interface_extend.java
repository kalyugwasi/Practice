interface my{
    public void show();
}
interface our extends my{
    public void dis();
}
class Test implements our{
    void show(){}
    void dis(){}
    public static void main(String args[]){}
 }