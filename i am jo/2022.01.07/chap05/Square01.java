//final필드는 선언과 동시에 초기화 가능

package chap05;

public class Square01 {
	final int sideLength; // 선언문에서는 초기화 하지 않았지만
	Square01(int sideLength) {
	this.sideLength = sideLength; // 생성자 안에서 초기화했음
	}
	}