package chap04;

import java.util.Scanner;

public class Exam2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("�⵵�� �Է��ϼ��� : ");
		int year = sc.nextInt();
		System.out.print("���� �Է��ϼ��� : ");
		int month = sc.nextInt();
		
		int[] date = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		if (year % 400 == 0)
			++date[2];
		else if (year % 100 == 0)
			;
		else if (year % 4 == 0)
			++date[2];
		
		System.out.printf("%d�� %d���� ������ ����: %d��", year, month, date[month]);
		sc.close();
	}
}