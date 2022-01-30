<<<<<<< HEAD
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;


//스트림 사용 전.
//public class stream {
//    public int[] change(int[] a){
//        ArrayList<Integer> blist = new ArrayList<>();
//        ArrayList<Integer> alist = new ArrayList<>();
//        for(int i:a){
//            blist.add(i);
//        }
//        for(int num:blist){
//            if(num%2 == 0){
//                alist.add(num);
//            }
//        }
//        HashSet<Integer> hset = new HashSet<>(alist);
//        System.out.println(hset);
//        ArrayList<Integer> new_list = new ArrayList<>(hset);
//        System.out.println(new_list);
//        new_list.sort(Comparator.reverseOrder());
//        int result [] = new int[new_list.size()];
//        for(int i = 0;i< new_list.size();i++){
//            result[i] = new_list.get(i);
//        }
//        return result;
//    }
//    public static void main(String[] args) {
//        int[] data = {5,6,4,2,3,1,1,2,2,4,8};
//        stream s = new stream();
//        int [] answer = s.change(data);
//        for (int a:answer){
//            System.out.println(a);
//        }
//    }
//}
//스트림 사용 후.
public class stream {
    public static void main(String[] args) {
        int [] data = {5, 6, 4, 2, 3, 1, 1, 2, 2, 4, 8};
        int [] result = Arrays.stream(data)
                .boxed()
                .filter((a) -> a%2==0)
                .distinct()
                .sorted(Comparator.reverseOrder())
                .mapToInt(Integer::intValue)
                .toArray()
                ;
        for (int a:result){
            System.out.println(a);
        }
    }
}
=======
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;


//스트림 사용 전.
//public class stream {
//    public int[] change(int[] a){
//        ArrayList<Integer> blist = new ArrayList<>();
//        ArrayList<Integer> alist = new ArrayList<>();
//        for(int i:a){
//            blist.add(i);
//        }
//        for(int num:blist){
//            if(num%2 == 0){
//                alist.add(num);
//            }
//        }
//        HashSet<Integer> hset = new HashSet<>(alist);
//        System.out.println(hset);
//        ArrayList<Integer> new_list = new ArrayList<>(hset);
//        System.out.println(new_list);
//        new_list.sort(Comparator.reverseOrder());
//        int result [] = new int[new_list.size()];
//        for(int i = 0;i< new_list.size();i++){
//            result[i] = new_list.get(i);
//        }
//        return result;
//    }
//    public static void main(String[] args) {
//        int[] data = {5,6,4,2,3,1,1,2,2,4,8};
//        stream s = new stream();
//        int [] answer = s.change(data);
//        for (int a:answer){
//            System.out.println(a);
//        }
//    }
//}
//스트림 사용 후.
public class stream {
    public static void main(String[] args) {
        int [] data = {5, 6, 4, 2, 3, 1, 1, 2, 2, 4, 8};
        int [] result = Arrays.stream(data)
                .boxed()
                .filter((a) -> a%2==0)
                .distinct()
                .sorted(Comparator.reverseOrder())
                .mapToInt(Integer::intValue)
                .toArray()
                ;
        for (int a:result){
            System.out.println(a);
        }
    }
}
>>>>>>> 58110c72042666d64e8117b99a8afe7db8511558
