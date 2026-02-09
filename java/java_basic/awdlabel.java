import java.awt.*;
import java.awt.event.*;

public class awdlabel extends Frame {
    
    awdlabel() {  // constructor name must match the class name
        Button btn = new Button("Jecrc");
        btn.setBounds(100, 100, 100, 100);
        TextField txt=new TextField();
        txt.setBounds(200,100,100,100);
        Label lbl=new Label("Login");
        lbl.setBounds(300,400,100,50);
        add(lbl);
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
        new awdlabel();
    }
}

