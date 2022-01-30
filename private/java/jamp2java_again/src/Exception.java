<<<<<<< HEAD
//public class Exception {
//    public static void main(String[] args) {
//        int c;
//        try{
//            c = 4/0;
//        }
//        catch (ArithmeticException e){
//            c = -1;
//        }
//        System.out.println(c);
//    }
//}
public class Exception extends Throwable {
    public void shouldbeRun(){
        System.out.println("ok thanks");
    }

    public static void main(String[] args) {
        Exception e = new Exception();
        int c;
        try {
            c = 4/0;
        }
        catch (ArithmeticException a){
            c = -1;
        }
        finally {
            e.shouldbeRun();
        }
        System.out.println(c);
    }
=======
//public class Exception {
//    public static void main(String[] args) {
//        int c;
//        try{
//            c = 4/0;
//        }
//        catch (ArithmeticException e){
//            c = -1;
//        }
//        System.out.println(c);
//    }
//}
public class Exception extends Throwable {
    public void shouldbeRun(){
        System.out.println("ok thanks");
    }

    public static void main(String[] args) {
        Exception e = new Exception();
        int c;
        try {
            c = 4/0;
        }
        catch (ArithmeticException a){
            c = -1;
        }
        finally {
            e.shouldbeRun();
        }
        System.out.println(c);
    }
>>>>>>> 58110c72042666d64e8117b99a8afe7db8511558
}