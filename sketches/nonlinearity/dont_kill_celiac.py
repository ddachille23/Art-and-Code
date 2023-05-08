# -*- coding: utf-8 -*-

## Don't Kill the Celiac Game

# Imports
import string
from time import sleep
import time
import threading
import os
import random
import sys

# Constants
GAME_LENGTH_MINS = 10 # minutes (change this one to change the game length)
GAME_LENGTH_SECS = GAME_LENGTH_MINS*60
GENERAL_TYPING_SPEED = 0.007

# Global variables
global remaining_time
name = ""
shopping_list = []
cart_items = []
health = 100

# Classes
class food_item:
    def __init__(self, name, food_category, is_gluten_free, ingredients, reasons_why_its_not_gf):
        self.name = name
        self.food_category = food_category
        self.is_gluten_free = is_gluten_free
        self.ingredients = ingredients
        self.reasons_why_its_not_gf = reasons_why_its_not_gf

## Foods 
# Sushi
eel_roll = food_item("Eel Rolls", "sushi", False, ["rice", "seaweed", "eel", "eel sauce"], "typically made with gluten containing soy sauce")
tuna_roll = food_item("Tuna Rolls", "sushi", True, ["rice", "seaweed", "salmon", "avocado"], "")
shrimp_tempura_roll = food_item("Shrimp Tempura Rolls", "sushi", False, ["rice", "seaweed", "shrimp", "tempura batter"], "have tempura batter")
california_roll = food_item("California Rolls", "sushi", False, ["rice", "seaweed", "avocado", "cucumber", "imitation crab"], "contain imitation crab")

# grains - oats
quaker_quick_oats = food_item("Quaker Quick 1-Minute Oats", "oats", False, ["whole grain rolled oats"], "are cross contaminated with wheat") 
trader_joes_rolled_oats = food_item("Trader Joe's Rolled Oats", "oats", True, ["whole grain rolled oats"], "")
quaker_old_fashioned_oats = food_item("Quaker Old Fashioned Oats", "oats", False, ["whole grain rolled oats"], "are cross contaminated with wheat")
kelloggs_rolled_oats = food_item("Kellogg's Rolled Oats", "oats", False, ["whole grain rolled oats"], "are cross contaminated with wheat")
oats_array = [quaker_quick_oats, trader_joes_rolled_oats, quaker_old_fashioned_oats, kelloggs_rolled_oats]

# grains - cereal
cinnamon_toast_crunch = food_item("Cinnamon Toast Crunch", "cereal", False, ["Whole Grain Wheat", "Sugar", "Rice Flour", "Sunflower Oil", "Fructose", "Maltodextrin", "Dextrose", "Salt", "Cinnamon", "Trisodium Phosphate", "Soy Lecithin", "Caramel Color"], "contains whole grain wheat")
fruity_pebbles = food_item("Fruity Pebbles", "cereal", True, ["Rice", "Sugar", "Hydrogenated" "Vegetable Oil", "Salt", "Natural and Artificial Flavor", "Red 40", "Yellow 6", "Turmeric Oleoresin", "Blue 1", "Yellow 5", "Blue 2", "BHA", "Sodium Ascorbate", "Ascorbic Acid", "Niacinamide", "Reduced Iron", "Zinc Oxide", "Vitamin B6", "Vitamin A Palmitate", "Riboflavin", "Thiamin Mononitrate", "Folic Acid", "Vitamin B12", "Vitamin D3"], "")
mini_wheats = food_item("Frosted Mini Wheats", "cereal", False, ["Whole Grain Wheat", "Sugar", "Whole Wheat Flour", "Brown Rice Syrup", "Gelatin", "Vegetable Juice", "Natural and Artificial Flavors", "Citric Acid", "Paprika Extract Color", "Beta-Carotene", "BHT", "Reduced iron", "Folic Acid"], "contain whole grain wheat and whole wheat flour")
frosted_flakes = food_item("Frosted Flakes", "cereal", False, ["Milled Corn", "Sugar", "Malt Flavor", "Niacinamide", "Vitamin B6/B2/B1/D3/B12", "Folic Acid"], "contain malt flavor")

# grains - pasta
jovial_brown_rice = food_item("Jovial Brown Rice Penne", "pasta", True, ["Organic Brown Rice Flour", "Water"], "")
barilla_capellini = food_item("Barilla Capellini", "pasta", False, ["Semonila (wheat)", "Durum Wheat Flour", "Vitamin B3", "Iron", "Vitamin B1", "Folic Acid"], "contains semolina (milled wheat) and durum wheat flour")
de_cecco_penne = food_item("De Cecco Penne", "pasta", False, ["Durum Wheat Semonila", "Water", "Niacin", "Thiamine Mononitrate", "Riboflavin", "Folic Acid", "Iron"], "contains durum wheat semonila")
voiello_spaghetti = food_item("Voiello Spaghetti", "pasta", False, ["Durum Wheat Flour", "Water"], "contains durum wheat flour")

