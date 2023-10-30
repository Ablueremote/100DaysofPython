print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

def true_calc(name):
  true_score = 0 
  true_score += name.count("t")
  true_score += name.count("r")
  true_score += name.count("u")
  true_score += name.count("e")
  return true_score
def love_calc(name):
  love_score = name.count("l")
  love_score += name.count("o")
  love_score += name.count("v")
  love_score += name.count("e")
  return love_score

true_score = true_calc(name1) + true_calc(name2)
true_score = str(true_score)
love_score = love_calc(name1) + love_calc(name2)
love_score = str(love_score)
score = true_score + love_score
score = int(score)

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50: 
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
  #New Update