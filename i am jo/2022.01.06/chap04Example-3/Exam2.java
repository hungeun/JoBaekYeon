package chap04Example;

import java.util.Arrays;
import java.util.Scanner;


public class Exam2 {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		int year, day;
		String month;
		String buffer;
		
		int yearNum; //2�� ����, 1�� ���
		
		String gangDal[] = { "1", "3", "5", "7", "8", "11" };
		
		System.out.print("�⵵�� �Է��ϼ��� : ");
		year = sc.nextInt();
		
		System.out.print("���� �Է��ϼ��� : ");
		buffer = sc.nextLine();
		month = sc.nextLine();
		
		if(year % 4 == 0 && year % 100 != 0) {
			yearNum = 2;
		}else if(year % 400 == 0) {
			yearNum = 2;
		}else {
			yearNum = 1;
		}
	
		if(Arrays.asList(gangDal).contains(month)) {
			System.out.println(year + "�� " + month + "���� ������ ���� : 31��" );
		}else if(yearNum == 2 && month.equals("2")) {
			System.out.println(year + "�� " + month + "���� ������ ���� : 29��" );
		}else if(yearNum == 1 && month.equals("2")) {
			System.out.println(year + "�� " + month + "���� ������ ���� : 28��" );
		}else {
			System.out.println(year + "�� " + month + "���� ������ ���� : 30��" );
		}
		

	}

}
