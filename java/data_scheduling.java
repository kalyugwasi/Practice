class Test
{
    int roll;
    void insert(int roll)
    {
        this.roll=roll;
        System.out.println(roll);
    }
    void dis()
    {
        System.out.println(roll+1);
    }
}
class data_scheduling {
    public static void main(String[] args) {
        Test t=new Test();
        t.insert(101);
        t.dis();
        //t.roll
    }
    
}
