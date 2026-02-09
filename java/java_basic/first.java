class MyT implements Runnable {
    public void run() {
        for(int i = 1;i<= 5;i++ ){
            System.out.println("Thread executing: " + i);
            try {
                Thread.sleep(450);
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }
}

public class first {
    public static void main(String[] args){
        MyT task = new MyT();
        Thread thread = new Thread(task);
        thread.start();
        for(int i = 1; i <= 5; i++) {
            System.out.println("Main thread running: " + i);
        }
    }
}
