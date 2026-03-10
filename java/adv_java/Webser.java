import java.io.*;
import java.net.*;

public class Webser {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://www.google.com");
            URLConnection con = url.openConnection();
            BufferedReader br = new BufferedReader(new InputStreamReader(con.getInputStream()));
            InetAddress address = InetAddress.getByName("www.google.com");
            System.out.println(address.getHostAddress());
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
            System.out.println("\n");
            long date = con.getLastModified();
            if(date == 0){
                System.out.println("No modification information.");
            }
            else {
                System.out.println("File Last Modified on: "
                        + new java.util.Date(date));
            }
            long data = con.getDate();
            System.out.println(new java.util.Date(data));
            br.close();
            System.out.println(con.getPermission());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
}
