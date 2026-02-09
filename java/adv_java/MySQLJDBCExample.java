import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class MySQLJDBCExample {
    private static final String DB_URL = "jdbc:mysql://localhost:3306/?useSSL=false&serverTimezone=UTC";
    private static final String USER = "root";
    private static final String PASS = "haider";

    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            try (Connection conn = DriverManager.getConnection(DB_URL, USER, PASS);
                    Statement stmt = conn.createStatement()) {
                String sql = "CREATE DATABASE registration";
                stmt.executeUpdate(sql);
                System.out.println("Database created successfully!");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

/*
 * class Test extends Frame {
 * Test() {
 * Label heading = new Label("STUDENT REGISTRATION", Label.CENTER);
 * heading.setBounds(150, 30, 300, 40);
 * heading.setFont(new Font("Arial", Font.BOLD, 20));
 * add(heading);
 * 
 * Label lbl1 = new Label("Name");
 * lbl1.setBounds(100, 80, 150, 30);
 * TextField txt1 = new TextField();
 * txt1.setBounds(260, 80, 200, 30);
 * 
 * Label lbl2 = new Label("Enroll No.");
 * lbl2.setBounds(100, 120, 150, 30);
 * TextField txt2 = new TextField();
 * txt2.setBounds(260, 120, 200, 30);
 * 
 * Label lbl3 = new Label("Section");
 * lbl3.setBounds(100, 160, 150, 30);
 * TextField txt3 = new TextField();
 * txt3.setBounds(260, 160, 200, 30);
 * 
 * Label lbl4 = new Label("Semester");
 * lbl4.setBounds(100, 200, 150, 30);
 * TextField txt4 = new TextField();
 * txt4.setBounds(260, 200, 200, 30);
 * 
 * Label lbl5 = new Label("Course");
 * lbl5.setBounds(100, 240, 150, 30);
 * TextField txt5 = new TextField();
 * txt5.setBounds(260, 240, 200, 30);
 * 
 * Label lbl6 = new Label("Subject");
 * lbl6.setBounds(100, 280, 150, 30);
 * TextField txt6 = new TextField();
 * txt6.setBounds(260, 280, 200, 30);
 * 
 * Label lbl7 = new Label("Aadhar Number");
 * lbl7.setBounds(100, 320, 150, 30);
 * TextField txt7 = new TextField();
 * txt7.setBounds(260, 320, 200, 30);
 * 
 * Button btn = new Button("Submit");
 * btn.setBounds(250, 380, 80, 40);
 * 
 * add(lbl1); add(txt1);
 * add(lbl2); add(txt2);
 * add(lbl3); add(txt3);
 * add(lbl4); add(txt4);
 * add(lbl5); add(txt5);
 * add(lbl6); add(txt6);
 * add(lbl7); add(txt7);
 * add(btn);
 * 
 * setLayout(null);
 * setSize(600, 500);
 * setVisible(true);
 * }
 * 
 * public static void main(String args[]) {
 * new Test();
 * }
 * }
 */
