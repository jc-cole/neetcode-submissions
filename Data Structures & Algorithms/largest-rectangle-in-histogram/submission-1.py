class Solution:

    # make list of bar indicies max -> min
    # max = 0
    # probe left
    # probe right
    # if num_cols * height of initial col > max: max = that num
    # repeat while this col height * total cols > max
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        highest_at_top_stack = sorted(enumerate(heights), key=lambda pair:pair[1])

        debug_count = 0

        current_max = 0
        my_index, my_height = highest_at_top_stack[-1]
        while (my_height * len(heights) > current_max):

            print(f"current max: {current_max}")
            print(f"current index: {my_index}")
            print(f"current height: {my_height}")

            total_adjacent_cols = 1

            i = my_index # current probe index

            #probe left
            while (i-1 >= 0 and heights[i-1] >= my_height):
                total_adjacent_cols += 1
                i -= 1
            
            i = my_index
            #probe right
            while (i+1 < len(heights) and heights[i+1] >= my_height):
                total_adjacent_cols += 1
                i += 1

            print(f"total cols found: {total_adjacent_cols}")

            this_max = total_adjacent_cols * my_height
            print(f"max from this col: {this_max}\n")
            if (this_max > current_max):
                current_max = this_max

            highest_at_top_stack.pop()
            if (highest_at_top_stack):
                my_index, my_height = highest_at_top_stack[-1]
                # debug_count += 1
                # if (debug_count == 7):
                #     break
            else:
                break
        
        return current_max
        



