import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Insem2 {
    public static void main(String[] args) {
        // Original list with duplicates
        List<Integer> numbers = Arrays.asList(10, 20, 10, 30, 20, 40, 30, 50);
        System.out.println("Original List: " + numbers);

        // Use Stream distinct() to remove duplicates
        List<Integer> uniqueNumbers = numbers.stream()
                                             .distinct()
                                             .collect(Collectors.toList());

        System.out.println("List after removing duplicates: " + uniqueNumbers);
    }
}

/*
// Custom Exception
class PositiveNumberException extends Exception {
    public PositiveNumberException(String message) {
        super(message);
    }
}

public class insem2 {
    public static void main(String[] args) {
        try {
            File file = new File("java\\bbb.txt");
            
            // Check if file exists
            if (!file.exists()) {
                throw new FileNotFoundException("File not found!");
            }

            Scanner sc = new Scanner(file);

            // Read integers from file
            while (sc.hasNextInt()) {
                int num = sc.nextInt();

                // Throw exception for positive number
                if (num > 0) {
                    throw new PositiveNumberException("Positive number found: " + num);
                }
            }

            System.out.println("All numbers are non-positive [zero or negative].");
            sc.close();
        } 
        catch (PositiveNumberException e) {
            System.out.println("Exception caught: " + e.getMessage());
        } 
        catch (FileNotFoundException e) {
            System.out.println("Error: " + e.getMessage());
        } 
        catch (Exception e) {
            System.out.println("General Exception: " + e.getMessage());
        }
    }
}
*/
/*
public class insem2{
    static void checkVowels(String str) throws Exception {
 if (!str.toLowerCase().matches(".*[aeiou].*")) {
 throw new Exception("No vowels found in the string!");
 } else {
 System.out.println("String contains vowels.");
 }
 }
 public static void main(String[] args) {
 Scanner sc = new Scanner(System.in);
 try {
 System.out.print("Enter a string: ");
 String input = sc.nextLine();
 checkVowels(input);
 }
 catch (Exception e) {
 System.out.println("Exception: " + e.getMessage());
 }
 finally {
 sc.close();
 }
 }
}*/
/*
public class insem2{
    public static void main(String[] args) {
 Scanner sc = new Scanner(System.in);
 HashSet<Integer> set = new HashSet<>();
 try {
 System.out.print("Enter number of elements: ");
 int n = sc.nextInt();
 System.out.println("Enter " + n + " integers:");
 for (int i = 0; i < n; i++) {
 int num = sc.nextInt();
 // Check for duplicates
 if (!set.add(num)) {
 throw new Exception("Duplicate number found: " +
num);
 }
 }
 System.out.println("All numbers are unique!");
 }
 catch (Exception e) {
 System.out.println("Exception: " + e.getMessage());
 }
 finally {
 sc.close();
 }
 }

}
 */
