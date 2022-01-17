package jump2java;

public class HouseDog extends Dog{
	public HouseDog(String name) {
		this.setName(name);
	}
	public HouseDog(int a) {
		if (a == 1) {
			this.setName("yorkshire");
		}
		else if (a == 2) {
			this.setName("bulldog");
		}
	}
	public void sleep() {
		System.out.println(this.name+" zzz in the house");
	}
	public void sleep(int hour) {
		System.out.println(this.name+" zzz in hour for "+hour);
	}
	
	public static void main(String[] args) {
		HouseDog dog = new HouseDog("HAPPY");
		HouseDog dog_1 = new HouseDog(2);
		System.out.println(dog.name);
		System.out.println(dog_1.name);
	}

}
