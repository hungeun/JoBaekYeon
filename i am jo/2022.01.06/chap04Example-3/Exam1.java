package chap04Example;

import java.util.Scanner;

public class Exam1 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int year, month, day;
		
		System.out.print("�⵵�� �Է��ϼ��� : ");
		year = sc.nextInt();	
		
		if(year % 4 == 0 && year % 100 != 0) {
			System.out.println(year + "���� �����Դϴ�.");
		}else if(year % 400 == 0) {
			System.out.println(year + "���� �����Դϴ�.");
		}else {
			System.out.println(year + "���� ����Դϴ�.");
		}
		
	}

}