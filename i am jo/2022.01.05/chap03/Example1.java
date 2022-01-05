/*
 [1]사용자에게 영어와 수학 두 과목의 점수를 입력받아 두 과목 모두 80점 이상이면 "합격입니다.", 아니면 "불합격입니다."를 출력
 
 [2]사용자에게 영어와 수학 두 과목의 점수를 입력받아 한 과목 이라도 80점 미만이면 "80점 미만의 값이 있습니다.", 아니면 "모두 80점 이상입니다."를 출력

 [3]사용자에게 영어와 수학 두 과목의 점수를 입력받아 두 과목 모두 80점 이상이면 "합격입니다.", 아니면 "불합격입니다."를 출력. 단 and연산자 사용x
 */

package chap03;

import java.util.Scanner;

public class Example1 {
	
	public static void main(String arg[]) {
		
		int eng, math;
		String score, result;
		String[] scores;
		Scanner sc = new Scanner(System.in);
		
		System.out.print("영어와 수학 점수를 입력하셍(ex 90 85)");
		score = sc.nextLine();
		sc.close();
		
		scores = score.split(" ");
		eng = Integer.parseInt(scores[0]);
		math = Integer.parseInt(scores[1]);
		
		result = !(eng < 80 || math <80) ? "합격입니다.": "불합격입니다";
		System.out.println(result);
	}
	
	
	
}
