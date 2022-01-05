/*
 * 숫자 맞추기 게임 프로그램
숫자를 입력하여 정답 숫자를 맞추는 게임이다. 정답 숫자는 1 부터 100 까지의 숫자 중 하나이며 입력한 숫자가 정답이 아닐 경우 정답이 입력한 숫자보다 크거나 작은지 힌트로 알려준다. 
정답을 맞출 때까지 숫자 입력을 반복하고 정답을 맞춘 후 에는 시도한 횟수를 출력한다.
 */
package chap03Example;

import java.util.Random;

import java.util.Scanner;

public class Exam3 {
	public static void main(String[] args) {
		Random rand = new Random();
		rand.setSeed(System.currentTimeMillis());
		Scanner sc = new Scanner(System.in);
		
		int answer = rand.nextInt(100);
		int answerPoint = 0;
		int num;
		int count = 0;
		
		do {
			count += 1;
			System.out.print("숫자 입력(1부터 100까지) :");
			num = sc.nextInt();
			if(num < answer) {
				System.out.println(num + "보다 큽니다!");
			}else if(num > answer){
				System.out.println(num + "보다 작습니다!");
			}else {
				System.out.println("정답입니다!");
				answerPoint = 1;
			}
		}while(answerPoint != 1);
			
		System.out.println("시도한 횟수는 " + count + "회입니다.");
	}

}