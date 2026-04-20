import java.rmi.*;
import java.rmi.registry.*;

public class CalculatorServer {
    public static void main(String[] args) {
        try {
            LocateRegistry.createRegistry(1099);

            CalculatorImpl obj = new CalculatorImpl();

            Naming.rebind("rmi://localhost/CalculatorService", obj);

            System.out.println("Calculator Server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
