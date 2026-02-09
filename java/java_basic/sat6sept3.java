class Test{
    void show(int x,long y)
    {
        System.out.println(x);
    }
    void show(long x,int y)
    {
        System.out.println(x);
    }
}

class sat6sept3
{
    public static void main(String args[])
    {
        Test t=new Test();
        t.show(24,26);
    }
}

//It gives ambiguity issues as both show can get the same value, it might work on cpp