# snacks - protein bars
clif_bar = food_item("Chocolate Chip Clif Bars", "protein bars", False, ["Organic Rolled Oats", "Organic Brown Rice Syrup", "Organic Soy Protein Isolate", "Organic Date Paste", "Organic Almonds", "Organic Tapioca Syrup", "Organic Roasted Soybeans", "Organic Roasted Soy Flour", "Organic Soy Flour", "Organic Cane Syrup", "Organic Crisp Rice (Organic Rice Flour", "Organic Barley Malt", "Organic Barley Syrup", "Sea Salt", "Organic Soy Lecithin", "Organic Vanilla Extract", "Organic Sunflower Oil", "Organic Tocopherols", "Vitamin E"], "contain organic rolled oats")
fiber_one_bar = food_item("Fiber One Chewy Protein Bars", "protein bars", False, ["ORGANIC ROLLED OATS", "ORGANIC BROWN RICE SYRUP", "SOY RICE CRISPS (SOY PROTEIN ISOLATE, RICE FLOUR, BARLEY MALT EXTRACT)", "ORGANIC ROASTED SOYBEANS", "ORGANIC TAPIOCA SYRUP", "ORGANIC CANE SYRUP", "UNSWEETENED CHOCOLATE", "CHICORY FIBER", "ORGANIC SOY FLOUR", "SUNFLOWER AND/OR SOYBEAN OIL", "NATURAL FLAVORS", "SALT", "ORGANIC CINNAMON", "MIXED TOCOPHEROLS (ANTIOXIDANT)"], "contain barley malt extract")
rx_bar = food_item("Chocolate Chip RX Bars", "protein bars", True, ["Dates", "Egg Whites", "Almonds", "Cashews", "Chocolate", "Natural Flavors", "Sea Salt"], "")
special_k_bar = food_item("Special K Chocolately Chip Cookie Dough Protein Bars", "protein bars", False, [""], "contain wheat starch and contaminated oats")

# condiments - soy sauce
tamari_soy_sauce = food_item("San-J Tamari Soy Sauce", "soy sauce", True, ["Water", "Soybeans", "Salt", "Alcohol"], "")
kikkoman_soy_sauce = food_item("Kikkoman Soy Sauce", "soy sauce", False, ["Water", "Wheat", "Soybeans", "Salt", "Alcohol"], "contains wheat")
great_value_soy_sauce = food_item("Great Value Soy Sauce", "soy sauce", False, ["Water", "Wheat", "Soybeans", "Salt", "Alcohol"], "contains wheat")
aloha_soy_sauce = food_item("Aloha Soy Sauce", "soy sauce", False, ["Water", "Wheat", "Soybeans", "Salt", "Alcohol"], "contains wheat")

# beer
bud_light = food_item("Bud Light", "beer", False, ["Water", "Barley", "Rice", "Hops"], "contains barley")
coors_light = food_item("Coors Light", "beer", False, ["Water", "Barley Malt", "Corn Syrup", "Yeast", "Hops Extract"], "contains barley malt")
bards_tail = food_item("Bard's Tail", "beer", True, ["Malted Sorghum", "Water", "Yeast"], "")
heineken = food_item("Heineken", "beer", False, ["Malted Barley", "Hop Extract", "Water"], "contains malted barley")


# Functions
def countdown_timer(duration):
    global elapsed_time
    global remaining_time
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        remaining_time = duration - elapsed_time
        
        if remaining_time <= 0:
            print("\nTime's up! You died of starvation (✖╭╮✖)")
            os._exit(0)

def print_animated(words, speed = GENERAL_TYPING_SPEED, newline = True):
    for char in words:
        sleep(speed)
        print(char, end = '', flush = True)
    if newline == True:
        print("")

def seconds_to_minutes_and_seconds(seconds):
    minutes = int(seconds/60)
    seconds = int(seconds%60)
    return minutes, seconds

def check_time(version = "normal"):
    time_left = seconds_to_minutes_and_seconds(remaining_time)
    minutes_left = time_left[0]
    seconds_left = time_left[1]
    
    if version == "normal":
        print("There are " + str(minutes_left) + " minutes and " + str(seconds_left) + " seconds left!")
    else:
        print("You got all the GF items in your cart with " + str(minutes_left) + " minutes and " + str(seconds_left) + " seconds left!")

def generate_shopping_list():
    global shopping_list
    all_possible_items = ["beer", "oats", "cereal", "pasta", "soy sauce", "protein bars", "sushi"] 
    shopping_list = random.sample(all_possible_items, 5) # randomly select 5 items from the list without replacement
    return shopping_list

def quit_game():
    print_animated("Goodbye!")
    os._exit(0)
    
def game_intro(): 
    global name
    print_animated("** WELCOME TO DON'T KILL THE CELIAC **")
    print_animated("Celiac is a genetic autoimmune disorder that affects 1 in 100 people in the United States.")
    print_animated("Celiacs cannot eat gluten, a protein found in wheat, malt, barley, and rye.")
    print_animated("If a celiac eats gluten, their immune system attacks their small intestine, causing damage and inflammation.")
    print_animated("What is your name?")
    name = input()
    name = string.capwords(name)
    print_animated(name + ", you are a celiac at Big Y and you have to find all the items on your shopping list before you go starving!")
    time.sleep(0.5)
    print_animated("The store has at least one gluten free version of each item on your list.")
    time.sleep(0.5)
    print_animated("You have " + str(GAME_LENGTH_MINS) + " minutes to add all the gluten free items to your cart!")
    time.sleep(0.5)
    print_animated("For each gluten containing item you add to your cart, your health diminishes by 20%.")
    time.sleep(0.5)
    print_animated("If your health reaches 0%, you die of starvation (✖╭╮✖)")
    time.sleep(0.5)
    print_animated("You currently have full health ", newline=False)
    show_health(health, animate=True)
    print()
    print_animated("Good luck!") 
    time.sleep(0.5)

    text = "_"
    while text != "": 
        print_animated("Press enter to start the game and see your shopping list! (type quit to exit the game at any time)")
        text = input()
        text = text.lower()
        if text == "quit":
            print_animated("Are you sure you want to quit? (yes/no)")
            response = input()
            response = response.lower()
            if "yes" in response:
                quit_game()
            else:
                continue

    # start the game
    num_gluten_items = 0
    print_animated("Here is your shopping list:")
    shopping_list = generate_shopping_list()
    for count, item in enumerate(shopping_list):
        print_animated("\t" + str(count+1) + ". " + string.capwords(item), speed=0.04)
    print_animated("Your " + str(GAME_LENGTH_MINS) + " minute timer starts now!")
    timer.start()

