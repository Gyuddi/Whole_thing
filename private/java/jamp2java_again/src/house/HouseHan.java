package house;

public class HouseHan {
    private String  name = "han gyu hyun";
    //private 접근 제어자 - 해당 클래스에서만 접근 가능.
    String lastname = "han";
    //default 접근 제어자 - 패키지가 동일하면 접근 가능.
    protected String firstname = "hyun";
    //protected 접근 제어자 - 상속받은 패키지에서 접근 가능.

    public String midname = "gyu";
    //public 접근 제어자 - 어떤 클래서에서도 접근 가능.
    public String getName(){
        return this.firstname;
    }
}
