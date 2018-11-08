
import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class WCMapper extends Mapper<Object, Text, Text, IntWritable> {
	private final static IntWritable one = new IntWritable(1);
	private Text word = new Text();
	
	public void map(Object key, Text text, Context context) throws IOException, InterruptedException{
		String input = text.toString().replaceAll("\\p{Punct}",""); 
		String[] lists =  input.split(" ");
		for (int i=0; i<lists.length; i++) {
			word.set(lists[i]);
			context.write(word, one);
		}
	}

}
