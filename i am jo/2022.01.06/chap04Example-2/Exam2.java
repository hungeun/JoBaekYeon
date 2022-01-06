package chap04Example;

import java.util.Scanner;

public class Exam2 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("년도를 입력하세요 : ");
		int year = sc.nextInt();
		int[] months = {31, 28 + year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		
		System.out.print("월을 입력하세요 : ");
		int month = sc.nextInt();
		System.out.printf("%d년 %d월의 마지막 일자: %d" + "일", year, month, months[month - 1]);
		
		sc.close();
	}
	private static int year(int year) {
		return year % 400 == 0 ? 1 : year % 100 == 0 ? 0 : year % 4 == 0 ? 1 : 0;
	}
}
