def vowels_count(a):
    vowels = []
    for word in a.split():
        for i in word:
            if i in 'aeiou':
                if word not in vowels: vowels.append(word)
    return vowels
print(vowels_count('You have no rhythm'))

# EXTRA CHALLENGE
class Cars:
    def __init__(self, model, color, year,
                transmission, electric=False): 
        self.model = model
        self.color = color
        self.year = year 
        self.transmission = transmission 
        self.electric = electric
# Creating the class method
    def print_car(self):
        return f'car_model = {self.model}\nColor = ' \ 
               f'{self.color} \nYear = {self.year}' \
               f' \nTransmission = {self.transmission} ' \
               f'\nElectric = {self.electric}'
               
class BMW(Cars):
    def __init__(self, model, color, year,
                transmission, electric=False): 
        Cars.__init__(self, model, color, year,
                transmission, electric=electric)
        
class Tesla(Cars):
    def __init__(self, model, color, year,
                transmission, electric=False):
        Cars.__init__(self, model, color, year,
                transmission, electric=electric)
        
class Ford(Cars):
    def __init__(self, model, color, year,
                transmission, electric=False): Cars.__init__(self, model, color, year,
                transmission, electric=electric)
# instantiating class objects
ford1 = Ford("Focus", "White", 2017, "Auto", False)
print(ford1.print_car())
tesla1 = Tesla("S", "Grey", 2016, "Manual", True)
print(tesla1.print_car())
bmw1 = BMW('X6', 'silver', 2018, 'Auto', False) 
print(bmw1.print_car())