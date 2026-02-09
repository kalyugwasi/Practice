import java.awt.*;
import java.awt.event.*;

public class awdbuttontext extends Frame {
    
    awdbuttontext() {  // constructor name must match the class name
        Button btn = new Button("Jecrc");
        btn.setBounds(300, 300, 100, 100);
        TextField txt=new TextField();
        txt.setBounds(500,300,100,100);
        add(txt);
        add(btn);


        setLayout(null);
        setSize(500, 500);
        setVisible(true);
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });
    }

    public static void main(String[] args) {
        new awdbuttontext();
    }
}
