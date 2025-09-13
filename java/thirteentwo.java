class Test {
    void show(){
        System.out.println("Parent");
    }
}
class Base extends Test{
    void show(){
        super.show(); //super keyword
        System.out.println("child");
    }
    public static void main(String args[]){
        Base t=new Base();  //Single level inheritence
        //Base t=new Test();  not supported
        //Test t=new Base();
        //Test t=new Test();
        t.show();
    }
    
}