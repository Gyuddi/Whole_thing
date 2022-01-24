//interface Calculator2{
//    int sum(int a,int b);
//    //람다 함수 사용시 인터페이스 메서드는 1개만 가능.
//}

import java.util.function.BiFunction;
import java.util.function.BinaryOperator;

public class lamda {
    public static void main(String[] args) {
        //Calculator2 mc =(int a, int b) -> a +b;
        BinaryOperator<Integer> mc = (a, b) -> a+b;
        int result = mc.apply(3,4);
        System.out.println(result);
    }
}
