import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Scanner;


public class In_output {
//InputStream - byte
//InputStreamReader - character
//BufferedReader - String

//    public static void main(String[] args) throws IOException {
//        InputStream in = System.in;
//        InputStreamReader reader = new InputStreamReader(in);
//        BufferedReader br = new BufferedReader(reader);
//        String a = br.readLine();
//        System.out.println(a);
//    }
//scanner는 단어,라인,정수를 콘솔 입력 가능
// next - 단어
//nextLine - 라인
//nextInt - 정수
public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println(sc.next());
    //err은 sout과 동일하지만 에러 출력 가능.
    System.err.println("에러 출력 가능");
}
}
