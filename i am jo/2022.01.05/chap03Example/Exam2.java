/*
 * 전기요금 계산 프로그램
	전기 사용량(kw)을 입력 받아 사용 요금을 출력하는 프로그램을 작성한다.
	사용 요금은 기본요금 + 사용량 * kw 당 요금 + 세금
	세금은 전체 사용 요금의 9%이며, 요금 적용 기준은 다음과 같다.
				[기본요금] [kw 당 요금]
					1 ~ 100kw: 370
					101 ~ 200kw: 660
					201 ~ 300kw: 1130
					301 ~ 400kw: 2710
					401 ~ 500kw: 5130
					500kw 초과: 9330
					1 ~ 100kw: 52.0
					101 ~ 200kw: 88.5
					201 ~ 300kw: 127.8
					301 ~ 400kw: 184.3
					401 ~ 500kw: 274.3
					500kw 초과: 494.0
 */
package chap03Example;
import java.util.Scanner;
public class Exam2 {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		double money = 0;
		
		System.out.print("전기 사용량을 입력하세요(kw) :");
		double elect = sc.nextDouble();
		System.out.println();
		
		if (elect <= 100) {
			money = (370 + 52 * elect);
		}else if(elect <= 200) {
			elect -= 100;
			money = (660 + 52 * 100 + 88.5 * elect);
		}else if(elect <= 300) {
			elect -= 200;
			money = (1130 + 52 * 100 + 88.5 * 100 + 127.8 * elect);
		}
		money = money * 109 / 100;
		
		System.out.println("이번 달 요금은 " + (int)money + "원 입니다.");
		
		
	}

}