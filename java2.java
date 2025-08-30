class Test{
    int roll_no;
    String name;
    void insert(int r,String n){
        roll_no = r;
        name=n;
    }
    void show(){
        System.out.println(roll_no+" "+name);
    }
    public static void main(String args[]) {
        Test t =new Test();
        t.insert(15,"Ansh");
        t.show();
    }
}
