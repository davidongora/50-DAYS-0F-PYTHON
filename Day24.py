def average_calories():
    scores = []
    while True:
        score = input('Enter a score or done when quit: ') 
        if score == 'done':
            break
        scores.append(int(score))
    return f" Mean of scores is " \
f"{sum(scores) / len(scores):.2f}"
print(average_calories())

# EXTRA CHALLENGE
def nested_lists(*args: list):
    list1 =[]
    for i in range(len(args)):
        for j in args:
            list1.append(j)
        break
    return list1
print(nested_lists([1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]))