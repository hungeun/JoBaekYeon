/*
  사용자에게 하나의 실수를 입력으로 받아 버림, 반올림, 올림의 결과를 출력
	ex1) 하나의 실수를 입력하세요 : 3.6
		 버림: 3
		 반올림:4
		 올림:4
 */

/*
 double num = 3.6;
 
 System.out.println("버림: " + (int)num);
 System.out.println("반올림: " + (int)(num + 0.5));
 
 if(num == int(num)) {
 	System.out.println("올림: " + (int)num);
 	}
 	else{
 		System.out.println("올림: " + (int)(num + 1));
 		}
 */

package chap03;

import java.util.Scanner;

public class quiz1 {
	public static void main(String args[]) {
		double n ;
		Scanner sc = new Scanner(System.in);
		
		System.out.print("하나의 실수를 입력하세요: ");
		n = sc.nextInt();
		sc.close();
		
		if (n-1 < n < n+1 )
		System.out.println("버림: n");
		
		else if (n+0.5 <= n < n+1 )
		System.out.println("반올림: n+1");
		
		else (n-1+0.1< n < n+1)
		System.out.println("올림: n+1");
	
		}
	}