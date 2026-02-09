public class arr {

/*
    public static void main(String[] args) {
        int[] arr={1,2,3,4,5,6,7,8,9,10};
        int n = arr.length; // property
        // int n = arr.length(); //method
        for (int i=0;i<=arr.length;i++){
            System.err.println(arr[i]);
        }
    }
*/
    //alternate way
    public static void main(String[] args) {
        int[] arr; //declare
        arr=new int[5]; //memory initialization
        arr[0]=1; //define
        arr[1]=2;
        arr[2]=3;
        arr[3]=4;
        arr[4]=5;

        for (int i=0;i<=arr.length;i++){
            System.err.println(arr[i]);
        }
    }
    
}
