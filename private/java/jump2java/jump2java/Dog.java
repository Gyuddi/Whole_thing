package jump2java;

public class Dog extends Animal{
	public void sleep() {
		System.out.println(this.name+"ZZZ");
	}
	
	public static void main(String[] args) {
		Dog dog = new Dog();
		dog.setName("Happy");
		System.out.println(dog.name);
		dog.sleep();
	}
}