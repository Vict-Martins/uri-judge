import java.util.Scanner;

public class URI_1005 {

    public static void main(String[] args) {

        Scanner date = new Scanner(System.in);
        double A = date.nextDouble();
        double B = date.nextDouble();
        double C = date.nextDouble();
        double MEDIA = ((A*2)+(B*3)+(C*5))/10;
        System.out.printf("MEDIA = %.1f\n", MEDIA);

    }

}
