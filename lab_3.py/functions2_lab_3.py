#Task 1
def true_rating(movies):
    return movies["imdb"] > 5.5

#Task 2
def high_rating(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

#Task 3
def category(movies, category):
    return [movie for movie in movies if movie["category"].lower() == category.lower()]

#Task 4
def calculate_rating(movies):
    total_rating = sum(movie["imdb"] for movie in movies)
    return total_rating / len(movies)

#Task 5
def calculate_category(movies, category):
    category_movies = category(movies, category)
    return calculate_category(category_movies)
