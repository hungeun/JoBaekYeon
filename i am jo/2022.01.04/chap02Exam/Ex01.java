package chap02Exam; //ü�� ���� ���α׷�

import java.util.Scanner;

public class Ex01 {
	public static void main(String arg[]) {
		
	
		
				
		Scanner sc = new Scanner(System.in);
		int weight;
		double height, bmi;
		String msg = "";
		
		System.out.print("������(kg): ");
		weight = sc.nextInt();
		
		System.out.print("Ű�� �Է��ϼ���");
		height = sc.nextDouble();
		
		sc.close();
		
		height /= 100;
		bmi = weight / (height*height);
		msg += bmi >= 20 && bmi <25 ? "ǥ���Դϴ�." : "ü�� ������ �ʿ��մϴ�.";
		
		System.out.println("BMI��" + bmi +"/" + "msg.");
	}
}