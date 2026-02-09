class Student
{
    int id;
    static int cm=10000; // wont change and will be initialized same for every object created
    static void change()
    {
        cm=20000;
    }
    void insert(int i)
    {
        change();
        id = i;
    }
    void display()
    {
        System.out.print(id+" "+cm);
    }
}
class sat6sept6
{
    public static void main(String[] args) 
    {
        Student s1=new Student();
        s1.insert(5);
        //student.change()
        s1.display(); 
    }
}


