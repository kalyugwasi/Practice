class Test{
    void show(int x)
    {
        dis('A');
        System.out.println(x);
    }
    void dis(char x)
    {
        System.out.println(x);
    }
    void insert(double x)
    {
        show(89); // same as this.show(89)
        System.out.println(x);
    }
}
class methodchange
{
    public static void main(String[] args) {
        Test t=new Test();
        t.insert(9.9);
    }
}