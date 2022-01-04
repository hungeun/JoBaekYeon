package chap02;

public class Example2 {
	public static void main(String argsp[]) {
		
		int i =100;
		short s =(short)i;  //명시적 형변환
	    
		int j = s; //작은걸 큰거에 저장은 이상은 없음
		
		byte a = 10;
		short b = 20, c;
		c = a + b  //안되는 이유?->java에서는 int보다 작은 byte나 short 타입을 연산할 때 int로 바꿈: int 프로모션
				   //해결 -> int c; 를 주면됨
		
		
	}
}
