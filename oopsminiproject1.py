class Lib:
    def __init__(self,name,list_book=[]):
        self.list_book = list_book
        self.name = name
        self.lenddict = {}

    def display_book(self):
        print(f"Welcome to our Lib: {self.name}")
        for i in self.list_book:
            print(i)

    def lend_book(self,user,book):
        if book is not self.lenddict.keys():
            self.lenddict.update({user:book})
        else:
            print(f"Book is already in possession of {self.lenddict[user]}")

        self.list_book.remove(book)

    def add_book(self,book):
        self.list_book.append(book)
        print("Book is successfully added")

    def return_book(self,book):
        self.lenddict.pop(book)
        self.lend_book.append(book)
        return f"Thanks for using our library"  

    def display_whotakesthebooks(self):
        for i,j in self.lenddict.items():
            print(i,":",j)  
         

if __name__ == "__main__":
    a = ["Thinks and Grow Rich","rich dad poor dad","48 Hours Startup","A brief History of time"]
    Store = Lib("harry",a)

    while True:
        print("Welcome to our Library: ")
        print("1.Display Book")
        print("2.Lend Book")
        print("3.Add book")
        print("4.return Book")
        print("5.Who take the Books")
        s = int(input())        

    
        if s == 1:
            print(" ")
            Store.display_book()

        elif s==2:
            book = input("which book do you want: ")
            user = input("Enter your name: ")

            Store.lend_book(user,book)

        elif s==3:
            book = input("Which book do you want to add: ")
            Store.add_book(book)

        elif s==4:
            book = input("Return it now,you cheap bastard: ")
            Store.return_book(book)

        elif s==5:
            Store.display_whotakesthebooks()

        
        print(" ")

        a  = input("q for quit or c for continue: ")
        if a == "q":
            break
        elif a== "c":
            continue
        print(' ')

