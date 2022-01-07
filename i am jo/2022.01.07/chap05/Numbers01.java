//클래스 내부에서의 메소드 호출  - 정수 배열의 통계를 내는 클래스 – 평균 계산 기능 추가
package chap05;

public class Numbers01 {
	int num[];
	Numbers01(int num[]) {
	this.num = num;
	}
	int getTotal() { // 합계를 구하는 메소드
	int total = 0;
	for (int cnt = 0; cnt < num.length; cnt++)
	total += num[cnt];
	return total;
	}
	int getAverage() { // 평균을 구하는 메소드
	int total;
	total = getTotal();
	int average = total / num.length;
	return average;
	}
	}