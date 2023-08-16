import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) {
        Scanner date = new Scanner(System.in);
        String name = date.nextLine();
        double salary = date.nextDouble();
        double sell = date.nextDouble();
        System.out.printf("TOTAL = R$ %.2f\n", salary+(sell*0.15));
    }

}
