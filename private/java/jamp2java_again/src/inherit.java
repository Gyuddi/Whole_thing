//class Animal{
//    String name;
//    void setName(String name){
//        this.name = name;
//    }
//}
class Dog extends Animal{
    //디폴트 생성자.
    Dog(){}
    void sleep(){
        System.out.println(this.name + "  zzzzz");
    }
}

class HouseDog extends Dog{
    //생성자.
    HouseDog(){}
    HouseDog(String name){
        this.setName(name);
    }
    //생성자 오버로딩.
        HouseDog(int type){
        if (type == 1){
            this.setName("Yorkshire");
        }
        else if (type == 2){
            this.setName("Bulldog");
        }
    }
    //메소드 오버라이딩 - 부모클래스의 메소드를 자식클래스가 동일한 형태로 또다시 구현
    void sleep(){
        System.out.println(this.name+"  zzzzz in house");
    }
    //메소드 오버로딩 - 입력항목이 다른 경우 동일한 이름의 메소드
    void sleep(int hour){
        System.out.println(this.name+"  zzzzz in house for "+hour+"hours.");
    }
}

public class inherit {
    public static void main(String[] args) {
        HouseDog dog = new HouseDog(2);
        System.out.println(dog.name);
        dog.sleep();
        dog.sleep(8);
        //Dog dog = new HouseDog();
        //is-a 관계.
    }
}
