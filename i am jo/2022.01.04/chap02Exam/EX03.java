package chap02Exam;

import java.util.Scanner;

public class EX03 {

public static void main(String arg[]) {
				
		
		Scanner sc = new Scanner(System.in);
			int distance, speed, hour, minute;
			double second;
			
		System.out.print("�Ÿ�(km): ");
		distance = sc.nextInt();
		
		System.out.print("�ӷ�(km/h): ");
		speed = sc.nextInt();
		 //�� = �Ÿ�/�ӷ�
		sc.close();
	
		hour = distance / speed;
		minute = (int)(((double)distance / speed - hour) * 60);
		second = ((((double)distance / speed -hour) * 60) - minute) * 60;
		System.out.println("�ҿ�ð���" + hour + "�ð�"+ minute + "��"+ second +"�� �Դϴ�.");
		
	}
}