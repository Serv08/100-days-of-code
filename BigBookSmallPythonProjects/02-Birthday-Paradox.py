from random import *

# parameter is for the number of randomly generated birthdays
def randomDateGenerator(peeps):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
    days = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    # 31
    days_31 = [0,2,4,6,7,9,11]
    # 30
    days_30 = [3,5,8,10]
    leap = input("\nLeap Year? (yes/no):\t")
    birthday_list = []
    for i in range(peeps):
        rand_month = randint(0,11)
        # dates
        if (leap == "yes") and (rand_month == 1):
            rand_day = randint(0,28)
        elif (leap == "no") and (rand_month == 1):
            rand_day = randint(0,27)
        elif any(days_31):
            rand_day = randint(0,30)
        elif any(days_30):
            rand_day = randint(0,29)

        date = (months[rand_month]+' '+days[rand_day])
        birthday_list.append(date)
    return birthday_list


if __name__ == '__main__':
    people = int(input("Enter the number of people in the room:\t"))

    generated_bday = (randomDateGenerator(people))

    # creates new list that doesn't have repeated birthday 
    bdays =[]
    [bdays.append(item) for item in generated_bday if item not in bdays]
    twin_counter = len(generated_bday) - len(bdays)
    # the probability of having twins in the same room is
    print(generated_bday)
    print("\ntwins:\t{}\npeople:\t{}\n".format(twin_counter,people))
    twins = twin_counter/people
    print(twins,'%')