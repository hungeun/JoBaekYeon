//Ŭ���� ���ο����� �޼ҵ� ȣ��  - ���� �迭�� ��踦 ���� Ŭ����

package chap05;

public class Numbers {
	int num[];
	Numbers(int num[]) { // ������
	this.num = num;
	}
	int getTotal() { // �迭�� �հ踦 ���ϴ� �޼ҵ�
	int total = 0;
	for (int cnt = 0; cnt < num.length; cnt++)
	total += num[cnt];
	return total;
	}
	}
