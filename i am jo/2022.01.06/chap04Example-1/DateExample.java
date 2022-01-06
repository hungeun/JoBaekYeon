package chap04;

import java.util.Scanner;

public class DateExample {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("년도를 입력하세요 : ");
		int year = sc.nextInt();
		System.out.print("월을 입력하세요 : ");
		int month = sc.nextInt();
		System.out.print("일을 입력하세요 : ");
		int day = sc.nextInt();		
		sc.close();
		
		Date date = new Date();
		System.out.printf("%d년 %d월 %d일은 %s요일입니다.",
				year, month, day, date.getWeekday(year, month, day));
	}
}