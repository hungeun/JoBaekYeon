//클래스 상속의 기초 문법
package chap05;

public class CheckingAccount extends Account2 {
	String cardNo;
	
	int pay(String cardNo, int amount) throws Exception {
		if (!cardNo.equals(this.cardNo) || (balance < amount))
			throw new Exception("지불이 불가능합니다.");
		return withdraw(amount);
	}
}
