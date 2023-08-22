import java.util.Scanner;

public class URI_1038 {

    public static void main(String[] args) {
        Scanner date = new Scanner(System.in);
        int A, B;
        A = date.nextInt();
        B = date.nextInt();
        switch(A) {
            case 1:
                System.out.printf("Total: R$ %.2f\n",(4.00*B));
                break;
            case 2:
                System.out.printf("Total: R$ %.2f\n", (4.50*B));
                break;
            case 3:
                System.out.printf("Total: R$ %.2f\n", (5.00*B));
                break;
            case 4:
                System.out.printf("Total: R$ %.2f\n", (2.00*B));
                break;
            case 5:
                System.out.printf("Total: R$ %.2f\n", (1.50*B));
                break;
        }

    }

}