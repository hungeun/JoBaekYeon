package chap02;

public class Example3 {
public static void main(String argsp[]) {
		
		int a = 0, b = 0;
		boolean c;
		
		c = ++a == 0 && b++ ==0; //&& ���ǿ����ڿ��� ù�� ° �򰡿����� false �̹Ƿ� �ι�°�� �� �ʿ�x, �ι� °�� ������ ����
								 //& �� �������̸� �ι� °���� ������ -> �����ϸ� false : 1 : 1
		System.out.println(c);
		//System.out.println(c + ":" + a + ":" + b); ->���: false : 1 : 0 
		
	}
}

/*
   A             B            A^B
   False         False        False
   False         True         True
   True          False        True
   True          True         False
*/