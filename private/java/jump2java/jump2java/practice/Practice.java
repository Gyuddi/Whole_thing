package jump2java.practice;
import java.util.Scanner;


public class Practice {
	int num;
	public void setNum() {
		int number;
		Scanner sc = new Scanner(System.in);
		number = sc.nextInt();
		sc.close(); 
		this.num = number;
	}
	public int mul(int a) {
		return num * a;
	}
	public int[] cac_return() {
		int[] result = new int[9];
		for (int i = 0; i<9;i++) {
			result[i] = this.mul(i+1);
		}
		return result;
	}
	public String toString() {
		int[] result = this.cac_return();
		StringBuffer sb = new StringBuffer();
		for(int i = 0; i<result.length;i++){
			sb.append(result[i]);
			if(i == result.length-1) {
				break;
			}
			sb.append(",");
		}
		return sb.toString();
	}
	
	public static void main(String[] args) {
		Practice practice = new Practice();
		practice.setNum();
		System.out.println(practice);
	}
}
