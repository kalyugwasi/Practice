class ThreadA extends Thread {
    public void run() {
        for (int i = 0; i < 5; i++)
            Thread.sleep(500);
        System.out.println("Great");
    }
}

class ThreadB extends Thread {
    public void run() {
        for (int i = 0; i < 5; i++)
            System.out.println("Achievement");
    }
}

public class Endsem {
    public static void main(String[] args) {
        new ThreadA().start();
        new ThreadB().start();
    }
}

// class PageFetcher extends Thread {
// private String page;

// PageFetcher(String page) {
// this.page = page;
// }

// public void run() {
// System.out.println("Fetching page: " + page);
// try {
// Thread.sleep(1000);
// } catch (Exception e) {
// }
// System.out.println("Completed: " + page);
// }
// }

// public class Endsem {
// public static void main(String[] args) {
// PageFetcher p1 = new PageFetcher("Page-1");
// PageFetcher p2 = new PageFetcher("Page-2");
// PageFetcher p3 = new PageFetcher("Page-3");
// p1.start();
// p2.start();
// p3.start();
// }
// }

// class Student24 {
// String name;
// int age;

// Student24(String name, int age) {
// this.name = name;
// this.age = age;
// }

// public void printinfo() {
// System.out.println(name + " " + age);
// }
// }

// public class Endsem {
// public static void main(String[] args) {
// Student24 s1 = new Student24("Himanshu", 25);
// s1.printinfo();
// }
// }

// interface BasicAnimal {
// void eat();

// void sleep();
// }

// class Monkey implements BasicAnimal {
// void jump() {
// System.out.println("Monkey is jumping...");
// }

// void bite() {
// System.out.println("Monkey is biting...");
// }

// public void eat() {
// System.out.println("MOnkey is eating...");
// }

// @Override
// final void sleep() {
// System.out.println("Monkey is sleeping...");
// }
// }

// class Human extends Monkey implements BasicAnimal {
// public void eat() {
// System.out.println("Human is eating...");
// }

// public void sleep() {
// System.out.println("Human is sleeping...");
// }
// }

// public class Endsem {
// public static void main(String[] args) {
// Human h = new Human();
// h.jump();
// h.bite();
// h.eat();
// h.sleep();
// }
// }
// class Animal {
// void sound() {
// System.out.println("Animal makes a sound.");
// }
// }

// class Dog extends Animal {
// @Override
// void sound() {
// super.sound(); // calling superclass method
// System.out.println("Dog barks.");
// }
// }

// public class Endsem {
// public static void main(String[] args) {
// Dog d = new Dog();
// d.sound();
// }
// }
// import java.io.*;

// public class Endsem {
// public static void main(String[] args) {
// try {
// File file = new File("java\\f1.txt"); // file name
// if (!file.exists()) {
// throw new FileNotFoundException("File not found!");
// }
// FileReader fr = new FileReader(file);
// BufferedReader br = new BufferedReader(fr);

// // Check if first line is null → empty file
// if (br.readLine() == null) {
// throw new Exception("File is empty!");
// } else {
// System.out.println("File has content.");
// }
// br.close();
// fr.close();
// } catch (FileNotFoundException e) {
// System.out.println("Error: " + e.getMessage());
// } catch (Exception e) {
// System.out.println("Exception: " + e.getMessage());
// }
// }
// }
// import java.io.*;

// public class FileCount {
// public static void main(String[] args) {
// int charCount = 0, wordCount = 0, lineCount = 0;
// try {
// BufferedReader br = new BufferedReader(new FileReader("data.txt"));
// String line;
// while ((line = br.readLine()) != null) {
// lineCount++;
// charCount += line.length();

// // Split by spaces to count words
// String[] words = line.trim().split("\\s+");
// if (words.length == 1 && words[0].equals("")) {
// continue;
// }
// wordCount += words.length;
// }
// br.close();
// System.out.println("Lines: " + lineCount);
// System.out.println("Words: " + wordCount);
// System.out.println("Characters: " + charCount);
// } catch (IOException e) {
// System.out.println("Error: " + e.getMessage());
// }
// }
// }
// import java.io.*;

// public class Endsem {
// public static void main(String[] args) {
// int charCount = 0, wordCount = 0, lineCount = 0;
// try {
// BufferedReader br = new BufferedReader(new FileReader("java\\f1.txt"));
// String line;
// while ((line = br.readLine()) != null) {
// lineCount++;
// charCount += line.length();

// // Split by spaces to count words
// String[] words = line.trim().split("\\s+");
// if (words.length == 1 && words[0].equals("")) {
// continue;
// }
// wordCount += words.length;
// }
// br.close();
// System.out.println("Lines: " + lineCount);
// System.out.println("Words: " + wordCount);
// System.out.println("Characters: " + charCount);
// } catch (IOException e) {
// System.out.println("Error: " + e.getMessage());
// }
// }
// }
