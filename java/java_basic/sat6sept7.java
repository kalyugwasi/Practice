class Placement
{
    int enroll;
    String name;
    static String college="JECRC";
    void insert(int e,String n){
        name = n;
        enroll = e;
    }
    void show(){
        System.out.print(enroll+" "+name+" "+college);
    }

}
public class sat6sept7 {
    public static void main(String[] args) {
        Placement p=new Placement();
        p.insert(101,"Prithvi");
        p.show();
    }
}
