import datetime

class Reminder:
    def __init__(self, date, event):
        self.date = date
        self.event = event


def schedule_input():
    while True:
        try:
            date_input = input("Please enter your date for events (MM-DD-YYYY): ")
            date = datetime.datetime.strptime(date_input, "%m-%d-%Y").date()
            event = input("Descriptions for the event: ")
            reminder = Reminder(date, event)
            return reminder
        
        except ValueError:
            print("Invalid input, please enter your date in the right form (MM-DD-YYYY)")

def storer(schedule_input):
    schedule_list = list(schedule_list)
    schedule_list = schedule_list.append(schedule_input)
    return schedule_list

def schedule_finder(date, schedule_list):
    item = date
    schedule = [item for item in schedule_list if isinstance(item, Reminder)]


# class MyClass:
#     pass

# my_list = [1, "hello", MyClass(), 3.14, MyClass()]

# my_class_instances = [item for item in my_list if isinstance(item, MyClass)]

# print("Instances of MyClass:", my_class_instances)

# class MyClass:
#     pass

# my_list = [1, "hello", MyClass(), 3.14, MyClass()]

# my_class_instances = list(filter(lambda item: isinstance(item, MyClass), my_list))

# print("Instances of MyClass:", my_class_instances)





def game():
    schedule = schedule_input()
    print(schedule.date, schedule.event)
    schedule_list = storer(schedule)


if __name__ == "__main__":
    game()