/*
 [1]����ڿ��� ����� ���� �� ������ ������ �Է¹޾� �� ���� ��� 80�� �̻��̸� "�հ��Դϴ�.", �ƴϸ� "���հ��Դϴ�."�� ���
 
 [2]����ڿ��� ����� ���� �� ������ ������ �Է¹޾� �� ���� �̶� 80�� �̸��̸� "80�� �̸��� ���� �ֽ��ϴ�.", �ƴϸ� "��� 80�� �̻��Դϴ�."�� ���

 [3]����ڿ��� ����� ���� �� ������ ������ �Է¹޾� �� ���� ��� 80�� �̻��̸� "�հ��Դϴ�.", �ƴϸ� "���հ��Դϴ�."�� ���. �� and������ ���x
 */

package chap03;

import java.util.Scanner;

public class Example1 {
	
	public static void main(String arg[]) {
		
		int eng, math;
		String score, result;
		String[] scores;
		Scanner sc = new Scanner(System.in);
		
		System.out.print("����� ���� ������ �Է��ϼ�(ex 90 85)");
		score = sc.nextLine();
		sc.close();
		
		scores = score.split(" ");
		eng = Integer.parseInt(scores[0]);
		math = Integer.parseInt(scores[1]);
		
		result = !(eng < 80 || math <80) ? "�հ��Դϴ�.": "���հ��Դϴ�";
		System.out.println(result);
	}
	
	
	
}
