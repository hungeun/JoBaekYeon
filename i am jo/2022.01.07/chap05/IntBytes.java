//정적 메소드들로만 구성된 기능적 클래스
package chap05;

public class IntBytes {
	static byte firstByte(int num) {
		num = (num >> 24) & 0xFF;
		return (byte) num;
		}
		//int 타입 데이터의 1번째 바이트를 리턴하는 메소드
	
	static byte secondByte(int num) {
		num = (num >> 16) & 0xFF;
		return (byte) num;
		}
		//int 타입 데이터의 2번째 바이트를 리턴하는 메소드
	
	static byte thirdByte(int num) {
		num = (num >> 8) & 0xFF;
		return (byte) num;
		}
		//int 타입 데이터의 3번째 바이트를 리턴하는 메소드
	
	static byte forthByte(int num) {
		num = num & 0xFF;
		return (byte) num;
		}
		}
		//int 타입 데이터의 4번째 바이트를 리턴하는 메소드
		
		
		
	