package chap04Example;

import java.util.Date;

import java.util.Scanner;

public class Exam1 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("�⵵�� �Է��ϼ��� : ");
		year(sc.nextInt());
		
		sc.close();
	}
	private static void year(int year) {
		System.out.println(year + "���� " + (year % 400 == 0 ? "����" : year % 100 == 0 ? "���" : year % 4 == 0 ? "����" : "���") + "�Դϴ�.");
	}
}
