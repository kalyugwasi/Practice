class Test{
    void show(int x)
    {
        System.out.println(x);
    }
    void show(char  x)
    {
        System.out.println(x);
    }
    void show(float x)
    {
        System.out.println(x);
    }
}

class sat6sept2
{
    public static void main(String args[])
    {
        Test t=new Test();
        t.show(2.8f);
    }
}