import java.util.Arrays;

public class Test {
	public static void main(String[] args) {
		
		// test print list
		String[] test = {"a","b", "c"};
		for (int i=0; i< test.length; i++) {
			for (int j = i+1; j<= test.length; j++) {
				String[] temp = Arrays.copyOfRange(test, i, j);
				String needed = String.join(" ",temp);
				System.out.println(needed);
			}
		}
		
		// test remove punctuation
		String text = "This. is@ a game of thrones!";
		String input = text.toString().replaceAll("\\p{Punct}",""); 
		System.out.println(input);
		String[] lists =  input.split(" ");
		for (int i=0; i<lists.length; i++) {
			System.out.println(lists[i]);
		}
	}
}
