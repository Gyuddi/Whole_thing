package jump2java.message;
public class Item {
	private String name;
	private int length;
	private String value;
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getLenght() {
		return length;
	}
	public void setLenght(int length) {
		this.length = length;
	}
	public String getValue() {
		return value;
	}
	public void setValue(String value) {
		this.value = value;
	}
	public String raw() {
	    StringBuffer padded = new StringBuffer(this.value);
	    while (padded.toString().getBytes().length < this.length) {
	        padded.append(' ');
	    }
	    return padded.toString();
	}
	public static void main(String[] args) {
		Item item =new Item();
		item.setName("�̸�");
		item.setLenght(10);
		item.setValue("ȫ�浿");
		System.out.println("["+item.raw()+"]");
	}
	
}
