import java.rmi.Remote;
import java.rmi.RemoteException;

public interface SecondHighestInterface extends Remote {
    // Method to calculate the second highest number
    int findSecondHighest(int[] numbers) throws RemoteException;
}