def entrance():
    while True:
        print_animated("You are at the Big Y entrance. You can:")
        print_animated("\t1. Go to the dairy/eggs aisle")
        print_animated("\t2. Go to the cleaning/pet supplies aisle")
        response = input()
        response = response.lower()
        if response == "quit":
            print_animated("Are you sure you want to quit? (yes/no)")
            quit_ans = input()
            quit_ans = quit_ans.lower()
            if "yes" in quit_ans:
                quit_game()
            else:
                continue
        elif response == "1" or "dairy" in response or "eggs" in response:
            eggs_dairy_section()
        elif response == "2" or "cleaning" in response or "pet" in response:
            cleaning_pets_section()
        else:
            print_animated("I don't understand what '" + response + "' means. Please try again.")
            continue
        break


def eggs_dairy_section():
    while True:
        print_animated("As you stroll down the aisle, you feel the cold refrigerated air brush your skin as the pungent smell of eggs and cheese hits you.")
        print_animated("You can:")
        print_animated("\t1. Explore the refrigerators")
        print_animated("\t2. Go to to the cleaning/pet supplies aisle")
        print_animated("\t3. Go to to the snacks/candy/condiments aisle")
        print_animated("\t4. Go back to the entrance")
        response = input()
        response = response.lower()
        if response == "quit":
            print_animated("Are you sure you want to quit? (yes/no)")
            quit_ans = input()
            quit_ans = quit_ans.lower()
            if "yes" in quit_ans:
                quit_game()
            else:
                continue
        elif response == "1" or "explore" in response or "refrigerators" in response:
            print_animated("None of these items are on your shopping list. Keep shopping.")
        elif response == "2" or "cleaning" in response or "pet" in response or "into" in response or "turn" in response:
            cleaning_pets_section()
        elif response == "3" or "snacks" in response or "candy" in response or "condiments" in response:
            snacks_candy_condiments()
        elif response == "4" or "back" in response or "entrance" in response:
            entrance()
        else:
            print_animated("I don't understand what '" + response + "' means. Please try again.")
            continue

def cleaning_pets_section():
    print_animated("In the cleaning/pet supplies aisle, you see a woman shopping for kibble with her chihuahua.")
    print_animated("Oh no! As you peruse the aisle, you feel your feet slip from under you and you suddenly fall to the ground.")
    print_animated("You look up and see a puddle of pee on the floor.")
    print_animated("You've injured yourself and lost 20% of your health! ", newline=False)
    reduce_health()
    while True:
        print_animated("You can:")
        print_animated("\t1. Lie on the floor in agony")
        print_animated("\t2. Go to the eggs/dairy aisle")
        print_animated("\t3. Go to the snacks/candy/condiments aisle")
        print_animated("\t4. Go to the grain aisle")
        print_animated("\t5. Go back to the entrance")
        response = input()
        response = response.lower()
        if response == "quit":
            print_animated("Are you sure you want to quit? (yes/no)")
            quit_ans = input()
            quit_ans = quit_ans.lower()
            if "yes" in quit_ans:
                quit_game()
            else:
                continue
        elif response == "1" or "lie" in response or "floor" in response or "agony" in response:
            lie_in_agony()
        elif response == "2" or "dairy" in response or "eggs" in response:
            eggs_dairy_section()
        elif response == "3" or "snack" in response or "candy" in response or "condiments" in response:
            snacks_candy_condiments()
        elif response == "4" or "grain" in response:
            grain_section()
        elif response == "5" or "back" in response or "entrance" in response:
            entrance()
        else:
            print_animated("I don't understand what '" + response + "' means. Please try again.")
            continue
        break

def lie_in_agony():
    print_animated("You are lying on the floor, with your head soaking in a puddle of chihuahua pee.")
    print_animated("You open your eyes and see the chihauna's owner standing over you.")
    print_animated("She says, 'Oh my gosh, I'm so sorry! I didn't see you there! Are you okay?'")
    print_animated("As you open your mouth to respond, a GLUTINOUS dog treat falls out of her pocket and lands in your mouth 😱.")
    print_animated("You have ingested gluten and lost 20% of your health! ", newline=False)
    reduce_health()
    while True:
        print_animated("You can:")
        print_animated("\t1. Go to the eggs/dairy aisle")
        print_animated("\t2. Go to the snack/candy/condiments aisle")
        print_animated("\t3. Go to the grain aisle")
        print_animated("\t4. Go back to the entrance")
        response = input()
        response = response.lower()
        if response == "quit":
            print_animated("Are you sure you want to quit? (yes/no)")
            quit_ans = input()
            quit_ans = quit_ans.lower()
            if "yes" in quit_ans:
                quit_game()
            else:
                continue
        elif response == "1" or "dairy" in response or "eggs" in response:
            eggs_dairy_section()
        elif response == "2" or "snack" in response or "candy" in response or "condiments" in response:
            snacks_candy_condiments()
        elif response == "3" or "grain" in response:
            grain_section()
        elif response == "4" or "back" in response or "entrance" in response:
            entrance()
        else:
            print_animated("I don't understand what '" + response + "' means. Please try again.")
            continue

