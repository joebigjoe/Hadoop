package joey.test;

import java.io.IOException;
import java.util.*;

import org.apache.pig.EvalFunc;
import org.apache.pig.data.Tuple;

public class CountGenres extends EvalFunc<String> {

	@Override
	public String exec(Tuple input) throws IOException {
		// TODO Auto-generated method stub
		if (input == null || input.size() == 0 || input.get(0) == null || input.get(0).equals(""))
			return null;
		String str = (String) input.get(0);
		try {
			String finalstr = "";
			String[] geners = str.split(",");
			for (int i = 0; i < geners.length; i++) {
				if (!finalstr.contains(geners[i]) && !geners[i].contains("no genres listed")) {
					int counter = 0;
					for (int j = 0; j < geners.length; j++) {
						if (geners[i].equals(geners[j])) {
							counter++;
						}
					}
					finalstr += geners[i] + "(" + Integer.toString(counter) + ")|";
				}
			}
			finalstr = finalstr.substring(0, finalstr.length() - 1);

			// sort them
			Map<String, Integer> unsortMap = new HashMap<String, Integer>();
			String[] genreswithcount = finalstr.split("\\|");
			for (int i = 0; i < genreswithcount.length; i++) {
				String key = genreswithcount[i].substring(0, genreswithcount[i].indexOf("("));
				Integer value = Integer.parseInt(genreswithcount[i].substring(genreswithcount[i].indexOf("(") + 1,
						genreswithcount[i].indexOf(")")));
				unsortMap.put(key, value);
			}

			Map<String, Integer> sortedMap = sortByValue(unsortMap);
			finalstr = "";

			for (Map.Entry<String, Integer> entry : sortedMap.entrySet()) {
				finalstr += entry.getKey() + "(" + Integer.toString(entry.getValue()) + ")|";
			}

			finalstr = finalstr.substring(0, finalstr.length() - 1);
			return finalstr;
			
		} catch (Exception e) {
			System.out.println(str);
			throw new IOException("Caught exception processing input row ", e);
		}
	}

	private Map<String, Integer> sortByValue(Map<String, Integer> unsortMap) {

		// 1. Convert Map to List of Map
		List<Map.Entry<String, Integer>> list = new LinkedList<Map.Entry<String, Integer>>(unsortMap.entrySet());

		// 2. Sort list with Collections.sort(), provide a custom Comparator
		// Try switch the o1 o2 position for a different order
		Collections.sort(list, new Comparator<Map.Entry<String, Integer>>() {
			public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
				return (o2.getValue()).compareTo(o1.getValue());
			}
		});

		// 3. Loop the sorted list and put it into a new insertion order Map
		// LinkedHashMap
		Map<String, Integer> sortedMap = new LinkedHashMap<String, Integer>();
		for (Map.Entry<String, Integer> entry : list) {
			sortedMap.put(entry.getKey(), entry.getValue());
		}

		/*
		 * //classic iterator example for (Iterator<Map.Entry<String, Integer>> it =
		 * list.iterator(); it.hasNext(); ) { Map.Entry<String, Integer> entry =
		 * it.next(); sortedMap.put(entry.getKey(), entry.getValue()); }
		 */

		return sortedMap;
	}
}
