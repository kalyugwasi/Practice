import java.io.IOException;
import jsva.io.*;
public class exceptionhandling {
    /*
    public static void main(String[] args) {
        int data;
        data = 10/0;
        System.out.println("Hello");
    }

    "This wont execute this will terminate in the debug console stating that
    Exception in thread "main" java.lang.ArithmeticException: / by zero
	at exceptionhandling.main(exceptionhandling.java:4) "
        */

    /*Nested try
    public static void main(String[] args) {
        try {
            try {
                int data;
                data=10/0;
            } catch (ArithmeticException e) {
                System.out.println(e);
            }
            try {
                int num;
                num = "Rahul";
            } catch (NumberFormatException e) {
                System.out.println(e);
            }
        } catch (Exception e){
            System.out.println("Handled");
        }
    }
        */
    /* Throw
    public static void main(String[] args) {
        try{
        int age=8;
        if (age<18){
            throw new NullPointerException("not for vote");
        } else{
            System.out.println("valid for vote");
        }
        } catch (Exception e){
            System.out.println(e);
        }
        System.out.println("Rest of the code..");
    } 
        */
    void m() throws IOException{
        throw new IOException("Device error");
    } 
    void n() throws IOException{
        m();
    }
    void p(){
        try {
            n();
        } catch (Exception e) {
            System.out.println("Exception handeled");
        }
    }
    public static void main(String args[])
    {
            exceptionhandling obj=new exceptionhandling();
            obj.p();
            System.out.println("Normal flow.."); 
            
    }
}