def snacks_candy_condiments():
     while True:
        print_animated("You are in the snacks/candy/condiments aisle.")
        print_animated("You can:")
        print_animated("\t1. Explore the items")
        print_animated("\t2. Go to the eggs/dairy aisle")
        print_animated("\t3. Go to to the cleaning/pet supplies aisle")
        print_animated("\t4. Go to to the grain aisle")
        print_animated("\t5. Go to to the beverages aisle")
        response = input()
        response = response.lower()
        if response == "quit":
            print_animated("Are you sure you want to quit? (yes/no)")
            quit_ans = input()
            quit_ans = quit_ans.lower()
            if "yes" in quit_ans:
                quit_game()
            else:
                continue
        elif response == "1" or "explore" in response or "itmes" in response:
            explore_snacks_candy_condiments()
        elif response == "2" or "dairy" in response or "eggs" in response:
            eggs_dairy_section()
        elif response == "3" or "cleaning" in response or "pet" in response or "supplies" in response:
            cleaning_pets_section()
        elif response == "4" or "grain" in response:
            grain_section()
        elif response == "5" or "beverages" in response:
            beverages_section()
        else:
            print_animated("I don't understand what '" + response + "' means. Please try again.")
            continue

def grain_section():
    while True:
        print_animated("You are in the grain aisle.")
        print_animated("You can:")
        print_animated("\t1. Explore the items")
        print_animated("\t2. Go to the cleaning/pet supplies aisle")
        print_animated("\t3. Go to to the snacks/candy/condiments aisle")
        print_animated("\t4. Go to to the beverage aisle")
        response = input()
        response = response.lower()
        if response == "quit":
            print_animated("Are you sure you want to quit? (yes/no)")
            quit_ans = input()
            quit_ans = quit_ans.lower()
            if "yes" in quit_ans:
                quit_game()
            else:
                continue
        elif response == "1" or "explore" in response or "itmes" in response:
            explore_grain_section()
        elif response == "2" or "cleaning" in response or "pet" in response or "supplies" in response:
            cleaning_pets_section()
        elif response == "3" or "snacks" in response or "candy" in response or "condiments" in response:
            snacks_candy_condiments()
        elif response == "4" or "beverage" in response or "drinks" in response:
            beverages_section()
        else:
            print_animated("I don't understand what '" + response + "' means. Please try again.")
            continue

def reduce_health(amount=20):
    global health
    old_health = health # store old health to use in health reduction animation
    health -= amount
    show_health(old_health, amount)
    print()
    print_animated("Your health is now " + str(health) + "% ")
    if health == 0:
        print_animated("You've died! Game over.")
        quit_game()

