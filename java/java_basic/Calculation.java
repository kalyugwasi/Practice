import Calculation.Calculator; // import from the package

public class Calculation {
    public static void main(String[] args) {
        Calculator calc = new Calculator();

        System.out.println("Addition: " + calc.add(5, 3));
        System.out.println("Subtraction: " + calc.subtract(5, 3));
        System.out.println("Multiplication: " + calc.multiply(5, 3));
        System.out.println("Division: " + calc.divide(10, 2));
    }
}