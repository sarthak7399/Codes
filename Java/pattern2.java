import java.util.*;
class pattern2
{
    public static void main(String[]args)
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter n");
        int n=sc.nextInt();
        int t=1;
        for(int x=n;x>=1;x--)
        {
            for(int y=1;y<=n;y++)
            {
                if((x+y)>=n+1)
                {
                    System.out.print("*");
                }
            }
            for(int y=1;y<=t;y++)
            {
                System.out.print(y);
                if(y<t)
                {
                    System.out.print(" ");
                }
            }
            System.out.println();
            t++;
        }
    }
}