from art5 import logo, vs

from game_data import data

import random

def get_random_data():
  """Get data from random account"""
  return random.choice(data)

def data_collect(data):
    data_name = data["name"]
    data_descr = data["description"]
    data_country = data["country"]
    return f"{data_name}, a {data_descr} from {data_country}"

def check_guess(guess, data1_followers, data2_followers):
    if data1_followers > data2_followers:
        return guess == "1"
    else:
        return guess == "2"

def game():
  print(logo)
  score = 0
  game_should_continue = True
  data1 = get_random_data()
  data2 = get_random_data()

  while game_should_continue:
      data1 = data2
      data2 = get_random_data()

      while data1 == data2:
          data2 = get_random_data()


      data1 = random.choice(data)
      data2 = random.choice(data)
      if data1 == data2:
            data2 = random.choice(data)


      print(f"Compare A:{data_collect(data1)}.")
      print(vs)
      print(f"Against A:{data_collect(data1)}.")

      guess = input("Who has more followers? Type '1' or '2' : ")
      data1_follower_count = data1["follower_count"]
      data2_follower_count = data2["follower_count"]
      is_correct = check_guess(guess, data1_follower_count, data2_follower_count)

      print(logo)
      if is_correct:
          score += 1
          print(f"You're right! Current score: {score}.")
      else:
          game_should_continue = False
          print(f"Sorry, that's wrong. Final score: {score}")

game()




