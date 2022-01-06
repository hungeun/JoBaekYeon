package chap04;

import java.util.Scanner;

public class Exam1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("년도를 입력하세요 : ");
		int year = sc.nextInt();
		
		String s;
		if (year % 400 == 0)
			s = "윤";
		else if (year % 100 == 0)
			s = "평";
		else if (year % 4 == 0)
			s = "윤";
		else
			s = "평";
		
		System.out.println(year + "년은 " + s + "년입니다.");
		sc.close();
	}
}