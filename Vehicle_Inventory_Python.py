print("Welcome to our ITS320 vehicle inventory system!")
option=0
index_position=0
cars=[]

class Vehicle:
    def __init__(self):
        self.make = ' '
        self.model = ' '
        self.color = ' '
        self.year = 0
        self.mileage = 0

    def __str__(self):
        self.make = input('Enter make: ')
        self.model = input('Enter model: ')
        self.color = input('Enter color: ')
        self.year = int(input('Enter year (YYYY): '))
        self.mileage = int(input('Enter mileage: '))
        return '{} {} {} {} with {} miles'.format(self.color,self.year,self.make,self.model,self.mileage)

def list_cars():
    for index, car in enumerate(cars):
        print(index, car)
        
def no_option():
    print('Option Not Supported!')

def index_choice():
    print('Index Number & Vehicle:')
    list_cars()
    index_position = int(input('\nEnter Index Position:\n'))
    return index_position
    
car = Vehicle()

while option != 6:
    option = int(input('\nSelect an Option:\n1: Add Vehicle\n2: Remove Vehicle\n3: Update Attributes\n4: View Inventory\n5: Export Inventory\n6: Exit\n'))
    if option == 1:
        sub_option=0
        while sub_option != 2:
            sub_option = int(input('\n1: Add Vehicle\n2: Return to Main Menu\n'))
            if sub_option == 1:
                print('Adding Vehicle')
                cars.append(car.__str__())
                print('\nSuccessfully added!')
            elif sub_option == 2:
                print('Returning to Main Menu')
            else:
                no_option()
    elif option == 2:
        sub_option1=0
        while sub_option1 != 2:
            sub_option1 = int(input('\n1: Remove Vehicle by Index\n2: Return to Main Menu\n'))
            if sub_option1 == 1:
                removed_car = cars.pop(index_choice())
                print('%s Removed!' % removed_car)
            elif sub_option1 == 2:
                print('Returning to Main Menu')
            else:
                no_option()
    elif option == 3:
        sub_option2=0
        while sub_option2 != 2:
            sub_option2 = int(input('\n1: Edit Attributes by Index\n2: Return to Main Menu\n'))
            if sub_option2 == 1:
                attribute_update= index_choice()
                cars[attribute_update] = car.__str__()
                print('Attributes Editted!')
            elif sub_option2 == 2:
                print('Returning to Main Menu')
            else:
                no_option()
        pass
    elif option == 4:
        print('Current inventory:')
        list_cars()
    elif option == 5:
        f = open('Inventory.txt', 'w')
        f.write(str(cars))
        f.close()
        print('Inventory exported')
    elif option == 6:
        print('Program terminated.\nGoodbye!')
    else:
        no_option()
        


