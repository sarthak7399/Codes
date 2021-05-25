import java.util.*;
class patternbox
{
    public static void main(String args[])
    {
        int i,j,k,l,n1,n2; 
        int ar[][];
        l=0;k=0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number");
        int n = sc.nextInt();
        
        ar = new int[n*2][n*2];
        n2=n*2;
        n1=n*2;
        while(l<n1 && k<n2)
        {
            for(i = l;i < n2-1;i++)
            {
                ar[k][i]=n;
            }
            k++;
            for(i = k;i<n1-1;i++)
            {
                ar[i][n2-2]=n;
            }
            n2--;
            if (k<n1)
            {
                for (i = n2 - 1; i >= l; --i) 
                {
                    ar[n1 - 2][i]=n;
                }
                n1--;
            }
            if (l < n2)
            {
                for (i = n1 - 1; i >= k; --i) 
                {
                    ar[i][l]=n;
                }
                l++;
            }
            n--;
        }
        for(i = 0; i < ar.length-1; i++)
        {
            for(j = 0; j < ar.length-1; j++)
            {
                System.out.print(ar[i][j]+ " ");
            }
            System.out.println();
        }
    }
}