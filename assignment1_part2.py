class book:
    author = ""
    title = ""

    def __init__(self, Author, Title):
        self.author = Author
        self.title = Title

    def display(self):
        print("\""+self.title+" , written by "+self.author+"\"")

object1 = book("John Steinbeck", "Of Mice and Men")
object1.display()

object2 = book("Harper Lee", "To Kill a Mockingbird")
object2.display()
