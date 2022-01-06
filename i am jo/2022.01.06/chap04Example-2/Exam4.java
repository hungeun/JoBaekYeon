package chap04Example;

import java.time.LocalDate;
import java.util.HashMap;
import java.util.Scanner;

public class Exam4 {
	public static void main(String[] args) {
		Date date;
		
		Scanner sc = new Scanner(System.in);
		System.out.print("�⵵�� �Է��ϼ��� : ");
		int year = sc.nextInt();
		System.out.print("���� �Է��ϼ��� : ");
		int month = sc.nextInt();
		System.out.print("���� �Է��ϼ��� : ");
		int day = sc.nextInt();

		date = new Date(year, month, day);
		System.out.printf("%d���� %s�Դϴ�.\n", year, date.isLeapYear() ? "����" : "���");
		System.out.printf("%d�� %d���� ������ ���� : %d��\n", year, month, date.getMonthLastDay());
		System.out.printf("%d�� %d�� %d���� %s�Դϴ�.\n", year, month, day, date.getWeekDay());
	}
}

class Date {
	int year, month, date;
	static LocalDate dates;
	static HashMap<String, String> weekMap = new HashMap<>();
	
	Date(int year, int month, int date) {
		this.year = year;
		this.month = month;
		this.date = date;
		
		dates = LocalDate.of(year, month, date);

		weekMap.put("SUNDAY", "�Ͽ���");
		weekMap.put("MONDAY", "������");
		weekMap.put("TUESDAY", "ȭ����");
		weekMap.put("WEDNESDAY", "������");
		weekMap.put("THURSDAY", "�����");
		weekMap.put("FRIDAY", "�ݿ���");
		weekMap.put("SATURDAY", "�����");
	}
	
	public boolean isLeapYear() {
		return dates.isLeapYear();
	}
	public int getMonthLastDay() {
		return dates.getDayOfMonth();
	}
	public String getWeekDay() {
		return weekMap.get(dates.getDayOfWeek().toString());
	}
}

