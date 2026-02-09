/*
import java.io.*;
public class filing{
    public static void main(String args[]) throws Exception{
        FileOutputStream fout1=new FileOutputStream("java/f1.txt");
        FileOutputStream fout2=new FileOutputStream("java/f2.txt");
        
        ByteArrayInputStream bout=new ByteArrayInputStream();
        bout.write(65);
        bout.writeTo(fout1);
        bout.writeTo(fout2);

        bout.flush();
        bout.close();
        System.out.println("Success");
    }
}
*/
import java.io.*;

public class Filing {
    public static void main(String[] args) throws Exception {
        // Create output files
        FileOutputStream fout1 = new FileOutputStream("java/f1.txt");
        FileOutputStream fout2 = new FileOutputStream("java/f2.txt");
        
        // Use ByteArrayOutputStream to collect bytes in memory
        ByteArrayOutputStream bout = new ByteArrayOutputStream();
        bout.write(65); // writes the byte value 65 (which is 'A')
        
        // Write to both files
        bout.writeTo(fout1);
        bout.writeTo(fout2);

        // Flush and close streams
        bout.flush();
        bout.close();
        fout1.close();
        fout2.close();

        System.out.println("Success");
    }
}
