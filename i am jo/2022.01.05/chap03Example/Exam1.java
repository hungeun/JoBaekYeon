/*
 * 장학금 계산 프로그램
	가정형편과 이전 학기의 성적으로 다음 학기의 등록금을 할인해 주는 프로그램을 작성한다.
	다음 학기 등록금은 100만원이며 장학금 지급 기준은 다음과 같다
	가정형편이 좋고 평균 학점이 4.0 이상이면 등록금의 20%를 장학금 지급.
	가정형편이 어려운 경우는 학점과 관계없이 등록금의 40%를 장학금 지급.
	가정형편이 어렵고 평균 학점이 4.0 이상이면 60%를 장학금 지급.
	가정형편은 a, b, c 등급으로 정하고 이 중 c 등급이면 장학금 지급 대상으로 한다.
 */
package chap03Example;

import java.util.Scanner;

public class Exam1 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		int money = 100;
		
		System.out.print("가정 형편을 입력하시오 :");
		String rich = sc.next();
		System.out.println();
		
		System.out.print("평균 학점을 입력하시오 :");
		double grade = sc.nextDouble();
		System.out.println();
		
		if ((rich.equals("a") || rich.equals("b")) && grade >= 4.0) {
			money = money * 80 / 100;
			
		}else if(rich.equals("c") && grade >= 4.0) {
			money = money * 40 / 100;
			
		}else if(rich.equals("c")) {
			money = money * 60 / 100;
		}
		
		System.out.println("다음 학기 납입할 등록금은 " + money + "만원 입니다.");
	}

}
