/*
 * ���б� ��� ���α׷�
	��������� ���� �б��� �������� ���� �б��� ��ϱ��� ������ �ִ� ���α׷��� �ۼ��Ѵ�.
	���� �б� ��ϱ��� 100�����̸� ���б� ���� ������ ������ ����
	���������� ���� ��� ������ 4.0 �̻��̸� ��ϱ��� 20%�� ���б� ����.
	���������� ����� ���� ������ ������� ��ϱ��� 40%�� ���б� ����.
	���������� ��ư� ��� ������ 4.0 �̻��̸� 60%�� ���б� ����.
	���������� a, b, c ������� ���ϰ� �� �� c ����̸� ���б� ���� ������� �Ѵ�.
 */
package chap03Example;

import java.util.Scanner;

public class Exam1 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		int money = 100;
		
		System.out.print("���� ������ �Է��Ͻÿ� :");
		String rich = sc.next();
		System.out.println();
		
		System.out.print("��� ������ �Է��Ͻÿ� :");
		double grade = sc.nextDouble();
		System.out.println();
		
		if ((rich.equals("a") || rich.equals("b")) && grade >= 4.0) {
			money = money * 80 / 100;
			
		}else if(rich.equals("c") && grade >= 4.0) {
			money = money * 40 / 100;
			
		}else if(rich.equals("c")) {
			money = money * 60 / 100;
		}
		
		System.out.println("���� �б� ������ ��ϱ��� " + money + "���� �Դϴ�.");
	}

}
