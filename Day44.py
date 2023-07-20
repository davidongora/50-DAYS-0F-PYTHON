def save_emails():
    w = []
    while True:
        email = input("Enter your email: ")
        w.append(email)
        if email == 'done':
            break
        with open('emails.csv', 'a') as f:
            f. write(email)
            f .write('\n')
# Second function to read emails
def open_emails():
    with open('emails.csv', 'r') as f:
        return f.read()
save_emails()
print(open_emails())