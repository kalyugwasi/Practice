import java.util.*;

public class third {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a three digit number: ");
        int num = sc.nextInt();
        
        int oNum = num;
        int result = 0;

        while (num > 0) {
            int digit = num % 10;
            result += digit * digit * digit;
            num = num / 10;
        }

        if (result == oNum)
            System.out.println(oNum + " is an Armstrong number");
        else
            System.out.println(oNum + " is NOT an Armstrong number");

        sc.close();
    }
}
