import java.util.ArrayList;
import java.util.Arrays;

//public class Loop {
//    public static void main(String[] args) {
//        int treeHit = 0;
//        while (treeHit < 10){
//            treeHit++;
//            System.out.println("나무를 "+treeHit+"번 찍었습니다.");
//            if (treeHit == 10){
//                System.out.println("나무가 쓰러졌습니다.");
//            }
//        }
//        int coffee_count = 0;
//        int coffee = 4500;
//        int budget = 50000;
//        while (budget>0){
//            coffee_count++;
//            budget = budget-coffee;
//        }
//        System.out.println("커피를 총"+coffee_count+"잔 시켰습니다.");
    //continue와 break 모두 존재한다.
//    }
//}
public class Loop {
    public static void main(String[] args) {
//        for(int i = 1;i<10;i++){
//            for(int j = 1;j<10;j++){
//                System.out.println(i+"*"+j+"="+i*j);
//            }
//        }
        //for each문도 존재한다.
        ArrayList<String> alist = new ArrayList<>(Arrays.asList("one","two","three"));
        for(String a: alist){
            System.out.println(a);
        }
    }
}