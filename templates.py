#Interface for booking movie ticket
#book multiple movies



# total_seats = [80,50,60]
# select_movies = ["kannada","english","hindi"]
# movie_seats = { kannada:80, english:50, hindi:60}
# movies = input("Select the movie")
# seats = input("Enter the number of seats")

# for movies,total_seats in dict(movie_seats):
#     if movies == "kannada" and seats<=total_seats:
#         print("You are booking Kannada movie for",seats)
#         print("Thanks for booking")
#         total_seats = total_seats - seats
#     else:
#         print("Sorry seats are full!!")

#     else if movies == "english"  and seats<=total_seats:
#         print("You are booking English movie for",seats)
#         print("Thanks for booking")
#         total_seats = total_seats - seats
#      else:
#         print("Sorry seats are full!!")

#     else if movies == "Hindi"  and seats<=total_seats :   
#         print("You are booking Hindi movie for",seats)
#         print("Thanks for booking")
#         total_seats = total_seats - seats
#      else:
#         print("Sorry seats are full!!")



#Construct a library where people can borrow and return books, keep track of books


from collections import defaultdict


available_editions={"fundaments of CS":4,"Biochemical":3,"DSA":6,"SystemDesign":7}



#auditofuser is used to keep track of total books browwed
auditofuser=defaultdict(list)

while True:
    username=input("Enter the Username")
    action = input("Do you want to borrow or return a book? (b/r): ").strip().lower()

    if action == "b":
        borrow_book = input("Enter the edition you need to borrow")
        print("Available books : ",available_editions.get(borrow_book))


        if borrow_book=="fundaments of CS" and available_editions.get(borrow_book)>0:
            print(username,"have borrowed : ",borrow_book)
            available_editions[borrow_book]= available_editions.get(borrow_book)-1
            auditofuser[username].append(borrow_book)


        elif borrow_book=="Biochemical" and available_editions.get(borrow_book)>0:
            print(username,"have borrowed : ",borrow_book)
            available_editions[borrow_book]= available_editions.get(borrow_book)-1
            auditofuser[username].append(borrow_book)

        elif borrow_book=="DSA" and available_editions.get(borrow_book)>0:
            print(username,"have borrowed : ",borrow_book)
            available_editions[borrow_book]= available_editions.get(borrow_book)-1
            auditofuser[username].append(borrow_book)

        elif borrow_book=="SystemDesign"and available_editions.get(borrow_book)>0:
            print(username,"have borrowed : ",borrow_book)
            available_editions[borrow_book]= available_editions.get(borrow_book)-1
            auditofuser[username].append(borrow_book)
        else :
            print("books are out of supply, will keep you posted!!")

    elif action == "r" :

        return_book = input("Enter the book you need to return")
    
        if return_book=="fundaments of CS":
            print(username,"You have returned : ",return_book)
            available_editions[return_book]+=1
            auditofuser[username].remove(return_book)
            print(available_editions)
            print(auditofuser)

        elif return_book=="Biochemical" :
            print(username,"You have returned : ",return_book)
            available_editions[return_book]+=1
            auditofuser[username].remove(return_book)
            print(available_editions)
            print(auditofuser)

        elif return_book=="DSA":
           print(username,"You have returned : ",return_book)
           available_editions[return_book]+=1
           auditofuser[username].remove(return_book)
           print(available_editions)
           print(auditofuser)

        elif return_book=="SystemDesign":
            print(username,"You have returned : ",return_book)
            available_editions[return_book]+=1
            auditofuser[username].remove(return_book)
            print(available_editions)
            print(auditofuser)

    

    
