
import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        Queue<Integer> queue = new LinkedList<>();
        
        for (int i = 0; i < progresses.length; i++) {
            
            // 필요한 작업일 수 개산
            int days = (100 - progresses[i] + speeds[i] - 1) / speeds[i];
            
            // 큐에 저장
            queue.offer(days);
        }

        List<Integer> answerList = new ArrayList<>();

        while (!queue.isEmpty()) {
            int deployDay = queue.poll();
            int count = 1;

            // 뒤에 있는 기능이 현재 기능보다 먼저 완료 되거나 같이 완료 된다면 함께배포
            while (!queue.isEmpty() && queue.peek() <= deployDay) {
                queue.poll();
                count++;
            }

            answerList.add(count);
        }

        return answerList.stream().mapToInt(Integer::intValue).toArray();
        
    }
}