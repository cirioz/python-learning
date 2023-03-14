class Tweet:
    pass

a = Tweet()

a.message = '140 characters.'
print(a.message)

# print(Tweet.message)

b = Tweet()

b.message = "Something entierely different"

print(a.message)

print(b.message)

#Dunder init method - constructor method

class Tweet:
    def __init__():
        print('Hi')

a = Tweet()

a = Tweet(1)

class Tweet:
    def __init__ (self):
        print('hi')

a = Tweet()

class Tweet:
    def __init__ (self, message):
        self.x = message

a = Tweet()

a = Tweet("Something here")

print(a.x)

b = Tweet("I'm another instance of Tweet")

print(b.x)

class Tweet:
    def __init__(self, message):
        self.message = message
    def print_tweet():
        print(self.message)

t = Tweet("An instance of Tweet")

t.print_tweet()


a = Tweet(1)

b = Tweet(2)

a.print_tweet()

b.print_tweet()

Tweet.print_tweet()


Tweet.print_tweet(a)
Tweet.print_tweet(b)


 