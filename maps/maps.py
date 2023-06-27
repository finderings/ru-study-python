from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        def necessary_rating(x: dict) -> float:
            rating = x.get("rating_kinopoisk")
            if rating and rating != "0" and len(x.get("country", "").split(",")) >= 2:
                return float(rating)
            return 0.0

        apply_rating = map(necessary_rating, list_of_movies)

        valid_rating = list(filter(lambda y: y != 0.0, apply_rating))
        if valid_rating:
            average_rating = sum(valid_rating) / len(valid_rating)
            return average_rating
        else:
            return 0.0

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        def necessary_rating(x: dict) -> dict:
            rate = x.get("rating_kinopoisk")
            if rate and float(rate) >= float(rating):
                return x
            return {}

        filtered_movies = list(map(necessary_rating, list_of_movies))

        titles = list(map(lambda movie: movie.get("name", ""), filtered_movies))
        count = sum(map(lambda title: title.count("и"), titles))
        return count
