import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.*;

public class Client {
    public static void main(String[] args) throws Exception{
        Socket s = new Socket("localhost", 6000);
        DataInputStream dis = new DataInputStream(s.getInputStream());
        DataOutputStream dos = new DataOutputStream(s.getOutputStream());
        dos.writeUTF("Hello Server");
        String reply = dis.readUTF();
        System.out.println("Server says: " + reply);
        s.close();
    }
}
/*
public class Client {
    public static void main(String[] args) throws Exception {
        Socket s = new Socket("localhost", 5000);
        DataOutputStream dos = new DataOutputStream(s.getOutputStream());
        dos.writeUTF("Teri mummi");
        dos.flush();
        dos.close();
        s.close();
    }
}
*/