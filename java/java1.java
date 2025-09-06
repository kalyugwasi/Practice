package java;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URI;
import java.net.URL;
public class java1 {
    public static void main(String[] args)  {
        try {
            URL my_url = new URI.toURL("http://www.github.com");
            BufferedReader br = new BufferedReader(new InputStreamReader(my_url.openStream()));
            String strTemp = "";
            while(null != (strTemp = br.readLine())){
                System.out.println(strTemp);
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}