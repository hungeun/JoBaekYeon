package chap02Exam;

import java.util.Scanner;

public class EX03 {

public static void main(String arg[]) {
				
		
		Scanner sc = new Scanner(System.in);
			int distance, speed, hour, minute;
			double second;
			
		System.out.print("거리(km): ");
		distance = sc.nextInt();
		
		System.out.print("속력(km/h): ");
		speed = sc.nextInt();
		 //시 = 거리/속력
		sc.close();
	
		hour = distance / speed;
		minute = (int)(((double)distance / speed - hour) * 60);
		second = ((((double)distance / speed -hour) * 60) - minute) * 60;
		System.out.println("소요시간은" + hour + "시간"+ minute + "분"+ second +"초 입니다.");
		
	}
}