def explore_grain_section():
    while True:
        print_animated("You can:")
        print_animated("\t1. Look at the oats")
        print_animated("\t2. Look at the cereals")
        print_animated("\t3. Look at the pastas")
        print_animated("\t4. Go back")
        response = input()
        response = response.lower()
        if response == "quit":
            print_animated("Are you sure you want to quit? (yes/no)")
            quit_ans = input()
            quit_ans = quit_ans.lower()
            if "yes" in quit_ans:
                quit_game()
            else:
                continue
        elif response == "1" or "oats" in response:
            while True: 
                print_animated("You see the following options:")
                print_animated("\t1. Quaker Quick 1-Minute Oats")
                print_animated("\t2. Trader Joe's Rolled Oats")
                print_animated("\t3. Quaker Old Fashioned Oats")
                print_animated("\t4. Kellogg's Rolled Oats")
                print_animated("\t5. None (go back)")
                print_animated("Which one do you want to add to your cart?")
                response = input()
                response = response.lower()
                if response == "quit":
                    print_animated("Are you sure you want to quit? (yes/no)")
                    quit_ans = input()
                    quit_ans = quit_ans.lower()
                    if "yes" in quit_ans:
                        quit_game()
                    else:
                        continue
                elif response == "1" or "quick" in response or "1-minute" in response:
                    item_not_gf(quaker_quick_oats, plural=True)
                    continue
                elif response == "2" or "trader" in response or "joes" in response:
                    print_animated("Trader Joe's Rolled Oats are certified gluten free! They are not cross contaminated and are safe for celiacs.")
                    add_to_cart(trader_joes_rolled_oats)
                    grain_section()
                elif response == "3" or "old" in response or "fashioned" in response:
                    item_not_gf(quaker_old_fashioned_oats, plural=True)
                    continue
                elif response == "4" or "kellogg" in response or "rolled" in response:
                    item_not_gf(kelloggs_rolled_oats, plural=True)
                    continue
                elif response == "5" or "none" in response or "back" in response:
                    explore_grain_section()
                else: 
                    print_animated("I don't understand what '" + response + "' means. Please try again.")
                    continue
        elif response == "2" or "cereal" in response:
            while True:
                print_animated("You see the following options:")
                print_animated("\t1. Cinnamon Toast Crunch")
                print_animated("\t2. Mini Wheats")
                print_animated("\t3. Fruity Pebbles")
                print_animated("\t4. Frosted Flakes")
                print_animated("\t5. None (go back)")
                print_animated("Which one do you want to add to your cart?")
                response = input()
                response = response.lower()
                if response == "quit":
                    print_animated("Are you sure you want to quit? (yes/no)")
                    quit_ans = input()
                    quit_ans = quit_ans.lower()
                    if "yes" in quit_ans:
                        quit_game()
                    else:
                        continue
                elif response == "1" or "cinnamon" in response or "toast" in response or "crunch" in response:
                    item_not_gf(cinnamon_toast_crunch)
                    continue
                elif response == "2" or "mini" in response or "wheats" in response:
                    item_not_gf(mini_wheats, plural=True)
                    continue
                elif response == "3" or "fruity" in response or "pebbles" in response:
                    print_animated("Fruity Pebbles are a certified gluten free, rice-based cereal! They are not cross contaminated and are safe for celiacs.")
                    add_to_cart(fruity_pebbles)
                    grain_section()
                elif response == "4" or "frosted" in response or "flakes" in response:
                    item_not_gf(frosted_flakes, plural=True)
                    continue
                elif response == "5" or "none" in response or "back" in response:
                    explore_grain_section()
                else: 
                    print_animated("I don't understand what '" + response + "' means. Please try again.")
                    continue
        elif response == "3" or "pasta" in response:
            while True:
                print_animated("You see the following options:")
                print_animated("\t1. Jovial Brown Rice Penne")
                print_animated("\t2. Barilla Capellini")
                print_animated("\t3. De Cecco Penne")
                print_animated("\t4. Voiello Spaghetti")
                print_animated("\t5. None (go back)")
                print_animated("Which one do you want to add to your cart?")
                response = input()
                response = response.lower()
                if response == "quit":
                    print_animated("Are you sure you want to quit? (yes/no)")
                    quit_ans = input()
                    quit_ans = quit_ans.lower()
                    if "yes" in quit_ans:
                        quit_game()
                    else:
                        continue
                elif response == "1" or "jovial" in response or "brown" in response or "rice" in response or "penne" in response:
                    print_animated("Jovial Brown Rice Penne is a certified gluten free, rice-based pasta! It is not cross contaminated and is safe for celiacs.")
                    add_to_cart(jovial_brown_rice)
                    grain_section()
                elif response == "2" or "barilla" in response or "capellini" in response:
                    item_not_gf(barilla_capellini)
                    continue
                elif response == "3" or "de" in response or "cecco" in response or "penne" in response:
                    item_not_gf(de_cecco_penne)
                    continue
                elif response == "4" or "voiello" in response or "spaghetti" in response:
                    item_not_gf(voiello_spaghetti)
                    continue
                elif response == "5" or "none" in response or "back" in response:
                    explore_grain_section()
                else: 
                    print_animated("I don't understand what '" + response + "' means. Please try again.")
                    continue
        elif response == "4" or "back" in response:
            grain_section()
        else:
            print_animated("I don't understand what '" + response + "' means. Please try again.")
            continue

