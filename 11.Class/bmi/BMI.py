class BMI:
    def __init__(self, weight, height):
        self.__weight = weight
        self.__height = height
        
    def bmi_level(data):
        bmi_2 = data.__weight / ((data.__height/100) ** 2)
        print('%.2f'%bmi_2)
        
        if bmi_2 < 18.5:
            print('Underweight')
        elif bmi_2 < 25:
            print('Normal')
        elif bmi_2 < 30:
            print('Overweight')
        else:
            print('Obses')
            
   def Taekwondo_level(man):
        if man.__weight < 58:
            print('蠅量級')
        elif man.__weight < 68:
            print('輕量級')
        elif man.__weight < 80:
            print('中量級')
        else:
            print('重量級')