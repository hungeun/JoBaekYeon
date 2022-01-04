package chap02Exam;

import java.util.Scanner;

public class EX02 {
	public static void main(String arg[]) {
		
		int a, b, c, d, e, f, g, h, i;
		
		Scanner sc = new Scanner(System.in);

		System.out.print("상품의 물건 값을 입력하세요");
		a = sc.nextInt();
		
		sc.close();
		 b = 10000;
		 c = b - a;
		 d = c/5000;	
		 e = (c-(d*5000))/1000;
		 f = (c-((e*1000)+(d*5000)))/500;
		 g = (c-((e*1000)+(d*5000)+(f*500)))/100;
		 h = (c-((e*1000)+(d*5000)+(f*500)+(g*100)))/50;
		 i = (c-((e*1000)+(d*5000)+(f*500)+(g*100)+(h*50)))/10;		 
				 
		System.out.println("거스름돈은" + c + "원입니다.");
		
		System.out.println("오천원권:" + d +"장");
		//c %= 5000;
		System.out.println("천원권:" + e +"장" );
		//c %= 1000;
		System.out.println("오백원짜리동전:" + f +"개");
		//c %= 500;
		System.out.println("백원짜리동전:" + g +"개");
		//c %= 100;
		System.out.println("오십원짜리동전:" + h +"개");
		//c %= 50;
		System.out.println("십원짜리동전:" +i + "개");
		//c %= 10;
		
	}
}