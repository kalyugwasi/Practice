import java.io.*;
public class iostreaming {
    /**
     * @param  args
     */
    public static void main(String args[]) {
        try {
            FileOutputStream fout=new FileOutputStream("java/abc.txt");
            String s = "hello";
            byte b[] = s.getBytes();
            fout.write(b);
            fout.close();
        }catch (Exception e) {
            System.out.println(e);
        }
        try {
            FileInputStream fin=new FileInputStream("java/abc.txt");
            int i = 0;
            while ((i=fin.read())!=-1){
                System.out.print((char)i);
            }
            fin.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
    
}
