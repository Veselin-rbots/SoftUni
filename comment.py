class Comment:
    def __init__(self, username, content , likes= 0):
        self.username = username
        self.content = content
        self.likes = likes

Comment = Comment("user1", "I like this book")
print(Comment.username)
print(Comment.content)
print(Comment.likes)
