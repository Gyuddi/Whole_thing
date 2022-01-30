//class FoolException extends RuntimeException {
//}
//public class exception_sample {
//    public void sayNick(String nick) {
//        if("fool".equals(nick)) {
//            throw new RuntimeException();
//            //예외 강제 발생!
//            //+RuntimeException은 실행시 발생하는 예외이고 Exception은 컴파일시 발생하는 예외이다.
//        }
//        System.out.println("당신의 별명은 "+nick+" 입니다.");
//    }
//
//    public static void main(String[] args) {
//        exception_sample sample = new exception_sample();
//        sample.sayNick("fool");
//        sample.sayNick("genious");
//    }
//}
class FoolException extends java.lang.Exception {
}
public class exception_sample {
    public void sayNick(String nick) throws FoolException {
            if ("fool".equals(nick)) {
                throw new FoolException();
                //Exception은 컴파일 오류이기에 감지 가능하다. so, try문에 감싸서 사용하자.
            }
            System.out.println("당신의 별명은 " + nick + " 입니다.");
    }
    public static void main (String[]args){
        exception_sample sample = new exception_sample();
        try{
            sample.sayNick("fool");
            sample.sayNick("genious");
        }
        catch (FoolException e){
            System.out.println("FoolException이 발생했습니다.");
        }

    }
}


