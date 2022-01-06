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
		
		int yearNum; //2면 윤년, 1면 평년
		
		String gangDal[] = { "1", "3", "5", "7", "8", "11" };
		
		System.out.print("년도를 입력하세요 : ");
		year = sc.nextInt();
		
		System.out.print("월을 입력하세요 : ");
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
			System.out.println(year + "년 " + month + "월의 마지막 일자 : 31일" );
		}else if(yearNum == 2 && month.equals("2")) {
			System.out.println(year + "년 " + month + "월의 마지막 일자 : 29일" );
		}else if(yearNum == 1 && month.equals("2")) {
			System.out.println(year + "년 " + month + "월의 마지막 일자 : 28일" );
		}else {
			System.out.println(year + "년 " + month + "월의 마지막 일자 : 30일" );
		}
		

	}

}