/*
public class insem2{
    public static void main(String[] args) {
 try {
 File file = new File("java\\bbb.txt"); // file name
 if (!file.exists()) {
 throw new FileNotFoundException("File not found!");
 }
 FileReader fr = new FileReader(file);
 BufferedReader br = new BufferedReader(fr);

 // Check if first line is null → empty file
 if (br.readLine() == null) {
 throw new Exception("File is empty!");
 } else {
 System.out.println("File has content.");
 }
 br.close();
 fr.close();
 }
 catch (FileNotFoundException e) {
 System.out.println("Error: " + e.getMessage());
 }
 catch (Exception e) {
 System.out.println("Exception: " + e.getMessage());
 }
 }
}
*/
/*
class InsufficientBalanceException extends Exception
{
    // Constructor with custom message
    public InsufficientBalanceException(String message)
    {
        super(message);
    }
}

// Step 2: Use the custom exception in application
class BankAccount
{
    private double balance;

    public BankAccount(double balance)
    {
        this.balance = balance;
    }

    // Withdraw method which may throw the user-defined exception
    public void withdraw(double amount) throws InsufficientBalanceException
    {
        if(amount > balance)
        {
            throw new InsufficientBalanceException("Withdrawal failed: Insufficient balance!");
        }
        else
        {
            balance -= amount;
            System.out.println("Withdrawal successful. Remaining balance: " + balance);
        }
    }
    double getbalance(){
        return balance;
    }
}
public class insem2
{
    public static void main(String[] args)
    {
        BankAccount account = new BankAccount(5000);

        try
        {
            account.withdraw(6000); // Trying to withdraw more than balance
        }
        catch (InsufficientBalanceException e)
        {
            System.out.println("Exception caught: " + e.getMessage());
        }

        try
        {
            account.withdraw(3000); // Valid withdrawal
        }
        catch (InsufficientBalanceException e)
        {
            System.out.println("Exception caught: " + e.getMessage());
        }
        try
        {
            account.withdraw(3000); // Valid withdrawal
        }
        catch (InsufficientBalanceException e)
        {
            System.out.println("Exception caught: " + e.getMessage());
        }
        finally {
            System.out.println(account.getbalance());
        }
    }
}*/
/*
class RollnoException extends Exception {
    public RollnoException(String message){
        super(message);
    }
}
class Student implements Serializable {
    private static final long serialVersionUID = 1L; // Good practice for serialization

    private String name;
    private int rollno;

    // Constructor
    public Student(String name, int rollno) throws RollnoException {
        if (rollno <= 0) {
            throw new RollnoException("Invalid Roll Number: " + rollno);
        }
        this.name = name;
        this.rollno = rollno;
    }

    // Display method
     public String getName() {
        return name;
    }

    public int getRollno() {
        return rollno;
    }
    public void display() {
        System.out.println("Name: " + name);
        System.out.println("Roll No: " + rollno);
    }
}
public class insem2 {
    public static void main(String[] args) {
        try {
            // valid student
            Student s1 = new Student("Alice", 101);
            s1.display();

            // invalid student to trigger custom exception
            Student s2 = new Student("Bob", -10);
            s2.display();

        } catch (RollnoException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
    */
/*
// Main class
public class insem2 {
    public static void main(String[] args) {

        // Serialize the object
        try (
            FileOutputStream fileOut = new FileOutputStream("java\\student.txt");
            ObjectOutputStream out = new ObjectOutputStream(fileOut)
        ) {
            Student s1 = new Student("Alice", 101);
            out.writeObject(s1);
            System.out.println("Student object has been serialized to student.txt\n");
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Deserialize the object
        try (
            FileInputStream fileIn = new FileInputStream("java\\student.txt");
            ObjectInputStream in = new ObjectInputStream(fileIn)
        ) {
            Student student = (Student) in.readObject();
            System.out.println("Student object has been deserialized:");
            student.display();
            student.getName();
            student.getRollno();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        } finally {
            System.out.println("Program Finished");
        }

    }
}
*/


/*
class EmptyFileException extends Exception {
    EmptyFileException(String message) {
        super(message);
    }
}

public class insem2 {
    public static void main(String[] args) {
            System.out.println("------Programe Started------");
        try (FileInputStream file = new FileInputStream("java\\bbb.txt")){
            if (file.available() == 0){
                throw new EmptyFileException("File is empty!");
            }else{
                System.out.println("File has content.");
            }
        } 
        catch (EmptyFileException e) {
            System.out.println("Exception caught: " + e.getMessage());
        } 
        catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        } 
        finally {
            System.out.println("Program ended.");
        }
    }
}
*/

        /*{
            String data = "Hello, this is my first Java Program to write data in file. aacha...";
            FileOutputStream fos = new FileOutputStream("java\\bbb.txt");
            fos.write(data.getBytes());
            fos.close();
            System.out.println("Data successfully written to output.txt");

            BufferedInputStream fis = new BufferedInputStream(new FileInputStream("java\\bbb.txt"));
            int i;
            while ((i=fis.read()) != -1) { 
                System.out.print((char)i);
            }
            fis.close();
            
        }*/