class Counter{
    static int count = 0;
    Counter(){
        this.count++;
        System.out.println(this.count);
    }
    //static변수 - 값이 변하지않으며 메모리 절약.
    // + 동일 메모리에 저장됨으로 다른 객체가 같은 변수를 공유함.

    public static int getCount() {
        return count;
    }
    //static 메소드는 객체 없이 호출 가능.
}
public class static_var {
    public static void main(String[] args) {
        Counter c1 = new Counter();
        Counter c2 = new Counter();
        System.out.println(Counter.getCount());
    }
}
