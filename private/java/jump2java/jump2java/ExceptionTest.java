package jump2java;

//public class ExceptionTest {
//	public static void main(String[] args) {
//		int c;
//		try {
//			c = 4/0;
//		}
//		catch (ArithmeticException e) {
//			c = -1;System.out.println(c);
//			
//		}
//	}
//}
//public class ExceptionTest{
//	public void shouldBeRun() {
//		System.out.println("�����ߴ�.");
//	}
//	public static void main(String[] args) {
//		ExceptionTest exceptionTest = new ExceptionTest();
//		int c;
//		try {
//			c = 4/0;
//		}
//		catch(ArithmeticException e) {
//			c=-1;
//			System.out.println(c);
//		}
//		finally {
//			exceptionTest.shouldBeRun();
//		}
//	}
//}
public class ExceptionTest {
	public void sayNick(String nick) throws FoolException {
	    if("fool".equals(nick)) {
	        throw new FoolException();
	    }
	    System.out.println("����� ������ "+nick+" �Դϴ�.");
	}

    public static void main(String[] args) {
        ExceptionTest test = new ExceptionTest();
        try {
	        test.sayNick("fool");
	        test.sayNick("genious");
	        }
        catch (FoolException e) {
        	System.err.println("FoolEXception�� �߻��߽��ϴ�.");
        }
    }
}

