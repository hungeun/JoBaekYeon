package chap04Example;

import java.time.LocalDate;
import java.util.HashMap;
import java.util.Scanner;

public class Exam3 {
	static HashMap<String, String> weekMap = new HashMap<>();
	public static void main(String[] args) {
		weekMap.put("SUNDAY", "�Ͽ���");
		weekMap.put("MONDAY", "������");
		weekMap.put("TUESDAY", "ȭ����");
		weekMap.put("WEDNESDAY", "������");
		weekMap.put("THURSDAY", "�����");
		weekMap.put("FRIDAY", "�ݿ���");
		weekMap.put("SATURDAY", "�����");
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("�⵵�� �Է��ϼ��� : ");
		int year = sc.nextInt();
		
		System.out.print("���� �Է��ϼ��� : ");
		int month = sc.nextInt();
		
		System.out.print("���� �Է��ϼ��� : ");
		int day = sc.nextInt();
		
		LocalDate date = LocalDate.of(year, month, day);
		System.out.printf("%d�� %d�� %d���� " + weekMap.get(date.getDayOfWeek().toString())+"�Դϴ�",year,month,day);
		
		
		//System.out.println(weekMap.get(date.getDayOfWeek().toString()));
	}
}
