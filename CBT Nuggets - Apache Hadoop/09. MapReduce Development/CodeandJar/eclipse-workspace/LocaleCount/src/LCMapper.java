import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class LCMapper extends Mapper<Object, Text, Text, IntWritable> {
	private final static IntWritable one = new IntWritable(1);
	private Text word = new Text();
	
	public void map(Object key, Text text, Context context) throws IOException, InterruptedException{
		try {
			String[] lists = text.toString().split(",");
			String country = lists[7].trim();
			String lang = lists[9].trim();
			if(lang.length()==2 && country.length()==2) {
				String locale = lang.toLowerCase() + "-" + country.toLowerCase();
				word.set(locale);
				context.write(word, one);
			}else {
				country = lists[9].trim();
				lang = lists[11].trim();
				if(lang.length()==2 && country.length()==2) {
					String locale = lang.toLowerCase() + "-" + country.toLowerCase();
					word.set(locale);
					context.write(word, one);
				}else {
					country = lists[8].trim();
					lang = lists[10].trim();
					if(lang.length()==2 && country.length()==2) {
						String locale = lang.toLowerCase() + "-" + country.toLowerCase();
						word.set(locale);
						context.write(word, one);
					}else {
						country = lists[6].trim();
						lang = lists[7].trim();
						if(lang.length()==2 && country.length()==2) {
							String locale = lang.toLowerCase() + "-" + country.toLowerCase();
							word.set(locale);
							context.write(word, one);
						}else {
							System.out.println("Exception: " + text.toString());
						}
					}
				}
			}
		}catch (Exception ex){
			System.out.println(text.toString());
		}	
	}
}
