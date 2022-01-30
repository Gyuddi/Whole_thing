import java.util.ArrayList;
import java.util.Arrays;

public class Array_List {
    public static void main(String[] args) {
//        int [] a = {9,8,7,4,5,6,2,1};
//        for(int i = 0;i <a.length;i++){
//            System.out.println(a[i]);
        //array는 생성할 때 길이가 고정됨. sout으로 프린트 불가....
//        int[] a = {2,1,3};
//        ArrayList<String> pitches = new ArrayList<>();
//        pitches.add("150");
//        pitches.add("152");
//        pitches.add("148");
//        System.out.println(pitches);
        //데이터가 이미 존재할 경우 데이터 이전 가능
        String [] data = {"128","129","130"};
        ArrayList<String> pitches = new ArrayList<>(Arrays.asList(data));
        String result = String.join(",",pitches);
        System.out.println(result);
        //join을 통해 배열을 문자열로!
    }
}
