import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class SecondHighestClient {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            SecondHighestInterface stub = (SecondHighestInterface) registry.lookup("SecondHighest");

            int[] data = {10, 5, 20, 15, 30, 25};
            int result = stub.findSecondHighest(data);
            System.out.println("Second Highest: " + result);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
