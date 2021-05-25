import java.util.*;
class patternPascal
{
    public static void main(String[]args)
    {
        int a=1,b=1,sum=0; 
        Scanner sc=new Scanner(System.in);
        System.out.println("enter n");
        int n=sc.nextInt();
        int t=1;
        for(int x=n;x>=1;x--)
        {
            for(int y=1;y<=n;y++)
            {
                if((x+y)>n+1)
                {
                    System.out.print(" ");
                }
            }
            for(int y=1;y<=t;y++)
            {
                if(y<n/2)
                {
                    System.out.print(a+sum);
                }
                else if(y>n/2)
                {
                    System.out.print(b+sum);
                }
                else
                {
                    sum=a+b;
                    System.out.print(sum);
                }
                
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