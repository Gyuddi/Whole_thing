public class Formating {
    public static void main(String[] args) {
        System.out.println(String.format("I eat %d apples",3));
        // %d - 숫자 포멧 코드
        System.out.println(String.format("I eat %s apples","five"));
        // %s - 문자열 포멧 코드
        // %s는 자동으로 % 뒤에 있는 값을 문자열로 바꾼다.
        String a = "fine";
        int b = 5;
        System.out.println(String.format("I eat %s %d apples",a,b));
    }
}
