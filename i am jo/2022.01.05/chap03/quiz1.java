/*
  ����ڿ��� �ϳ��� �Ǽ��� �Է����� �޾� ����, �ݿø�, �ø��� ����� ���
	ex1) �ϳ��� �Ǽ��� �Է��ϼ��� : 3.6
		 ����: 3
		 �ݿø�:4
		 �ø�:4
 */

/*
 double num = 3.6;
 
 System.out.println("����: " + (int)num);
 System.out.println("�ݿø�: " + (int)(num + 0.5));
 
 if(num == int(num)) {
 	System.out.println("�ø�: " + (int)num);
 	}
 	else{
 		System.out.println("�ø�: " + (int)(num + 1));
 		}
 */

package chap03;

import java.util.Scanner;

public class quiz1 {
	public static void main(String args[]) {
		double n ;
		Scanner sc = new Scanner(System.in);
		
		System.out.print("�ϳ��� �Ǽ��� �Է��ϼ���: ");
		n = sc.nextInt();
		sc.close();
		
		if (n-1 < n < n+1 )
		System.out.println("����: n");
		
		else if (n+0.5 <= n < n+1 )
		System.out.println("�ݿø�: n+1");
		
		else (n-1+0.1< n < n+1)
		System.out.println("�ø�: n+1");
	
		}
	}