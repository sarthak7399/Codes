import java.util.*;
class patternSpiral
{
    public static void main(String args[])
    {
        int i,j,k,l,n1,n2; 
        String ar[][];
        l=0;k=0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number");
        int n = sc.nextInt();
        /*
        ar = new String[n*2][n*2];
        n2=n*2;
        n1=n*2;
        while(l<n1 && k<n2)
        {
            for(i = l;i < n2-1;i++)
            {
                //ar[k][i]="*";
                if(l%2!=0)
                    ar[k][i]=" ";
                else
                    ar[k][i]="*";
            }
            k++;
            for(i = k;i<n1-1;i++)
            {
                //ar[i][n2-2]="#";
                if(k%2!=0)
                    ar[i][n2-2]="*";
                else
                    ar[i][n2-2]=" ";
            }
            n2--;
            if (k<n1)
            {
                for (i = n2 - 1; i >= l; --i) 
                {
                    //ar[n1 - 2][i]="$";
                    if(l%2!=0)
                        ar[n1-2][i]=" ";
                    else
                        ar[n1-2][i]="*";
                }
                n1--;
            }
            if (l < n2)
            {
                for (i = n1 - 1; i>=k; --i) 
                {
                    if(k%2!=0 && i!=k)
                        ar[i][l]="*";
                    else
                        ar[i][l]=" ";
                }
                l++;
            }
            n--;
        }
        for(i = 0; i < ar.length-1; i++)
        {
            for(j = 0; j < ar.length-1; j++)
            {
                if(ar[i][j]==null)
                    ar[i][j]=" ";
                System.out.print(ar[i][j]+ " ");
            }
            System.out.println();
        }*/
        /*ar = new String[n*2][n*2];
        n2=n*2;
        n1=n*2;
        while(l<n1 && k<n2)
        {
            for(i = l;i < n2;i++)
            {
                //ar[k][i]="*";
                if(l%2!=0)
                    ar[k][i]=" ";
                else
                    ar[k][i]="*";
            }
            k++;
            for(i = k;i<=n1-1;i++)
            {
                //ar[i][n2-2]="#";
                if(k%2!=0)
                    ar[i][n2-1]="&";
                else
                    ar[i][n2-1]=" ";
            }
            n2--;
            if (k<n1)
            {
                for (i = n2 - 1; i >= l; --i) 
                {
                    //ar[n1 - 2][i]="$";
                    if(l%2!=0)
                        ar[n1-1][i]=" ";
                    else
                        ar[n1-1][i]="$";
                }
                n1--;
            }
            if (l < n2)
            {
                for (i = n1; i>= k; --i) 
                {
                    if(k%2!=0 && i!=k)
                        ar[i][l]="#";
                    else
                    {
                        if(i==k && i%2==0)
                        {
                            ar[i][l]="*";
                        }
                        else
                            ar[i][l]=" ";
                    }
                }
                l++;
            }
            n--;
        }*/
        ar = new String[n*2][n*2];
        n2=n;
        n1=n;
        while(l<n1 && k<n2)
        {
            for(i = l;i < n2;i++)
            {
                //ar[k][i]="*";
                if(l%2!=0)
                    ar[k][i]=" ";
                else
                    ar[k][i]="*";
            }
            k++;
            for(i = k;i<=n1-1;i++)
            {
                //ar[i][n2-2]="#";
                if(k%2!=0)
                    ar[i][n2-1]="*";
                else
                    ar[i][n2-1]=" ";
            }
            n2--;
            if (k<n1)
            {
                for (i = n2 - 1; i >= l; --i) 
                {
                    //ar[n1 - 2][i]="$";
                    if(l%2!=0)
                        ar[n1-1][i]=" ";
                    else
                        ar[n1-1][i]="*";
                }
                n1--;
            }
            if (l < n2)
            {
                for (i = n1; i>= k; --i) 
                {
                    if(k%2!=0 && i!=k)
                        ar[i][l]="*";
                    else
                    {
                        if(i==k && i%2==0)
                        {
                            ar[i][l]="*";
                        }
                        else
                            ar[i][l]=" ";
                    }
                }
                l++;
            }
            n--;
        }
        for(i = 0; i <= ar.length-1; i++)
        {
            for(j = 0; j <= ar.length-1; j++)
            {
                if(ar[i][j]==null)
                    ar[i][j]=" ";
                System.out.print(ar[i][j]+ " ");
            }
            System.out.println();
        }
    }
}