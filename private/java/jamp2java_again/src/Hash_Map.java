import java.util.HashMap;
import java.util.HashSet;

public class Hash_Map {
    public static void main(String[] args) {
        HashMap<String,String> map = new HashMap<>();
        map.put("people","사람");
        map.put("baseball","야구");
        System.out.println(map);
        System.out.println(map.get("people"));
        //튜플과 동일하다.
        HashSet<Integer> s = new HashSet<>();
        s.add(5);
        s.add(8);
        System.out.println(s);
        //set과 동일하다.
    }
}
