public class paging {
    static int getTotalPage(int m,int n){
        return (m-1)/n +1;
    }

    public static void main(String[] args) {
        System.out.println(getTotalPage(5, 10));  // 1 출력
        System.out.println(getTotalPage(15, 10));  // 2 출력
        System.out.println(getTotalPage(25, 10));  // 3 출력
        System.out.println(getTotalPage(30, 10));
    }
}
