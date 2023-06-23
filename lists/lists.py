class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        if not input_list:
            return input_list

        max_value = input_list[0]
        for num in input_list:
            if num > max_value:
                max_value = num

        i = 0
        while i < len(input_list):
            if input_list[i] > 0:
                input_list[i] = max_value
            i += 1
        return input_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        def recur_search(low, high):
            if low > high:
                return -1

            mid = (low + high) // 2

            if input_list[mid] == query:
                return mid
            elif input_list[mid] > query:
                return recur_search(low, mid - 1)
            else:
                return recur_search(mid + 1, high)

        return recur_search(0, len(input_list) - 1)