def explore_snacks_candy_condiments():
    while True:
        print_animated("You can:")
        print_animated("\t1. Look at the protein bars")
        print_animated("\t2. Look at the candy")
        print_animated("\t3. Look at the condiments")
        print_animated("\t4. Go back")
        response = input()
        response = response.lower()

        if response == "quit":
            print_animated("Are you sure you want to quit? (yes/no)")
            quit_ans = input()
            quit_ans = quit_ans.lower()
            if "yes" in quit_ans:
                quit_game()
            else:
                continue
        elif response == "1" or "protein" in response:
            while True:
                print_animated("You see the following options:")
                print_animated("\t1. Chocolate Chip Clif Bars")
                print_animated("\t2. Fiber One Chewy Protein Bars")
                print_animated("\t3. Chocolate Chip RX Bars")
                print_animated("\t4. Special K Chocolately Chip Cookie Dough Protein Bars")
                print_animated("\t5. None (go back)")
                print_animated("Which one do you want to add to your cart?")
                response = input()
                response = response.lower()
                if response == "quit":
                    print_animated("Are you sure you want to quit? (yes/no)")
                    quit_ans = input()
                    quit_ans = quit_ans.lower()
                    if "yes" in quit_ans:
                        quit_game()
                    else:
                        continue
                elif response == "1" or "clif" in response:
                    item_not_gf(clif_bar, plural=True)
                    continue
                elif response == "2" or "fiber" in response:
                    item_not_gf(fiber_one_bar, plural=True)
                    continue
                elif response == "3" or "rx" in response:
                    print_animated("RX-Bars are gluten free! They contain clean ingredients and are safe for celiacs.")
                    add_to_cart(rx_bar)
                    explore_snacks_candy_condiments()
                elif response == "4" or "special" in response:
                    item_not_gf(special_k_bar, plural=True)
                    continue
                elif response == "5" or "none" in response or "back" in response:
                    explore_snacks_candy_condiments()
        elif response == "2" or "candy" in response:
            print_animated("You don't have any candy on your shopping list. Continue shopping.")
            continue
        elif response == "3" or "condiments" in response:
            while True:
                print_animated("You see the following options:")
                print_animated("\t1. Soy Sauce")
                print_animated("\t2. Ketchup")
                print_animated("\t3. Mayonnaise")
                print_animated("\t4. None (go back)")
                print_animated("Which condiment do you want to look at?")
                response = input()
                response = response.lower()
                if response == "quit":
                    print_animated("Are you sure you want to quit? (yes/no)")
                    quit_ans = input()
                    quit_ans = quit_ans.lower()
                    if "yes" in quit_ans:
                        quit_game()
                    else:
                        continue
                elif response == "1" or "soy" in response:
                    while True:
                        print_animated("You see the following soy sauce options: ")
                        print_animated("\t1. Kikkoman Soy Sauce")
                        print_animated("\t2. San-J Tamari Soy Sauce")
                        print_animated("\t3. Great Value Soy Sauce")
                        print_animated("\t4. Aloha Soy Sauce")
                        print_animated("\t5. None (go back)")
                        print_animated("Which soy sauce do you want to add to your cart?")
                        response = input()
                        response = response.lower()
                        if response == "quit":
                            print_animated("Are you sure you want to quit? (yes/no)")
                            quit_ans = input()
                            quit_ans = quit_ans.lower()
                            if "yes" in quit_ans:
                                quit_game()
                            else:
                                continue
                        elif response == "1" or "kikkoman" in response:
                            item_not_gf(kikkoman_soy_sauce)
                            continue
                        elif response == "2" or "san-j" in response:
                            print_animated("San-J Tamari Soy Sauce is gluten free since it's made with rice instead of wheat! It is safe for celiacs.")
                            add_to_cart(tamari_soy_sauce)
                            explore_snacks_candy_condiments()
                        elif response == "3" or "great" in response:
                            item_not_gf(great_value_soy_sauce)
                            continue
                        elif response == "4" or "aloha" in response:
                            item_not_gf(aloha_soy_sauce)
                            continue
                        elif response == "5" or "none" in response or "back" in response:
                            explore_snacks_candy_condiments()
                elif response == "2" or "ketchup" in response:
                    print_animated("Ketchup is not on your shopping list. Continue shopping.")
                    explore_snacks_candy_condiments()
                elif response == "3" or "mayonnaise" in response:
                    print_animated("Mayonnaise is not on your shopping list. Continue shopping.")
                    explore_snacks_candy_condiments()
                elif response == "4" or "none" in response or "back" in response:
                    explore_snacks_candy_condiments()
                else:
                    print_animated("I don't understand what '" + response + "' means. Please try again.")
                    continue
            continue
        elif response == "4" or "back" in response:
            snacks_candy_condiments()
        else:
            print_animated("I don't understand what '" + response + "' means. Please try again.")
            continue

def beverages_section():
    while True:
        print_animated("You are in the beverages section. You can:")
        print_animated("\t1. Explore the beverages")
        print_animated("\t2. Go to the grain aisle")
        print_animated("\t3. Go to to the snacks/candy/condiments aisle")
        print_animated("\t4. Go to to the meat aisle")
        print_animated("\t5. Go to to the prepared foods section")
        response = input()
        response = response.lower()
        if response == "quit":
            print_animated("Are you sure you want to quit? (yes/no)")
            quit_ans = input()
            quit_ans = quit_ans.lower()
            if "yes" in quit_ans:
                quit_game()
            else:
                continue
        elif response == "1" or "explore" in response:
            explore_beverages()
        elif response == "2" or "grain" in response:
            grain_section()
        elif response == "3" or "snacks" in response or "candy" in response or "condiments" in response:
            snacks_candy_condiments()
        elif response == "4" or "meat" in response:
            meat_section()
        elif response == "5" or "prepared" in response or "foods" in response:
            prepared_foods_section()
        else:
            print_animated("I don't understand what '" + response + "' means. Please try again.")
            continue

def explore_beverages():
    while True:
        print_animated("You can:")
        print_animated("\t1. Look at the beer")
        print_animated("\t2. Look at the wine")
        print_animated("\t3. Look at the soda")
        print_animated("\t4. Look at the water")
        print_animated("\t5. Go back")
        response = input()
        response = response.lower()
        if response == "quit":
            print_animated("Are you sure you want to quit? (yes/no)")
            quit_ans = input()
            quit_ans = quit_ans.lower()
            if "yes" in quit_ans:
                quit_game()
            else:
                continue
        elif response == "1" or "beer" in response:
            while True:
                print_animated("You see the following options:")
                print_animated("\t1. Bud Light")
                print_animated("\t2. Coors Light")
                print_animated("\t3. Bard's Tale Beer")
                print_animated("\t4. Heineken")
                print_animated("\t5. None (go back)")
                print_animated("Which one do you want to add to your cart?")
                response = input()
                response = response.lower()
                if response == "quit":
                    print_animated("Are you sure you want to quit? (yes/no)")
                    quit_ans = input()
                    quit_ans = quit_ans.lower()
                    if "yes" in quit_ans:
                        quit_game()
                    else:
                        continue
                elif response == "1" or "bud" in response:
                    item_not_gf(bud_light)
                    continue
                elif response == "2" or "coors" in response:
                    item_not_gf(coors_light)
                    continue
                elif response == "3" or "bard" in response:
                    print_animated("Bard's Tale Beer is made with sorghum instead of barley and is 100% gluten free!")
                    add_to_cart(bards_tail)
                    explore_beverages()
                elif response == "4" or "heineken" in response:
                    item_not_gf(heineken)
                    continue
                elif response == "5" or "none" in response or "back" in response:
                    explore_beverages()
        elif response == "2" or "wine" in response:
            print_animated("You don't have any wine on your shopping list. Continue shopping.")
            continue
        elif response == "3" or "soda" in response:
            print_animated("You don't have any soda on your shopping list. Continue shopping.")
            continue
        elif response == "4" or "water" in response:
            print_animated("You don't have any water on your shopping list. Continue shopping.")
            continue
        elif response == "5" or "back" in response:
            beverages_section()
        else:
            print_animated("I don't understand what '" + response + "' means. Please try again.")
            continue

