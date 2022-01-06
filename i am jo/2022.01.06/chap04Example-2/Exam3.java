package chap04Example;

import java.time.LocalDate;
import java.util.HashMap;
import java.util.Scanner;

public class Exam3 {
	static HashMap<String, String> weekMap = new HashMap<>();
	public static void main(String[] args) {
		weekMap.put("SUNDAY", "일요일");
		weekMap.put("MONDAY", "월요일");
		weekMap.put("TUESDAY", "화요일");
		weekMap.put("WEDNESDAY", "수요일");
		weekMap.put("THURSDAY", "목요일");
		weekMap.put("FRIDAY", "금요일");
		weekMap.put("SATURDAY", "토요일");
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("년도를 입력하세요 : ");
		int year = sc.nextInt();
		
		System.out.print("월을 입력하세요 : ");
		int month = sc.nextInt();
		
		System.out.print("일을 입력하세요 : ");
		int day = sc.nextInt();
		
		LocalDate date = LocalDate.of(year, month, day);
		System.out.printf("%d년 %d월 %d일은 " + weekMap.get(date.getDayOfWeek().toString())+"입니다",year,month,day);
		
		
		//System.out.println(weekMap.get(date.getDayOfWeek().toString()));
	}
}
