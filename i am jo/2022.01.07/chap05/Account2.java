package chap05;

public class Account2 {
	String accountNo;
	String ownerName;
	int balance;
	
	void deposit(int amount) {
		balance += amount;
	}
	
	int withdraw(int amount) throws Exception {
	
		if (balance < amount)
			throw new Exception("�ܾ��� �����մϴ�.");
			balance -= amount;
		return amount;
	}
}
