package chap02;

public class Example2 {
	public static void main(String argsp[]) {
		
		int i =100;
		short s =(short)i;  //����� ����ȯ
	    
		int j = s; //������ ū�ſ� ������ �̻��� ����
		
		byte a = 10;
		short b = 20, c;
		c = a + b  //�ȵǴ� ����?->java������ int���� ���� byte�� short Ÿ���� ������ �� int�� �ٲ�: int ���θ��
				   //�ذ� -> int c; �� �ָ��
		
		
	}
}
