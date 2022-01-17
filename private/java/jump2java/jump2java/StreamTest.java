package jump2java;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class StreamTest {
    public static void main(String[] args) throws Exception {
        InputStream in = System.in;
        InputStreamReader reader = new InputStreamReader(in);
        BufferedReader bReader = new BufferedReader(reader);
        String a = bReader.readLine();
        
        System.out.println(a);
    }
}