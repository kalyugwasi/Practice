import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class secHighclient {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            secHighinterface stub = (secHighinterface) registry.lookup("SecondHighest");

            int[] data = { 10, 5, 20, 15, 30, 25 };
            int result = stub.findSecondHighest(data);
            System.out.println("Second Highest: " + result);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
