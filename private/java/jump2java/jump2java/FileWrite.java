package jump2java;
import java.io.FileWriter;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintWriter;

//public class FileWrite {
//    public static void main(String[] args) throws IOException {
//        FileOutputStream output = new FileOutputStream("c:/out.txt");
//        for (int i = 1;i<11;i++) {
//        	String dataString = i+" ���� �� �Դϴ�.\r\n";
//        	output.write(dataString.getBytes());
//        }
//        output.close();
//    }
//}

public class FileWrite {
    public static void main(String[] args) throws IOException {
        PrintWriter pw = new PrintWriter("c:/out.txt");
        for(int i=1; i<11; i++) {
            String data = i+" ��° ���Դϴ�.";
            pw.println(data);
        }
        pw.close();
        
        PrintWriter pw2 = new PrintWriter(new FileWriter("c:/out.txt",true));
        for (int i = 11; i<21; i++) {
        	String data = i+" ��° ���Դϴ�.";
        	pw2.println(data);
        }
        pw2.close();
    }
}