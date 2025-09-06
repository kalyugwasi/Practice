class Test{
    Test(int x)
    {
        System.out.println(x);
    }
    Test(char x)
    {
        this(8.9);
        System.out.println(x);
    }
    Test(double x)
    {
        this(90);
        System.out.println(x);
    }
}
class thisfunc
{
    public static void main(String[] args) {
        Test t=new Test('A');
    }
}