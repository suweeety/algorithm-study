package 자바코딩개념.문자열과수.문자개수세기;

import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class Main { // 문자 개수를 세는 클래스 선언

    public static void main(String[] args) {

        Map<Character, Integer> test1 = countDuplicateCharacters("Hello");
        for (Map.Entry<Character, Integer> entry : test1.entrySet()) {
            System.out.println(entry.getKey() + " = " + entry.getValue());
        }
        System.out.println("======end======");

        Map<Character, Long> test2 = countDuplicateCharacters2("never");
        for (Map.Entry<Character, Long> entry : test2.entrySet()) {
            System.out.println(entry.getKey() + " = " + entry.getValue());
        }
        System.out.println("======end======");
    }

    public static Map<Character, Integer> countDuplicateCharacters(String str) { // 문자열에서 중복 문자의 개수를 세는 메서드
        Map<Character, Integer> result = new HashMap<>(); // 문자별 개수를 저장할 HashMap 생성

//        for (char ch : str.toCharArray()) { ... } 를 사용해도 됨
        for (int i = 0; i < str.length(); i++) { // 문자열의 각 문자에 대해 반복
            char ch = str.charAt(i); // 현재 인덱스의 문자를 가져옴

            result.compute(ch, (k, v) -> (v == null) ? 1 : ++v); // 해당 문자의 개수를 1 증가시키거나, 처음이면 1로 초기화
        }

        return result; // 문자별 개수 결과 반환
    }

    public static Map<Character, Long> countDuplicateCharacters2(String str) {
        Map<Character, Long> result = str.chars()
                .mapToObj(c -> (char) c)
                .collect(Collectors.groupingBy(c -> c, Collectors.counting()));

        return result;
    }
}
