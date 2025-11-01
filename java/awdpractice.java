import java.awt.*;
import java.awt.event.*;

public class awdpractice extends Frame {
    awdpractice() {
        Label lbl1 = new Label("Email: ");
        lbl1.setBounds(100, 100, 50, 25);
        TextField txt1 = new TextField();
        txt1.setBounds(150, 100, 250, 25);

        Label lbl2 = new Label("Pass: ");
        lbl2.setBounds(100, 150, 50, 25); 
        TextField txt2 = new TextField();
        txt2.setBounds(150, 150, 250, 25);

        Button btn = new Button("Oh");
        btn.setBounds(200, 200, 80, 50);

        // Add components
        add(lbl1);
        add(txt1);
        add(lbl2);
        add(txt2);
        add(btn);

        setLayout(null);
        setSize(500, 400);
        setVisible(true);

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });
    }

    public static void main(String[] args) {
        new awdpractice();
    }
}
