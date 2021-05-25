import java.util.*;
class pattern1
{
    public static void main(String args[])
    {
        int i,j;

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number");
        int n = sc.nextInt();

        int mid = n/2;
        
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(mid>j && j!=0 && i < mid)
                {
                    System.out.print(" ");
                }
                else if(i!=0 && j>mid && i<mid)
                {
                    System.out.print(" ");
                }
                else if(i>mid && j>mid && j<n-1)
                {
                    System.out.print(" ");
                }
                else if(j<mid && i>mid && i!= n-1)
                {
                    System.out.print(" ");
                }
                else
                {
                    System.out.print("*");
                }
            }
            System.out.println();
        }
    }
}