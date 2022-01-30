import java.util.ArrayList;

class HeavyWork extends Thread{
    String name;

    HeavyWork(String name) {
        this.name = name;
    }
    public void run(){
        work();
    }
    public void work() {
        for (int i = 0; i < 5; i++) {
            try {
                Thread.sleep(100);  // 0.1 초 대기한다.
            } catch (java.lang.Exception e) {
            }
        }
        System.out.printf("%s done.\n", this.name);
    }
}

public class Thread_practice {
    public static void main(String[] args) {
        ArrayList<Thread> threads = new ArrayList<>();
        long start = System.currentTimeMillis();
        for (int i = 1; i < 5; i++) {
            Thread w = new HeavyWork("w" + i);
            threads.add(w);
            w.start();

        }
        for(int i = 0;i<threads.size();i++){
            Thread t = threads.get(i);
            try{
                t.join();
            }catch (java.lang.Exception e){}
        }
        long end = System.currentTimeMillis();
        System.out.printf("elapsed time:%s ms\n", end - start);
    }
}