class shape{
    String color;
    public void printInfo(){
        System.out.println(color);
    }
}
class Triangle extends shape{
}
class circle extends shape{
}
public class insem2 {
    public static void main(String[] args){
        Triangle t1=new Triangle();
        t1.color = "red";  
        t1.printInfo();  

        circle c1=new circle();
        c1.color = "yellow";  
        c1.printInfo();
    }
}
