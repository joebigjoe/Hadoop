import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class LocaleCount {
	public static void main(String[] args) {
		Configuration conf =new Configuration();
		try {
			Job job = Job.getInstance(conf, "Locale Count Joey");
			job.setJarByClass(LocaleCount.class);
			job.setMapperClass(KWMapper.class);
			job.setCombinerClass(LCReducer.class);
			job.setReducerClass(LCReducer.class);
			job.setOutputKeyClass(Text.class);
			job.setOutputValueClass(IntWritable.class);
			//job.setSortComparatorClass(IntComparator.class);
			FileInputFormat.addInputPath(job, new Path(args[0]));
			FileOutputFormat.setOutputPath(job, new Path(args[1]));
			try {
				System.exit(job.waitForCompletion(true)? 0:1);
			} catch (ClassNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
