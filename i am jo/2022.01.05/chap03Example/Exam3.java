/*
 * ���� ���߱� ���� ���α׷�
���ڸ� �Է��Ͽ� ���� ���ڸ� ���ߴ� �����̴�. ���� ���ڴ� 1 ���� 100 ������ ���� �� �ϳ��̸� �Է��� ���ڰ� ������ �ƴ� ��� ������ �Է��� ���ں��� ũ�ų� ������ ��Ʈ�� �˷��ش�. 
������ ���� ������ ���� �Է��� �ݺ��ϰ� ������ ���� �� ���� �õ��� Ƚ���� ����Ѵ�.
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
			System.out.print("���� �Է�(1���� 100����) :");
			num = sc.nextInt();
			if(num < answer) {
				System.out.println(num + "���� Ů�ϴ�!");
			}else if(num > answer){
				System.out.println(num + "���� �۽��ϴ�!");
			}else {
				System.out.println("�����Դϴ�!");
				answerPoint = 1;
			}
		}while(answerPoint != 1);
			
		System.out.println("�õ��� Ƚ���� " + count + "ȸ�Դϴ�.");
	}

}