import java.io.*;

public class ReadWrite {
    public static void main(String[] args) {
        try {
            // Ensure folder exists
            File dir = new File("java");
            if (!dir.exists()) {
                dir.mkdir();
            }

            FileWriter fw = new FileWriter("java/abc.txt");
            fw.write("My name is Sachin");
            fw.close();
        } catch (Exception e) {
            System.out.println(e);
        }
        System.out.println("Success");
    }
}