def meat_section():
    while True:
        print_animated("You are in the meat section. You can:")
        print_animated("\t1. Explore the meat")
        print_animated("\t2. Go to the grain aisle")
        print_animated("\t3. Go to to the beverages asile")
        print_animated("\t4. Go to to the prepared foods section")
        print_animated("\t5. Go to to the produce aisle")
        response = input()
        response = response.lower()
        if response == "quit":
            print_animated("Are you sure you want to quit? (yes/no)")
            quit_ans = input()
            quit_ans = quit_ans.lower()
            if "yes" in quit_ans:
                quit_game()
            else:
                continue
        elif response == "1" or "explore" in response:
            print_animated("Arnold Schwarzenegger came to the store yesterday and bought all the meat! There's nothing left here.")
            meat_section()
        elif response == "2" or "grain" in response:
            grain_section()
        elif response == "3" or "beverages" in response:
            snacks_candy_condiments()
        elif response == "4" or "prepared" in response or "foods" in response:
            prepared_foods_section()
        elif response == "5" or "produce" in response or "fruit" in response or "vegetables" in response:
            produce_section()
        else: 
            print_animated("I don't understand what '" + response + "' means. Please try again.")
            continue
            
def prepared_foods_section():
    while True:
        print_animated("You are in the prepared foods section. You can:")
        print_animated("\t1. Talk to the worker behind the counter")
        print_animated("\t2. Go to the meat aisle")
        print_animated("\t3. Go to to the beverages asile")
        print_animated("\t4. Go to to the produce aisle")
        print_animated("\t5. Go to to the bakery")
        response = input()
        response = response.lower()
        if response == "quit":
            print_animated("Are you sure you want to quit? (yes/no)")
            quit_ans = input()
            quit_ans = quit_ans.lower()
            if "yes" in quit_ans:
                quit_game()
            else:
                continue
        elif response == "1" or "talk" in response or "worker" in response or "counter" in response:
            talk_to_worker()
        elif response == "2" or "meat" in response:
            meat_section()
        elif response == "3" or "beverages" in response:
            beverages_section()
        elif response == "4" or "produce" in response or "fruit" in response or "vegetables" in response:
            produce_section()
        elif response == "5" or "bakery" in response:
            bakery_section()
        else: 
            print_animated("I don't understand what '" + response + "' means. Please try again.")
            continue

def produce_section():
    while True:
        print_animated("You are in the produce section. You can:")
        print_animated("\t1. Explore the produce")
        print_animated("\t2. Go to the meat aisle")
        print_animated("\t3. Go to to the prepared foods section")
        print_animated("\t4. Go to to the bakery")
        response = input()
        response = response.lower()
        if response == "quit":
            print_animated("Are you sure you want to quit? (yes/no)")
            quit_ans = input()
            quit_ans = quit_ans.lower()
            if "yes" in quit_ans:
                quit_game()
            else:
                continue
        elif response == "1" or "explore" in response:
            print_animated("You don't have any produce on your shopping list. Continue shopping.")
            continue
        elif response == "2" or "meat" in response:
            meat_section()
        elif response == "3" or "prepared" in response or "foods" in response:
            prepared_foods_section()
        elif response == "4" or "bakery" in response:
            bakery_section()
        else: 
            print_animated("I don't understand what '" + response + "' means. Please try again.")
            continue

def talk_to_worker():
    while True:
        print_animated("Hi " + name + "! My name is Tsubasa. I make fresh sushi here daily. We have the following rolls today:")
        print_animated("\t1. California Roll")
        print_animated("\t2. Eel Roll")
        print_animated("\t3. Shrimp Tempura Roll")
        print_animated("\t4. Tuna Roll")
        print_animated("\t5. None (go back)")
        print_animated("Which one would you like to add to your cart?")
        response = input()
        response = response.lower()
        if response == "quit":
            print_animated("Are you sure you want to quit? (yes/no)")
            quit_ans = input()
            quit_ans = quit_ans.lower()
            if "yes" in quit_ans:
                quit_game()
            else:
                continue
        elif response == "1" or "california" in response or "roll" in response:
            item_not_gf(california_roll, plural=True)
            continue
        elif response == "2" or "eel" in response or "roll" in response:
            item_not_gf(eel_roll, plural=True)
            continue
        elif response == "3" or "shrimp" in response or "tempura" in response or "roll" in response:
            item_not_gf(shrimp_tempura_roll, plural=True)
            continue
        elif response == "4" or "tuna" in response or "roll" in response:
            print_animated("Tuna Rolls are gluten free!")
            add_to_cart(tuna_roll)
            prepared_foods_section()
        elif response == "5" or "none" in response or "back" in response:
            prepared_foods_section()
        else:
            print_animated("I don't understand what '" + response + "' means. Please try again.")
            continue

