class Singleton{
    private static Singleton one;
    private Singleton(){
    }
    public static Singleton getInstance(){
        if (one == null){
            one = new Singleton();
            //객체가 단 한번 생성되어야 함으로, 가정문을 통해 확인.
        }
        return one;
    }
}
//싱글톤은 클래스를 통해 생성할 수 있는 객체가 단 하나.
public class Singleton_sample {
    public static void main(String[] args) {
        Singleton singleton1 = Singleton.getInstance();
        Singleton singleton2 = Singleton.getInstance();
        System.out.println(singleton1 == singleton2);
    }
}
