package chap04;

import java.util.Scanner;

public class DateExample {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("�⵵�� �Է��ϼ��� : ");
		int year = sc.nextInt();
		System.out.print("���� �Է��ϼ��� : ");
		int month = sc.nextInt();
		System.out.print("���� �Է��ϼ��� : ");
		int day = sc.nextInt();		
		sc.close();
		
		Date date = new Date();
		System.out.printf("%d�� %d�� %d���� %s�����Դϴ�.",
				year, month, day, date.getWeekday(year, month, day));
	}
}