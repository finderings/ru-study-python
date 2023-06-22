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

        low = 0
        high = len(input_list) - 1

        while low <= high:
            mid = (low + high) // 2
            if input_list[mid] == query:
                return mid
            if input_list[mid] > query:
                high = mid - 1
            else:
                low = mid + 1
        return -1
