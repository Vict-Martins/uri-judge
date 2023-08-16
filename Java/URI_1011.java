import java.util.Scanner;

public class URI_1011 {
    
    public static void main(String[] args) {
        Scanner date = new Scanner(System.in);
        int raio = date.nextInt();
        Double volume = (4/3.0)*3.14159*Math.pow(raio, 3);
        System.out.printf("VOLUME = %.3f\n", volume);
    }

}