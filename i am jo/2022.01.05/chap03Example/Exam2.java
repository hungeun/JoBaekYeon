/*
 * ������ ��� ���α׷�
	���� ��뷮(kw)�� �Է� �޾� ��� ����� ����ϴ� ���α׷��� �ۼ��Ѵ�.
	��� ����� �⺻��� + ��뷮 * kw �� ��� + ����
	������ ��ü ��� ����� 9%�̸�, ��� ���� ������ ������ ����.
				[�⺻���] [kw �� ���]
					1 ~ 100kw: 370
					101 ~ 200kw: 660
					201 ~ 300kw: 1130
					301 ~ 400kw: 2710
					401 ~ 500kw: 5130
					500kw �ʰ�: 9330
					1 ~ 100kw: 52.0
					101 ~ 200kw: 88.5
					201 ~ 300kw: 127.8
					301 ~ 400kw: 184.3
					401 ~ 500kw: 274.3
					500kw �ʰ�: 494.0
 */
package chap03Example;
import java.util.Scanner;
public class Exam2 {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		double money = 0;
		
		System.out.print("���� ��뷮�� �Է��ϼ���(kw) :");
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
		
		System.out.println("�̹� �� ����� " + (int)money + "�� �Դϴ�.");
		
		
	}

}