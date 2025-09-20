import java.test;

public class student {
    public static void main(String[] args) {
        test t = new test();

        t.setRoll(101);
        t.setName("Alice");
        t.setSalary(55000.50);

        System.out.println("Roll: " + t.getRoll());
        System.out.println("Name: " + t.getName());
        System.out.println("Salary: " + t.getSalary());
    }
}
