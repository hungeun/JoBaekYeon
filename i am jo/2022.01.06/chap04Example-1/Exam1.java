package chap04;

import java.util.Scanner;

public class Exam1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("�⵵�� �Է��ϼ��� : ");
		int year = sc.nextInt();
		
		String s;
		if (year % 400 == 0)
			s = "��";
		else if (year % 100 == 0)
			s = "��";
		else if (year % 4 == 0)
			s = "��";
		else
			s = "��";
		
		System.out.println(year + "���� " + s + "���Դϴ�.");
		sc.close();
	}
}