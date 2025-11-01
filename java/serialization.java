import java.io.*;

class A implements Serializable {
    int i;
    String s;

    public A(int i, String s) {
        this.i = i;
        this.s = s;
    }
}

public class Serialization {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        A a = new A(20, "JECRC");

        // Write the object to file
        FileOutputStream fos = new FileOutputStream("xyz.txt");
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        oos.writeObject(a);
        oos.close();
        fos.close();

        // Read the object back from file
        FileInputStream fis = new FileInputStream("xyz.txt");
        ObjectInputStream ois = new ObjectInputStream(fis);
        A b = (A) ois.readObject();

        // Print the data
        System.out.println(b.i + " " + b.s);

        ois.close();
        fis.close();
    }
}
