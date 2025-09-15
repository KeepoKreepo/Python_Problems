cinema_halls = int(input())
hall_capacity = int(input())
movie_goers = int(input())

if cinema_halls * hall_capacity >= movie_goers:
    print('True')
else:
    print('False')