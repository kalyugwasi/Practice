import java.io.*;
import java.util.*;

public class insem2 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter your data:");
            String data = sc.nextLine();
            sc.close();

            // Write to file
            try (FileOutputStream fw = new FileOutputStream("java\\bbb.txt")) {
                fw.write(data.getBytes());
                fw.close();
            }
            System.out.println("Data successfully written to bbb.txt");

            // Read from file
            try (FileReader fr = new FileReader("java\\bbb.txt")) {
                StringBuilder numericLine = new StringBuilder();
                StringBuilder charLine = new StringBuilder();

                int ch;
                while ((ch = fr.read()) != -1) {
                    numericLine.append(ch).append(" ");
                    charLine.append((char) ch);
                }
                fr.close();
                System.out.println(numericLine.toString());
                System.out.println(charLine.toString());
            } // <-- you forgot this closing brace
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage() + " file");
        }
    }
}


        /*{
            String data = "Hello, this is my first Java Program to write data in file. aacha...";
            FileOutputStream fos = new FileOutputStream("java\\bbb.txt");
            fos.write(data.getBytes());
            fos.close();
            System.out.println("Data successfully written to output.txt");

            BufferedInputStream fis = new BufferedInputStream(new FileInputStream("java\\bbb.txt"));
            int i;
            while ((i=fis.read()) != -1) { 
                System.out.print((char)i);
            }
            fis.close();
            
        }*/