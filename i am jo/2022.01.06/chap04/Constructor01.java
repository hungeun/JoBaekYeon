package chap04;

public class Constructor01 {
	public static void main(String args[]) {
		GoodsStock obj;
		obj = new GoodsStock("52135", 200);
		System.out.println("��ǰ�ڵ�:" + obj.goodsCode);
		System.out.println("������:" + obj.stockNum);
		obj.addStock(1000);
		System.out.println("��ǰ�ڵ�:" + obj.goodsCode);
		System.out.println("������:" + obj.stockNum);
		}
	}

