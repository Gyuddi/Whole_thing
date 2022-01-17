package jump2java;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.FileReader;

public class FileRead {
	public static void main(String[] args) throws IOException {
		BufferedReader bReader = new BufferedReader(new FileReader("c:/out.txt"));
		while (true) {
			String line = bReader.readLine();
			if(line == null) break;
			System.out.println(line);
		}
		bReader.close();
	}
}
