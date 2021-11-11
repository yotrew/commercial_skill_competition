import java.util.*;
public class G {
	static ArrayList<String> gcode = new ArrayList<String>(); 
	static void gray_code(int n){
		if (n==1){
			gcode.add("0");
			gcode.add("1");
			return;
		}
		gray_code(n-1);
		ArrayList<String> tmp= new ArrayList<String>();
		for(int i=0;i<gcode.size();i++){
			tmp.add("0"+gcode.get(i));
		}
			
		for(int i=gcode.size()-1;i>-1;i--){
			tmp.add("1"+gcode.get(i));
		}
		gcode=tmp;
	}
    
    
    
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String in1,in2;// = scanner.nextLine();
		int n =Integer.parseInt( scanner.nextLine());
		gray_code(n);
		for(int i=0;i<gcode.size();i++){
			System.out.println(gcode.get(i));
		}		
	}
}
