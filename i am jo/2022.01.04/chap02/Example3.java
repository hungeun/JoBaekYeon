package chap02;

public class Example3 {
public static void main(String argsp[]) {
		
		int a = 0, b = 0;
		boolean c;
		
		c = ++a == 0 && b++ ==0; //&& 조건연산자여서 첫번 째 평가연산이 false 이므로 두번째는 할 필요x, 두번 째는 실행을 안함
								 //& 논리 연산자이면 두번 째까지 연산함 -> 실행하면 false : 1 : 1
		System.out.println(c);
		//System.out.println(c + ":" + a + ":" + b); ->결과: false : 1 : 0 
		
	}
}

/*
   A             B            A^B
   False         False        False
   False         True         True
   True          False        True
   True          True         False
*/