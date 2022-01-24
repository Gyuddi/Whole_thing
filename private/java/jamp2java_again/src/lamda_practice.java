import java.util.ArrayList;
import java.util.Arrays;

public class lamda_practice {
    public static void main(String[] args) {
//        int[] numbers = {1, 2, 3, 4, 5};
//        int [] result = Arrays.stream(numbers)
//                .filter((a)-> a%2 == 1)
//                .map(a -> a = 2*a)
//                .toArray()
//                ;
//        System.out.println(Arrays.toString(result));
        int[] numbers = {1, -2, 3, -5, 8, -3};
        int[] result = Arrays.stream(numbers)
                .filter((a) ->a>0)
                .toArray()
                ;
        System.out.println(Arrays.toString(result));
    }
}
