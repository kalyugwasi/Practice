import java.io.*;

class EmptyFileException extends Exception {
    EmptyFileException(String message) {
        super(message);
    }
}

public class insem2 {
    public static void main(String[] args) {
            System.out.println("------Programe Started------");
        try (FileInputStream file = new FileInputStream("java\\bbb.txt")){
            if (file.available() == 0){
                throw new EmptyFileException("File is empty!");
            }else{
                System.out.println("File has content.");
            }
        } 
        catch (EmptyFileException e) {
            System.out.println("Exception caught: " + e.getMessage());
        } 
        catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        } 
        finally {
            System.out.println("Program ended.");
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