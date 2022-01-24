public class If {
    public static void main(String[] args) {
        String str = "";
        int x = 3;
        int y = 5;
        if(x>y){
            System.out.println("bigger");
        }
        else if (x==y){
            System.out.println("same");
        }
        else {
            System.out.println("smaller");
        }
        switch (x){
            case 1:str = "one";
            case 2:str = "two";
            case 3:str = "three";
        }
        System.out.println(str);
    }

}
