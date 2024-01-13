import java.util.*;
public class pattern4 {
    public static void main(String args[])
    {
        int i,j;
        System.out.println("Enter a number");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=i;j++)
            {
                System.out.print((i+j)%2);
            }
            System.out.println();
        }
    }
}