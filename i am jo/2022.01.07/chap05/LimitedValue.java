/*상수 필드(또는 상수 변수) : static과 final 키워드가 모두 붙은 필드 → 초기값을 바꿀 수 없으므로 상수로 사용하기에 적합
		
		상수 필드가 있는 클래스
 */
package chap05;

public class LimitedValue {
	final static int UPPER_LIMIT = 100000;
	int value;
	
	void setValue(int value) {
		if (value < UPPER_LIMIT)
			this.value = value;
		else
			this.value = UPPER_LIMIT;
	}
	}
