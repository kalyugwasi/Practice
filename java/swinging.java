import java.awt.event.*;
import javax.swing.*;


public class swinging extends JFrame {
    swinging() {
        JLabel lbl1 = new JLabel("Email: ");
        lbl1.setBounds(100, 100, 50, 25);
        JTextField txt1 = new JTextField();
        txt1.setBounds(150, 100, 250, 25);

        JLabel lbl2 = new JLabel("Pass: ");
        lbl2.setBounds(100, 150, 50, 25); 
        JTextField txt2 = new JTextField();
        txt2.setBounds(150, 150, 250, 25);

        JButton btn = new JButton("Oh");
        btn.setBounds(200, 200, 80, 50);

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
        new swinging();
    }
}
