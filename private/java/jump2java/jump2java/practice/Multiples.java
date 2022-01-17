package jump2java.practice;

public class Multiples {
	
	boolean[] table = new boolean[5000];
	public boolean[] retable() {
		for(int i = 0;i<5000;i++) {
			int a =i;
			int sum = 0;
			sum+=a;
			while(true) {
				sum +=(a%10);
				a = a/10;
				if(a == 0) {
					break;
				}
			}
			if(sum>=5000) {
				break;
			}
			table[sum] = true;
		}
		return table;
	}
	public int total() {
		this.retable();
		int total = 0;
		for (int i = 0;i<5000;i++) {
			if(table[i] == false) {
				total+=i;
			}
		}
		return total;
	}
	public static void main(String[] args) {
		Multiples multiples = new Multiples();
		System.out.println(multiples.total());
		}


}
