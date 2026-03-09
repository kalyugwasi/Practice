import java.net.*;

public class Server {
    public static void main(String[] args) throws Exception {
        DatagramSocket ds = new DatagramSocket(7000);
        byte[] recieve = new byte[1024];
        DatagramPacket dp = new DatagramPacket(recieve, recieve.length);
        ds.receive(dp);
        String msg = new String(dp.getData());
        System.out.println("Client wants to say " + msg);
        ds.close();
    }
}

/*
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
*//*
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