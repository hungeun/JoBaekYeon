package chap02Exam;

import java.util.Scanner;

public class EX02 {
	public static void main(String arg[]) {
		
		int a, b, c, d, e, f, g, h, i;
		
		Scanner sc = new Scanner(System.in);

		System.out.print("��ǰ�� ���� ���� �Է��ϼ���");
		a = sc.nextInt();
		
		sc.close();
		 b = 10000;
		 c = b - a;
		 d = c/5000;	
		 e = (c-(d*5000))/1000;
		 f = (c-((e*1000)+(d*5000)))/500;
		 g = (c-((e*1000)+(d*5000)+(f*500)))/100;
		 h = (c-((e*1000)+(d*5000)+(f*500)+(g*100)))/50;
		 i = (c-((e*1000)+(d*5000)+(f*500)+(g*100)+(h*50)))/10;		 
				 
		System.out.println("�Ž�������" + c + "���Դϴ�.");
		
		System.out.println("��õ����:" + d +"��");
		//c %= 5000;
		System.out.println("õ����:" + e +"��" );
		//c %= 1000;
		System.out.println("�����¥������:" + f +"��");
		//c %= 500;
		System.out.println("���¥������:" + g +"��");
		//c %= 100;
		System.out.println("���ʿ�¥������:" + h +"��");
		//c %= 50;
		System.out.println("�ʿ�¥������:" +i + "��");
		//c %= 10;
		
	}
}