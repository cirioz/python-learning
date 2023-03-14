

#! Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#! Then check for the number of times the letters in the word LOVE occurs. 
#! Then combine these numbers to make a 2 digit number.
#!For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."

compare= ['t', 'r', 'u', 'e', 'l', 'o', 'v', 'e']

name_one = input("What is your name?").lower()
count = 0
name_two = input("What is your love interests name").lower()

#! Solution 1
for i in name_one:
    if i in compare:
        count += 1
    else:
        pass
print(count)

for i in name_two:
    if i in compare:
        count += 1
    else:
        pass
print(count)

#! Solution 2
# for i in name_two:
#     if i == "t" or i == "r" or i == "u" or i == "e" or i == "l" or i == "o" or i == "v":
#         count += 1
#     else:
#         pass
# print(count)

if (count < 10 or count > 90) and count <10 and count>90:
    print(f"Your score is {count}, you go together like coke and mentos.")
elif count > 40 and count < 50:
    print(f"Your score is {count}, you are alright together.")
else:
    print(f"Your score is {count}")
    
    
    
    #! Solution 3 UZASNO
    
    name1 = input("What is your name?")
    name2 = input("What is their name?")
    
    
    combined_string = name1 + name2
    lower_case_string = combined_string.lower()
    
    t = lower_case_string.count("t")
    r = lower_case_string.count("r")
    u = lower_case_string.count("u")
    e = lower_case_string.count("e")
    
    true = t + r + u + e
    
    
    l = lower_case_string.count("l")
    o = lower_case_string.count("o")
    v = lower_case_string.count("v")
    e = lower_case_string.count("e")
    
    love = l + o + v + e
    
    love_score = int(str(true + love))
    print(love_score)
    