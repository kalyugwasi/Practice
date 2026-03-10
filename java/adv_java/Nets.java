
import java.net.*;


public class Nets {
    public static void main(String[] args) {
        try {
            InetAddress ip = InetAddress.getLocalHost();
            System.out.println(ip.getHostName());
            System.out.println(ip.getHostAddress());
            System.out.println(ip);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}