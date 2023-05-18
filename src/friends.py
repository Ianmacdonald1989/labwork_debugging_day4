def get_name(person):
    result = person["name"]
    return result

def get_favourite_tv_show(person):
    result = person["favourites"]["tv_show"]
    return result

def likes_to_eat(person, food):
    snacks = person["favourites"]["snacks"]
    if food in snacks:
        return True 
    
    return False

def add_friend(person, friend):
    person["friends"].append("friend")

def remove_friend(person, friend):
    person["friends"].remove("friend")
 
def total_money(persons):
    total = 0 
    for person in persons:
        amount = person["monies"]
        total = total + amount 
    return total    

def lend_money(lender, lendee, amount):
    lender["monies"] -= amount
    lendee["monies"] += amount 


def all_favourite_foods(people):
    favourite_foods = []
    for person in people:
        for snack in person["favourites"]["snacks"]:
            favourite_foods.append(snack)

    return favourite_foods

def find_no_friends(people):
    no_mates = []
    for person in people:
        if len(person["friends"]) == 0:
            no_mates.append(person)

    return no_mates
    

def unique_favourite_tv_shows(people):
    unique_tv_shows = []
    for person in people:
        if person["favourites"]["tv_show"] not in unique_tv_shows:
            unique_tv_shows.append(person["favourites"]["tv_show"])

    return unique_tv_shows

