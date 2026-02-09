import javax.swing.*;

public class swinging2 extends JFrame {
    swinging2() {

        JLabel lbl1 = new JLabel("Email: ");
        lbl1.setBounds(100, 100, 50, 25);
        JTextField txt1 = new JTextField();
        txt1.setBounds(150, 100, 250, 25);

        JLabel lbl2 = new JLabel("Pass: ");
        lbl2.setBounds(100, 150, 50, 25);
        JPasswordField txt2 = new JPasswordField();
        txt2.setBounds(150, 150, 250, 25);

        JButton btn = new JButton("Oh");
        btn.setBounds(200, 200, 80, 40);

        ImageIcon img = new ImageIcon("C:\\Users\\himan\\Documents\\GitHub\\Practice\\html\\resources\\img\\image.jpg");

        JButton imgBtn = new JButton(img);
        imgBtn.setBounds(150, 250, 150, 80);

        add(lbl1);
        add(txt1);
        add(lbl2);
        add(txt2);
        add(btn);
        add(imgBtn);

        setVisible(true);        
        setLayout(null);
        setSize(500, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);


    }

    public static void main(String[] args) {
        new swinging2();
    }
}
