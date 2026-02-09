class Test{
    Test(int x,int y)
    {
        System.out.print(x+y);
    }
    Test(int x)
    {
        System.out.print(x);
    }
}
class sat6sept5
{
    public static void main(String args[])
    {
        Test t=new Test(20,90);
        Test t1=new Test(75);
    }    
}
