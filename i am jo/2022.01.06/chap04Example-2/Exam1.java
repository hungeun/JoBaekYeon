package chap04Example;

import java.util.Date;

import java.util.Scanner;

public class Exam1 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("년도를 입력하세요 : ");
		year(sc.nextInt());
		
		sc.close();
	}
	private static void year(int year) {
		System.out.println(year + "년은 " + (year % 400 == 0 ? "윤년" : year % 100 == 0 ? "평년" : year % 4 == 0 ? "윤년" : "평년") + "입니다.");
	}
}
