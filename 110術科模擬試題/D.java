import java.util.*;

public class D {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String input;// = scanner.nextLine();
		int n =Integer.parseInt( scanner.nextLine());
		input = scanner.nextLine();
		String[] ch=input.split(" ");
		Set<String> words = new LinkedHashSet <>();
		for(String a:ch)
			words.add(a);
		System.out.println(words.size());
		
	}
}
