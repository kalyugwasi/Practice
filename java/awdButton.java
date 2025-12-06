import java.awt.*;
import java.awt.event.*;

public class awdButton extends Frame {
    
    awdButton() { 
        Button btn = new Button("Jecrc");
        btn.setBounds(100, 100, 100, 50);
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
        new awdButton();
    }
}
