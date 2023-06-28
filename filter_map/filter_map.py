from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        if input_array == []:
            return input_array

        result = []
        for value in input_array:
            bool_type, result_func = func(value)
            if bool_type:
                result.append(result_func)

        return result
