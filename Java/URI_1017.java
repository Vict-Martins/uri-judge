import java.util.Scanner;

public class URI_1017 {
    
    public static void main(String[] args) {
        Scanner date = new Scanner(System.in);
        int time = date.nextInt();
        int median = date.nextInt();
        double result = (double)(time*median)/12;
        System.out.printf("%.3f\n", result);
    }
}
