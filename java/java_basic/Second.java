import java.awt.*;

class Second extends Frame {
    TextField textField;
    Button submitBtn;

    Second() {
        textField = new TextField(20);
        submitBtn = new Button("Submit");

        setLayout(new FlowLayout());
        add(textField);
        add(submitBtn);

        setSize(300, 200);
        setTitle("AWT");
        setVisible(true);
    }

    public static void main(String[] args) {
        new Second();
    }
}
