prompt = "Enter your 5 favourite movies"
prompt += "\nEnter 'quit' when you are finished: "

movie_list = []
while True:
    movie = input(prompt)
    if movie == 'quit':
        break
    movie = str(movie)
    movie_list.append(movie)
print(movie_list)
