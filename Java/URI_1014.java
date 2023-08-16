import java.util.Scanner;

public class URI_1014 {
    
    public static void main(String[] args) {

        Scanner date = new Scanner(System.in);
        int dist = date.nextInt();
        double med = date.nextDouble();
        System.out.printf("%.3f km/l\n", dist/med);
    }

}
