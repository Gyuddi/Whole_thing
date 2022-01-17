package jump2java;

public class Bouncer {
	public void barkAnimal(Barkable barkable) {
		barkable.bark();
	}
		
	public static void main(String[] args) {
		Tiger tiger = new Tiger();
		Lion lion = new Lion();
		
		Bouncer bouncer = new Bouncer();
		bouncer.barkAnimal(tiger);
		bouncer.barkAnimal(lion);
	}
}