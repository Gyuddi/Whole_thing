import java.util.*;

public class practice1 {
    enum CoffeeType{
        AMERICANO,
        ICE_AMERICANO,
        CAFE_LATTE
    };
    static void printCoffeePrice(CoffeeType type) {
        HashMap<CoffeeType, Integer> priceMap = new HashMap<>();
        priceMap.put(CoffeeType.AMERICANO, 3000);  // 1: 아메리카노
        priceMap.put(CoffeeType.ICE_AMERICANO, 4000);  // 2: 아이스 아메리카노
        priceMap.put(CoffeeType.CAFE_LATTE, 5000);  // 3: 카페라떼
        int price = priceMap.get(type);
        System.out.println(String.format("가격은 %d원 입니다.", price));
    }
    public static void main(String[] args) {
        //q3
//        String num = "881120-1068234";
//        System.out.println(num.substring(0,6));
//        System.out.println(num.substring(7,14));
        //q4
//        String num = "881120-1068234";
//        System.out.println(num.charAt(7));
        //q5
//        String a = "a:b:c:d";
//        System.out.println(a.replaceAll(":","#"));
        //q6
//        ArrayList<Integer> myList = new ArrayList<>(Arrays.asList(1, 3, 5, 4, 2));
//        myList.sort(Comparator.reverseOrder());
//        System.out.println(myList);
        //q7
//        ArrayList<String> myList = new ArrayList<>(Arrays.asList("Life", "is", "too", "short"));
//        String result = String.join(" ",myList);
//        System.out.println(result);
        //q8
//        HashMap<String, Integer> grade = new HashMap<>();
//        grade.put("A", 90);
//        grade.put("B", 80);
//        grade.put("C", 70);
//        int a = grade.remove("B");
//        System.out.println(String.format("%s가 추출되었습니다.",a));
//        System.out.println(grade);
        //q9
//        ArrayList<Integer> numbers = new ArrayList<>(Arrays.asList(1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5));
//        HashSet<Integer> set_num = new HashSet<>(numbers);
//        System.out.println(set_num);
        //q10
        printCoffeePrice(CoffeeType.AMERICANO);
    }
}
