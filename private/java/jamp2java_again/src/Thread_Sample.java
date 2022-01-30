public class Thread_Sample extends Thread {
    int seq;
    public  Thread_Sample(int seq){
        this.seq = seq;
    }
    public void run(){
        System.out.println(this.seq + "thread start.");
        try {
            Thread.sleep(1000);
        }
        catch (java.lang.Exception e){
        }
        System.out.println(this.seq+"thread end.");
    }

    public static void main(String[] args) {
        for(int i = 0;i<10;i++){
            Thread t = new Thread_Sample(i);
            t.start();
        }
        System.out.println("main end");
    }
}
