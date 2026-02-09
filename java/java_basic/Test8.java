class Test8{
    Test8(){System.out.println("parent");}
}
class Base extends Test8{
    Base(){
        System.out.println("Child");
    }
    public static void main(String args[]){
        Base t=new Base();  //Single level inheritence
        //Base t=new Test();  not supported
        //Test t=new Base();
        //Test t=new Test();
    }
    
}

// auto calls the super from base before printing the child 