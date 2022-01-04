package chap02Exam; //체중 관리 프로그램

import java.util.Scanner;

public class Ex01 {
	public static void main(String arg[]) {
		
	
		
				
		Scanner sc = new Scanner(System.in);
		int weight;
		double height, bmi;
		String msg = "";
		
		System.out.print("몸무게(kg): ");
		weight = sc.nextInt();
		
		System.out.print("키를 입력하세요");
		height = sc.nextDouble();
		
		sc.close();
		
		height /= 100;
		bmi = weight / (height*height);
		msg += bmi >= 20 && bmi <25 ? "표준입니다." : "체중 관리가 필요합니다.";
		
		System.out.println("BMI는" + bmi +"/" + "msg.");
	}
}