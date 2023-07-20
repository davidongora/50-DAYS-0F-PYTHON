def get_marks():
    d = {}
    while True:
        name = input('Enter the student name or done: ') 
        if name == 'done':
            break
        marks = int(input('Enter the marks: '))
        d[name] = d.get(marks, 0) + marks
    return d
print(get_marks())