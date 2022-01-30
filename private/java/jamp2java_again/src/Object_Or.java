<<<<<<< HEAD
//
//class Calculator {
//    int result = 0;
//
//    int add(int num) {
//        result += num;
//        return result;
//    }
//}
//
//
//public class Object_Or {
//    class Calculator {
//        int result = 0;
//
//        int add(int num) {
//            result += num;
//            return result;
//        }
//    }
//    public static void main(String[] args) {
//        Calculator cal1 = new Calculator();  // 계산기1 객체를 생성한다.
//        Calculator cal2 = new Calculator();  // 계산기2 객체를 생성한다.
//
//        System.out.println(cal1.add(3));
//        System.out.println(cal1.add(4));
//
//        System.out.println(cal2.add(3));
//        System.out.println(cal2.add(7));
//    }
//}
//class Animal{
//    String name;
//
//    public void setName(String name) {
//        this.name = name;
//    }
//}
//public class Object_Or{
//    public static void main(String[] args) {
//        Animal cat  = new Animal();
//        cat.setName("NAVI");
//        System.out.println(cat.name);
//    }
//}
//public class Sample {
//    int sum(int a, int b) {  // a, b 는 매개변수
//        return a+b;
//    }
//
//    public static void main(String[] args) {
//        Sample sample = new Sample();
//        int c = sample.sum(3, 4);  // 3, 4는 인수
//
//        System.out.println(c);  // 7 출력
//    }
//}
//return을 써서 메소드 빠져나가기.
//public class Object_Or {
//    void sayNick(String nick){
//        if("fool".equals(nick)){
//            return;
//        }
//        System.out.println("나의 별명은"+nick+"입니다.");
//    }
//
//    public static void main(String[] args) {
//        Object_Or sample = new Object_Or();
//        sample.sayNick("angel");
//        sample.sayNick("fool");
//    }
//}
public class Object_Or {
    int a = 0;
    void raise_a(){
        this.a++;
    }

    public static void main(String[] args) {
        Object_Or sample = new Object_Or();
        System.out.println(sample.a);
        sample.raise_a();
        System.out.println(sample.a);
    }
=======
//
//class Calculator {
//    int result = 0;
//
//    int add(int num) {
//        result += num;
//        return result;
//    }
//}
//
//
//public class Object_Or {
//    class Calculator {
//        int result = 0;
//
//        int add(int num) {
//            result += num;
//            return result;
//        }
//    }
//    public static void main(String[] args) {
//        Calculator cal1 = new Calculator();  // 계산기1 객체를 생성한다.
//        Calculator cal2 = new Calculator();  // 계산기2 객체를 생성한다.
//
//        System.out.println(cal1.add(3));
//        System.out.println(cal1.add(4));
//
//        System.out.println(cal2.add(3));
//        System.out.println(cal2.add(7));
//    }
//}
//class Animal{
//    String name;
//
//    public void setName(String name) {
//        this.name = name;
//    }
//}
//public class Object_Or{
//    public static void main(String[] args) {
//        Animal cat  = new Animal();
//        cat.setName("NAVI");
//        System.out.println(cat.name);
//    }
//}
//public class Sample {
//    int sum(int a, int b) {  // a, b 는 매개변수
//        return a+b;
//    }
//
//    public static void main(String[] args) {
//        Sample sample = new Sample();
//        int c = sample.sum(3, 4);  // 3, 4는 인수
//
//        System.out.println(c);  // 7 출력
//    }
//}
//return을 써서 메소드 빠져나가기.
//public class Object_Or {
//    void sayNick(String nick){
//        if("fool".equals(nick)){
//            return;
//        }
//        System.out.println("나의 별명은"+nick+"입니다.");
//    }
//
//    public static void main(String[] args) {
//        Object_Or sample = new Object_Or();
//        sample.sayNick("angel");
//        sample.sayNick("fool");
//    }
//}
public class Object_Or {
    int a = 0;
    void raise_a(){
        this.a++;
    }

    public static void main(String[] args) {
        Object_Or sample = new Object_Or();
        System.out.println(sample.a);
        sample.raise_a();
        System.out.println(sample.a);
    }
>>>>>>> 58110c72042666d64e8117b99a8afe7db8511558
}