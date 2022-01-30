<<<<<<< HEAD
import java.util.ArrayList;
interface Mineral{
    int get_value();
}

class Gold implements Mineral {
    public int get_value(){
        return 100;
    }
}

class Silver implements Mineral{
    public int get_value(){
        return 90;
    }
}

class Bronze implements Mineral{
    public int get_value(){
        return 80;
    }
}

class MineralCalculator {
    int value = 0;

    public void add(Mineral min){
        this.value += min.get_value();
    }
    public int getValue() {
        return this.value;
    }
}

class Calculator {
    int value;

    Calculator() {
        this.value = 0;
    }

    void add(int val) {
        this.value += val;
    }

    int getValue() {
        return this.value;
    }
    boolean isOdd(){
        if(this.value%2 == 0){
            return true;
        }
        else {
            return false;
        }
    }
    int avg(int[] data){
        int total = 0;
        for(int num:data){
            total+=num;
        }
        int answer = total/data.length;
        return answer;
    }
    int avg(ArrayList<Integer> data){
        int total = 0;
        for(int num:data){
            total+=num;
        }
        int answer = total/data.size();
        return answer;
    }
}
class UpgradeCalculator extends Calculator {
    void minus(int val){
        this.value -= val;
    }
}
class MaxLimitCalculator extends UpgradeCalculator{
    void add(int val){
        this.value += val;
        if(this.value > 100){
            System.out.println("100을 초과하였습니다.");
            this.value -= val;
        }
    }
}

public class practice3 {
    public static void main(String[] args) {
        MineralCalculator cal = new MineralCalculator();
        cal.add(new Gold());
        cal.add(new Silver());
        cal.add(new Bronze());
        System.out.println(cal.getValue());
    }
=======
import java.util.ArrayList;
interface Mineral{
    int get_value();
}

class Gold implements Mineral {
    public int get_value(){
        return 100;
    }
}

class Silver implements Mineral{
    public int get_value(){
        return 90;
    }
}

class Bronze implements Mineral{
    public int get_value(){
        return 80;
    }
}

class MineralCalculator {
    int value = 0;

    public void add(Mineral min){
        this.value += min.get_value();
    }
    public int getValue() {
        return this.value;
    }
}

class Calculator {
    int value;

    Calculator() {
        this.value = 0;
    }

    void add(int val) {
        this.value += val;
    }

    int getValue() {
        return this.value;
    }
    boolean isOdd(){
        if(this.value%2 == 0){
            return true;
        }
        else {
            return false;
        }
    }
    int avg(int[] data){
        int total = 0;
        for(int num:data){
            total+=num;
        }
        int answer = total/data.length;
        return answer;
    }
    int avg(ArrayList<Integer> data){
        int total = 0;
        for(int num:data){
            total+=num;
        }
        int answer = total/data.size();
        return answer;
    }
}
class UpgradeCalculator extends Calculator {
    void minus(int val){
        this.value -= val;
    }
}
class MaxLimitCalculator extends UpgradeCalculator{
    void add(int val){
        this.value += val;
        if(this.value > 100){
            System.out.println("100을 초과하였습니다.");
            this.value -= val;
        }
    }
}

public class practice3 {
    public static void main(String[] args) {
        MineralCalculator cal = new MineralCalculator();
        cal.add(new Gold());
        cal.add(new Silver());
        cal.add(new Bronze());
        System.out.println(cal.getValue());
    }
>>>>>>> 58110c72042666d64e8117b99a8afe7db8511558
}