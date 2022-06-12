import java.util.*;

public class Cryptography
{
    public static void main(String args[])
    {
        String a ="abcdefghijklmnopqrstuvwxyz .,?1234567890";     
        String c ="#vwi%ptsdfqn[u<joygl^xazem*c|>!@r$hb&+}k";
        String ss="";
        
        Scanner obj = new Scanner(System.in);
        System.out.print("1.Encryption\n2.Decryption\nEnter your choice : ");
        int cs =obj.nextInt();

        if(cs!=1 && cs!=2)
        {
            System.out.println("INVALID INPUT");
            System.exit(0);
        }        

        obj.nextLine();
        System.out.print("Enter the message : ");
        String s = obj.nextLine();
        s=s.toLowerCase();
        s=s.trim();  
        
        if(cs==1)
        {
            System.out.print("THE ENCRYPTED MESSAGE : ");
            for(int i=0; i<s.length();i++)
            {
                ss+=c.charAt(a.indexOf(s.charAt(i)));
            }
            System.out.println(ss);
        }

        else
        {
            System.out.print("THE DECRYPTED MESSAGE : ");
            for(int i=0; i<s.length();i++)
            {
                ss+=a.charAt(c.indexOf(s.charAt(i)));
            }
            System.out.println(ss);
        }
        
    }
}
