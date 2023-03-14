class User:
    def __init__(self, user_id, username):
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Ozren")
user_2 = User("002", "Suzuki")
# user_1 = user_2



user_1.follow(user_2)


print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# print(user_1.id)
# print(user_1.followers)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "Suzuki"



# class Car:
#     def __init__(self):


class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

new_q = Question("The dog is black", "False")
print(new_q.text)