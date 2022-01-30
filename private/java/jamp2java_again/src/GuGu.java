public class GuGu {
    //입력 - 정수 자료형 1개 (int n)
    //출력 - 없음 (void)
//    public void dan(int n) {
//        System.out.println(n*1);
//        System.out.println(n*2);
//        System.out.println(n*3);
//        System.out.println(n*4);
//        System.out.println(n*5);
//        System.out.println(n*6);
//        System.out.println(n*7);
//        System.out.println(n*8);
//        System.out.println(n*9);
//    }
    //static 메소드 - 객체 생성 없이 단독 호출 가능
    public void dan(int n){
        for (int i = 1;i<10;i++){
            System.out.println(i*n);;
        }
    }
    public static void main(String[] args) {
        GuGu gugu = new GuGu();
        for (int i = 1; i < 10; i++) {
            gugu.dan(i);
        }
    }
}
