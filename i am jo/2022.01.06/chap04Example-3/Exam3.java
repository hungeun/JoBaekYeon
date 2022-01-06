package chap04Example;

import java.util.Arrays;
import java.util.Scanner;


public class Exam3 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int year, day;
		String month;
		String buffer;
		
		int yearNum; //2면 윤년, 1면 평년
		int dayNum; //마지막 일자		
		
		int JeonIl;
		
		String gangDal[] = { "1", "3", "5", "7", "8", "11" };
		String day_Week[] = { "월", "화", "수", "목", "금", "토", "일"};
		
		int month_Day[] = {31, 0, 31, 30, 31, 30, 31, 30, 31, 30, 31, 32};
		
		System.out.print("년도를 입력하세요 : ");
		year = sc.nextInt();
		
		System.out.print("월을 입력하세요 : ");
		buffer = sc.nextLine();
		month = sc.nextLine();
		
		System.out.print("일을 입력하세요 : ");
		day = sc.nextInt();
		
		if(year % 4 == 0 && year % 100 != 0) {
			yearNum = 2;
		}else if(year % 400 == 0) {
			yearNum = 2;
		}else {
			yearNum = 1;
		}
	
		if(Arrays.asList(gangDal).contains(month)) {
			dayNum = 31;
		}else if(yearNum == 2 && month.equals("2")) {
			month_Day[1] = 29;
		}else if(yearNum == 1 && month.equals("2")) {
			month_Day[1] = 28;
		}else {
			dayNum = 30;
		}
		
		JeonIl = (year - 1) * 365 + (year - 1)/4 - (year - 1)/100 + (year - 1)/400;
		
		for(int i = 0; i < Integer.parseInt(month)- 1; i++) {
			JeonIl += month_Day[i];
		}
				
		JeonIl += day;
		
		System.out.println(year + "년 " + month + "월 "  + day + "일은 " +day_Week[JeonIl%7-1] + "요일 입니다.");
		

	}
}