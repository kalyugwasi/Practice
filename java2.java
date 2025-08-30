class Test{
    int a;
    void show(int x){
        a=x;
        System.out.println(x);
    }
    void dis(){
        System.out.print(a);
    }
    public static void main(String args[]) {
        Test t =new Test();
        t.show(24);
    }
}
