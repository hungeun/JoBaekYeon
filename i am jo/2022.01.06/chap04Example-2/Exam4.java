package chap04Example;

import java.time.LocalDate;
import java.util.HashMap;
import java.util.Scanner;

public class Exam4 {
	public static void main(String[] args) {
		Date date;
		
		Scanner sc = new Scanner(System.in);
		System.out.print("년도를 입력하세요 : ");
		int year = sc.nextInt();
		System.out.print("월을 입력하세요 : ");
		int month = sc.nextInt();
		System.out.print("일을 입력하세요 : ");
		int day = sc.nextInt();

		date = new Date(year, month, day);
		System.out.printf("%d년은 %s입니다.\n", year, date.isLeapYear() ? "윤년" : "평년");
		System.out.printf("%d년 %d월의 마지막 일자 : %d일\n", year, month, date.getMonthLastDay());
		System.out.printf("%d년 %d월 %d일은 %s입니다.\n", year, month, day, date.getWeekDay());
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

		weekMap.put("SUNDAY", "일요일");
		weekMap.put("MONDAY", "월요일");
		weekMap.put("TUESDAY", "화요일");
		weekMap.put("WEDNESDAY", "수요일");
		weekMap.put("THURSDAY", "목요일");
		weekMap.put("FRIDAY", "금요일");
		weekMap.put("SATURDAY", "토요일");
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

