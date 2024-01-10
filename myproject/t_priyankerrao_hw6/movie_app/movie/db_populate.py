from movie.models import Movie, User
def perform_db_operations():
    # Delete all Movie instances
    Movie.objects.all().delete()

    # Delete all User instances
    User.objects.all().delete()

    # Add 10 Movie instances
    for i in range(10):
        Movie.objects.create(
            title=f'Movie Title {i}',
            description=f'Description for Movie Title {i}',
            director=f'Director {i}',
            release_year=f'Year {i}',
            budget=f'Budget {i}',
            runtime=f'Runtime {i}',
            rating=f'Rating {i}',
            genre=f'Genre {i}',
        )

    # Add 3 User instances
    users_data = [
        {'username': 'user1', 'password': 'pass1', 'first_name': 'User', 'last_name': 'One', 'email': 'user1@example.com'},
        {'username': 'user2', 'password': 'pass2', 'first_name': 'User', 'last_name': 'Two', 'email': 'user2@example.com'},
        {'username': 'user3', 'password': 'pass3', 'first_name': 'User', 'last_name': 'Three', 'email': 'user3@example.com'},
    ]
    for user in users_data:
        User.objects.create(**user)


    # Retrieve all movies
    all_movies = Movie.objects.all()

    # Filter for movies starting with some text
    movies_starting_with = Movie.objects.filter(title__startswith='Movie')

    # Get one movie by ID
    one_movie = Movie.objects.get(pk=51)

    # Update one movie by ID
    one_movie.title='New Movie Title'

    # Delete one movie by ID
    Movie.objects.get(pk=51).delete()

    # Get data for user given a username
    user_data = User.objects.get(username='user1')
