//클래스 내부에서의 메소드 호출  - 정수 배열의 통계를 내는 클래스

package chap05;

public class Numbers {
	int num[];
	Numbers(int num[]) { // 생성자
	this.num = num;
	}
	int getTotal() { // 배열의 합계를 구하는 메소드
	int total = 0;
	for (int cnt = 0; cnt < num.length; cnt++)
	total += num[cnt];
	return total;
	}
	}