def bakery_section():
    while True:
        print_animated("You are in the bakery section. You can:")
        print_animated("\t1. Explore the bakery")
        print_animated("\t2. Go to the produce aisle")
        print_animated("\t3. Go to to the prepared foods section")
        response = input()
        response = response.lower()
        if response == "quit":
            print_animated("Are you sure you want to quit? (yes/no)")
            quit_ans = input()
            quit_ans = quit_ans.lower()
            if "yes" in quit_ans:
                quit_game()
            else:
                continue
        elif response == "1" or "explore" in response:
            print_animated("You don't have any bakery items on your shopping list. Continue shopping.")
            continue
        elif response == "2" or "produce" in response or "fruit" in response or "vegetables" in response:
            produce_section()
        elif response == "3" or "prepared" in response or "foods" in response:
            prepared_foods_section()
        else: 
            print_animated("I don't understand what '" + response + "' means. Please try again.")
            continue

def item_not_gf(item, plural = False):
    if plural == True:
        print_animated("Oh no! " + item.name + " are not safe for celiacs because they " + item.reasons_why_its_not_gf + "!")
    else:
        print_animated("Oh no! " + item.name + " is not safe for celiacs because it " + item.reasons_why_its_not_gf + "!")
    reduce_health()
    
def add_to_cart(item):
    global cart_items
    if item in cart_items:
        print_animated("You already have " + item.name + " in your cart.")
        return
    
    if len(cart_items) < 5:
        cart_items.append(item)
        print_animated("You have added " + item.name + " to your cart 🛒.")
    else:
        print_animated("You have reached the maximum number of items in your cart. Please remove an item before adding another.")

    print_animated("Your cart contains the following items:")
    for count, item in enumerate(cart_items):
        print_animated("\t" + str(count+1) + ". " + item.name)

    print_animated("Would you like to remove any items from your cart? (yes/no)")
    remove_ans = input()
    remove_ans = remove_ans.lower()
    if "yes" in remove_ans:
        remove_from_cart()
        print_animated("You still need to get the following items:")
        cart_item_categories = []
        # add the item categories to a new array
        for item in cart_items:
            cart_item_categories.append(item.food_category)
        # print products from the shopping list that aren't in the cart
        on_shopping_list_not_in_cart = []
        for prod in shopping_list:
            if prod not in cart_item_categories:
                print_animated("\t •" + string.capwords(prod))
                on_shopping_list_not_in_cart.append(prod)
        if on_shopping_list_not_in_cart == []:
            print_animated("You have all the items you need!")
            check_time(version="final")
            print_animated("You now check out with your gluten free items are live happily every after!")
            quit_game()
    else:
        print_animated("You still need to get the following items:")
        cart_item_categories = []
        # add the item categories to a new array
        for item in cart_items:
            cart_item_categories.append(item.food_category)
        # print products from the shopping list that aren't in the cart
        on_shopping_list_not_in_cart = []
        for prod in shopping_list:
            if prod not in cart_item_categories:
                print_animated("\t •" + string.capwords(prod))
                on_shopping_list_not_in_cart.append(prod)
        if on_shopping_list_not_in_cart == []:
            print_animated("You have all the items you need.")
            check_time(version="final")
            print_animated("You now check out with your gluten free items are live happily every after!")
            quit_game()
        return
        
def remove_from_cart():
    global cart_items
    while True:
        if cart_items != []: 
            print_animated("Which item would you like to remove from your cart? (type the number)")
            remove_ans = input()
            remove_ans = remove_ans.lower()
            if remove_ans == "1" or remove_ans == "2" or remove_ans == "3" or remove_ans == "4" or remove_ans == "5":
                remove_ans = int(remove_ans)
                remove_ans = remove_ans - 1
                print_animated("You have removed " + cart_items[remove_ans].name + " from your cart.")
                cart_items.remove(cart_items[remove_ans])
                print_animated("Your cart now contains the following items:")
                for count, item in enumerate(cart_items):
                    print_animated("\t" + str(count+1) + ". " + item.name)
                if cart_items != []:
                    print_animated("Would you like to remove another item from your cart? (yes/no)")
                    remove_ans = input()
                    remove_ans = remove_ans.lower()
                    if "yes" in remove_ans:
                        remove_from_cart()
                    else:
                        return
            elif "none" in remove_ans or "no" in remove_ans or "nothing" in remove_ans or "nevermind" in remove_ans:
                return
            elif remove_ans == "quit":
                print_animated("Are you sure you want to quit? (yes/no)")
                quit_ans = input()
                quit_ans = quit_ans.lower()
                if "yes" in quit_ans:
                    quit_game()
                else:
                    continue
            else:
                print_animated("I'm sorry, I don't know what " + str(remove_ans) + " means.")
                break
        else:
            return

def show_health(health_input,amount_reduced = 0, animate = False):
    # build health string
    health_string = ""
    for i in range(int(health_input/10)):
        health_string = health_string + "❤️"

    # draw health string
    for char in health_string:
        if animate == True:
            sleep(GENERAL_TYPING_SPEED)
            print(char, end = '', flush = True)
        else: 
            print(char, end = '', flush = True)
    
    if amount_reduced > 0: 
        sleep(1)

        # remove health amount
        for i in range(int(amount_reduced/10)):
            print('\b \b', end='', flush=True)
            time.sleep(0.70)
    
# Main
# Run a countdown timer in a separate thread        
event = threading.Event()
timer = threading.Thread(target = countdown_timer, args = (GAME_LENGTH_SECS,))

# play
game_intro()
entrance()

# for python 2 compatibility
if sys.version_info.major == 2:
    raw_input = input