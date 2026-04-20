import java.rmi.*;
import java.util.Scanner;

public class CalculatorClient {
    public static void main(String[] args) {
        try {
            Calculator c = (Calculator) Naming.lookup("rmi://localhost/CalculatorService");

            Scanner sc = new Scanner(System.in);

            System.out.print("Enter first number: ");
            int a = sc.nextInt();

            System.out.print("Enter second number: ");
            int b = sc.nextInt();

            System.out.println("Choose operation:");
            System.out.println("1. Add");
            System.out.println("2. Subtract");
            System.out.println("3. Multiply");
            System.out.println("4. Divide");

            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Result = " + c.add(a, b));
                    break;
                case 2:
                    System.out.println("Result = " + c.sub(a, b));
                    break;
                case 3:
                    System.out.println("Result = " + c.mul(a, b));
                    break;
                case 4:
                    System.out.println("Result = " + c.div(a, b));
                    break;
                default:
                    System.out.println("Invalid choice");
            }

            sc.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
