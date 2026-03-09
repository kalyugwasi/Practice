
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.*;


public class Server {
    public static void main(String[] args) throws Exception {
        ServerSocket ss = new ServerSocket(6000);
        System.out.println("Waiting...");
        Socket s = ss.accept();
        DataInputStream dis = new DataInputStream(s.getInputStream());
        DataOutputStream dos = new DataOutputStream(s.getOutputStream());
        String msg = dis.readUTF();
        System.out.println("Client says: " + msg);
        dos.writeUTF("Hello Client");
        ss.close();
    }
}
/*
public class Server {
    public static void main(String[] args) throws Exception {
        ServerSocket ss = new ServerSocket(5000);
        System.out.println("Server Waiting...");
        Socket s = ss.accept();
        System.out.println("Client Conneceted");
        DataInputStream dis = new DataInputStream(s.getInputStream());
        String msg = dis.readUTF();
        System.out.println("Client Says: " + msg);
        ss.close();
    }
}
*/