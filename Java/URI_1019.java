import java.util.Scanner;

public class URI_1019 {

    public static void main(String[] args) {
        Scanner date = new Scanner(System.in);
        int time = date.nextInt();
        int hour, min, sec, aux;
        hour = time/3600;
        aux = time%3600;
        min = aux/60;
        aux = aux%60;
        sec = aux;
    System.out.println(hour+":"+min+":"+sec);
    }
    
}
