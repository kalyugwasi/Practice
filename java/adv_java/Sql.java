import java.sql.*;

public class Sql {
    public static void main(String[] args) {
        //test
    }
}
class Drop {
    public static void main(String[] args) {
        try {
            Connection con = DriverManager.getConnection("jdbc:mysql//localhost:3302/",
                    "root",
                    "password"
                );
            Statement st = con.createStatement();
            String s = "DROP TABLE testdb";
            st.executeUpdate(s);
            System.out.println("Table Droppeed Successfully");
            con.close(); {
        
    }
        } catch (Exception e) {
        }
    }
}
class Insert {
    public static void entire(String[] args) {
        try {
            Connection con = DriverManager.getConnection("jdbc:mysql//localhost:3302/testdb",
                    "root",
                    "password"
                );
            Statement stmn = con.createStatement();
            String sql = "Insert into student values(101,'Himanshu',85)";
            stmn.executeUpdate(sql);
            System.out.println("Inserted Succcessfully");
            con.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void safe(String[] args) {
        try {
            Connection con = DriverManager.getConnection("jdbc:mysql//localhost:3302/testdb", "root", "password");
            String query = "INSERT INTO student(roll,name,per) VALUES(?,?,?)";
            PreparedStatement ps = con.prepareStatement(query);
            ps.setInt(1, 5);
            ps.setString(2, "Himanshu");
            ps.setInt(3, 20);
            ps.executeUpdate();
            System.out.println("Insertion successfull");
            con.close();
        } catch (Exception e) {
        }
    }
}

class Mysql{
    public static void main(String[] args){
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con = DriverManager.getConnection(
                "jdbc:mysql//localhost:3306/testdb",
                "root", 
                "passowrd");
                System.out.println("COnnected Successfully");
                con.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
class Oracle{
    public static void main(String[] args) {
        try {
            Class.forName("oracle.jdbc.driver.OracleDriver");
            Connection con=DriverManager.getConnection(
                "jdbc:oracle:thin@localhost:1512:xe",
                "System",
                "password"
            );
            System.out.println("Connection Successfull");
            con.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}