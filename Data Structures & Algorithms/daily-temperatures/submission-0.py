class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0 for _ in range(len(temperatures))]
        stack = []
        for day_num, today_temp in enumerate(temperatures):

            while stack and today_temp > stack[-1]["temp"]:
                top = stack[-1]
                days[top["day_num"]] = day_num - top["day_num"]
                stack.pop()

            stack.append({
                "temp": today_temp, 
                "day_num": day_num
            })
        
        return days
