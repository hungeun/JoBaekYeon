//���� �޼ҵ��θ� ������ ����� Ŭ����
package chap05;

public class IntBytes {
	static byte firstByte(int num) {
		num = (num >> 24) & 0xFF;
		return (byte) num;
		}
		//int Ÿ�� �������� 1��° ����Ʈ�� �����ϴ� �޼ҵ�
	
	static byte secondByte(int num) {
		num = (num >> 16) & 0xFF;
		return (byte) num;
		}
		//int Ÿ�� �������� 2��° ����Ʈ�� �����ϴ� �޼ҵ�
	
	static byte thirdByte(int num) {
		num = (num >> 8) & 0xFF;
		return (byte) num;
		}
		//int Ÿ�� �������� 3��° ����Ʈ�� �����ϴ� �޼ҵ�
	
	static byte forthByte(int num) {
		num = num & 0xFF;
		return (byte) num;
		}
		}
		//int Ÿ�� �������� 4��° ����Ʈ�� �����ϴ� �޼ҵ�
		
		
		
	