from textblob import TextBlob
def spelling_checker():
    while True:
        word = input('Enter a word : ')
# checking if the input word is correct 
        if word != TextBlob(word).correct():
           # suggesting the correct word to the user
            question = input(f'Did you mean ' 
                             f'{TextBlob(word).correct()}?. '
                             f'type yes/no :') 
            if question == 'yes':
                break 
            else:
                print("Please try again")
        # if the word entered is correct
        # the code breaks and returns word
        elif word == TextBlob(word).correct(): 
            break
    return f'Your word is, {TextBlob(word).correct()}' 
print(spelling_checker())


# EXTRA CHALLENGE
import winsound
import datetime
def set_alarm():
    # Enter hour
    hour = input("Please enter hour") # Enter minute
    minute = input("Please enter hour")
    # concatenate hour and minute
    alarm_time = hour + ':' + minute
# let the user know the alarm time set
    print("You have set alarm for ", alarm_time)
    while True:
        now = datetime.datetime.now().strftime("%H:%M") 
        if alarm_time == now:
            print("Wake up")
            print("Wake up")
            print("Wake up")
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        break
set_alarm()