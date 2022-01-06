package chap04Example;

import java.util.Arrays;
import java.util.Scanner;

public class Exam4 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int year, day;
		String month;
		String buffer;
		
		int yearNum; 
		int dayNum;		
		
		int JeonIl, iMonth;
		
		System.out.print("�⵵�� �Է��ϼ��� : ");
		year = sc.nextInt();
		
		System.out.print("���� �Է��ϼ��� : ");
		buffer = sc.nextLine();
		month = sc.nextLine();
		iMonth = Integer.parseInt(month);
		
		System.out.print("���� �Է��ϼ��� : ");
		day = sc.nextInt();
		
		Date ob = new Date(year, iMonth, day);
		System.out.println(year + "�� " + month + "�� "  + day + "���� " + ob.getWeekday() + "���� �Դϴ�.");
	}

}

class Date{
	int year, month, date, yearNum, dayNum;
	int JeonIl;
	
	String gangDal[] = { "1", "3", "5", "7", "8", "11" };
	String day_Week[] = { "��", "ȭ", "��", "��", "��", "��", "��"};
	
	int month_Day[] = {31, 0, 31, 30, 31, 30, 31, 30, 31, 30, 31, 32};
	
	Date(int year, int month, int date){
		this.year = year;
		this.month = month;
		this.date = date;
	}
	
	String getWeekday(){
		if(year % 4 == 0 && year % 100 != 0) {
			yearNum = 2;
		}else if(year % 400 == 0) {
			yearNum = 2;
		}else {
			yearNum = 1;
		}

		if(Arrays.asList(gangDal).contains(month)) {
			dayNum = 31;
		}else if(yearNum == 2 && month == 2) {
			month_Day[1] = 29;
		}else if(yearNum == 1 && month == 2) {
			month_Day[1] = 28;
		}else {
			dayNum = 30;
		}
		
		JeonIl = (year - 1) * 365 + (year - 1)/4 - (year - 1)/100 + (year - 1)/400;
		
		for(int i = 0; i < month- 1; i++) {
			JeonIl += month_Day[i];
		}
				
		JeonIl += date;
		
		return day_Week[JeonIl%7-1];
	}
	

	
}