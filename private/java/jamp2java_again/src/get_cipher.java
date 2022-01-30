<<<<<<< HEAD
public class get_cipher {
    static void get_digit(int m){
        int count = 0;
        while (m >0){
            m = m/10;
            count+=1;
        }
        System.out.println(String.format("자릿수는 %s 입니다.",count));
    }

    public static void main(String[] args) {
        get_digit(3);
        get_digit(25);
        get_digit(333);
        get_digit(7876);
    }
}
=======
public class get_cipher {
    static void get_digit(int m){
        int count = 0;
        while (m >0){
            m = m/10;
            count+=1;
        }
        System.out.println(String.format("자릿수는 %s 입니다.",count));
    }

    public static void main(String[] args) {
        get_digit(3);
        get_digit(25);
        get_digit(333);
        get_digit(7876);
    }
}
>>>>>>> 58110c72042666d64e8117b99a8afe7db8511558
