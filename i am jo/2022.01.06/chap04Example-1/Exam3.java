package chap04;

import java.util.Scanner;

public class Exam3 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("년도를 입력하세요 : ");
		int year = sc.nextInt();
		System.out.print("월을 입력하세요 : ");
		int month = sc.nextInt();
		System.out.print("일을 입력하세요 : ");
		int day = sc.nextInt();
		
		int date = 0;
		
		for (int i = 1; i < year; ++i)
		{
			date += 365;
			if (year % 400 == 0)
				++date;
			else if (year % 100 == 0)
				;
			else if (year % 4 == 0)
				++date;
		}
		
		int[] arr = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		for (int i = 1; i < month; ++i)
			date += arr[i];
		if (month > 2)
			if (year % 400 == 0)
				++date;
			else if (year % 100 == 0)
				;
			else if (year % 4 == 0)
				++date;
		
		date += day;
		
		String[] s = {"일", "월", "화", "수", "목", "금", "토"};
		
		System.out.printf("%d년 %d월의 %d일은 %s요일입니다.", year, month, day, s[date%7]);
		sc.close();
	}
}