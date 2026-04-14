import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class secHighserver extends UnicastRemoteObject implements secHighinterface {
    protected secHighserver() throws RemoteException {
        super();
    }

    @Override
    public int findSecondHighest(int[] numbers) throws RemoteException {
        // Logic to find second highest
        int highest = Integer.MIN_VALUE;
        int secondHighest = Integer.MIN_VALUE;

        for (int num : numbers) {
            if (num > highest) {
                secondHighest = highest;
                highest = num;
            } else if (num > secondHighest && num != highest) {
                secondHighest = num;
            }
        }
        return secondHighest;
    }

    public static void main(String[] args) {
        try {
            secHighserver obj = new secHighserver();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.bind("SecondHighest", obj);
            System.out.println("Server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
