import java.rmi.*;

public interface Hello extends Remote {
    String sayHello() throws RemoteException;
}

import java.rmi.server.*;

public class HelloImpl extends UnicastRemoteObject implements Hello {

    protected HelloImpl() throws RemoteException {}

    public String sayHello() {
        return "Hello from Server";
    }
}

import java.rmi.*;

public class RMIServer {
    public static void main(String[] args) {
        try {
            Hello obj = new HelloImpl();
            Naming.rebind("HelloService", obj);
            System.out.println("Server started...");
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
}

import java.rmi.*;

public class RMIClient {
    public static void main(String[] args) {
        try {
            Hello obj = (Hello) Naming.lookup("rmi://localhost/HelloService");
            System.out.println(obj.sayHello());
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
}