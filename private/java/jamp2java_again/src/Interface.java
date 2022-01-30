interface Predator{
    String getFood();
    default void printFood(){
        System.out.printf("my food is%s\n",getFood());
    }
    int LEG_COUNT = 4;
    static int speed(){
        return LEG_COUNT*30;
    }
}
interface  Barkable{
    void bark();
}
//Predator의 객체와 Barkable의 객체는 서로 사용 가능한 매소드가 다르다. so
interface BarkablePredator extends Predator,Barkable{
}


class Animal {
    String name;
    void setName(String name) {
        this.name = name;
    }
}

class Tiger extends Animal implements BarkablePredator{
    @Override
    public String getFood() {
        return "apple";
    }

    @Override
    public void bark() {
        System.out.println("어흥");
    }
}

class Lion extends Animal implements BarkablePredator{
    @Override
    public String getFood() {
        return "banana";
    }

    @Override
    public void bark() {
        System.out.println("으르렁");
    }
}

class ZooKeeper {
    void feed(Predator predator) {
        System.out.println("feed "+predator.getFood());
    }
}
class Bouncer{
    void barkAnimal(Barkable animal){
        animal.bark();
    }
}

public class Interface {
    public static void main(String[] args) {
        ZooKeeper zooKeeper = new ZooKeeper();
        Tiger tiger = new Tiger();
        Lion lion = new Lion();
        tiger.printFood();

        zooKeeper.feed(tiger);
        zooKeeper.feed(lion);
        Bouncer bouncer = new Bouncer();
        bouncer.barkAnimal(tiger);
        bouncer.barkAnimal(lion);
    }
}
