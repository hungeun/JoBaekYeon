//Ŭ���� ����� ���� ����
package chap05;

public class CheckingAccount extends Account2 {
	String cardNo;
	
	int pay(String cardNo, int amount) throws Exception {
		if (!cardNo.equals(this.cardNo) || (balance < amount))
			throw new Exception("������ �Ұ����մϴ�.");
		return withdraw(amount);
	}
}
