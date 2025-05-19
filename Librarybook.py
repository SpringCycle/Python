
from collections import defaultdict


available_editions={"fundaments of CS":4,"Biochemical":3,"DSA":6,"SystemDesign":7}



#auditofuser is used to keep track of total books browwed
auditofuser=defaultdict(list)

while True:
    username=input("Enter the Username : ")
    action = input("Do you want to borrow or return a book? (b/r): ").strip().lower()
    
    if action == "b":
        borrow_book=input("Enter the book you need to borrow : ")
        # for book,tbook in available_editions.items():
        if  borrow_book in available_editions and available_editions[borrow_book]>0:
            print(username,"have borrowed : ",borrow_book)
            available_editions[borrow_book]= available_editions.get(borrow_book)-1
            auditofuser[username].append(borrow_book)
        else :
            print("Book not available")
            
          
    elif action=="r":
        return_book= input("Enter the book you need to return : ")
        #user is key , books is value as list
        if return_book in auditofuser[username]:
            available_editions[return_book]+=1
            auditofuser[username].remove(return_book)
            print(username, " returned book", return_book)
            print("remaining books for ", auditofuser[username])
        else:
            print(username,"hasn't borrowed the book")
            
    elif action=="s":
        print(available_editions)
        print(auditofuser)
        
    else :
        print("Invalid Option")

   
    #     borrow_book = input("Enter the edition you need to borrow : ")
    #     print("Available books : ",available_editions.get(borrow_book))


    #     if borrow_book=="fundaments of CS" and available_editions.get(borrow_book)>0:
    #         print(username,"have borrowed : ",borrow_book)
    #         available_editions[borrow_book]= available_editions.get(borrow_book)-1
    #         auditofuser[username].append(borrow_book)


    #     elif borrow_book=="Biochemical" and available_editions.get(borrow_book)>0:
    #         print(username,"have borrowed : ",borrow_book)
    #         available_editions[borrow_book]= available_editions.get(borrow_book)-1
    #         auditofuser[username].append(borrow_book)

    #     elif borrow_book=="DSA" and available_editions.get(borrow_book)>0:
    #         print(username,"have borrowed : ",borrow_book)
    #         available_editions[borrow_book]= available_editions.get(borrow_book)-1
    #         auditofuser[username].append(borrow_book)

    #     elif borrow_book=="SystemDesign"and available_editions.get(borrow_book)>0:
    #         print(username,"have borrowed : ",borrow_book)
    #         available_editions[borrow_book]= available_editions.get(borrow_book)-1
    #         auditofuser[username].append(borrow_book)
    #     else :
    #         print("books are out of supply, will keep you posted!!")

    # elif action == "r" :

    #     return_book = input("Enter the book you need to return : ")
    
    #     if return_book=="fundaments of CS":
    #         print(username,"You have returned : ",return_book)
    #         if return_book in available_editions:
    #             available_editions[return_book].append(return_book)
    #             auditofuser[username].remove(return_book)
    #         else:
    #             print(username,"haven't borrowed book")
    #         print(auditofuser)

    #     elif return_book=="Biochemical" :
    #         print(username,"You have returned : ",return_book)
    #         if return_book in available_editions:
    #             available_editions[return_book].append(return_book)
    #             auditofuser[username].remove(return_book)
    #             print(auditofuser)
    #         else:
    #             print(username,"haven't borrowed book")
    #         print(auditofuser)

    #     elif return_book=="DSA":
    #         if return_book in auditofuser[username]:
    #             available_editions[return_book]+=1
    #             auditofuser[username].remove(return_book)
    #             print(username,"returned the book")
    #             print(auditofuser)
    #         else:
    #             print(username,"haven't borrowed book")
    #         print(auditofuser)
            

    #     elif return_book=="SystemDesign":
    #         if return_book in auditofuser:
    #             available_editions[return_book]+=1
    #             auditofuser[username].remove(return_book)
    #             print(username,"You have returned : ",return_book)
    #             print(auditofuser)
    #         else:
    #             print(username,"haven't borrowed book")
    #         print(auditofuser)
            
    #     else:
    #         print(username,"haven't borrowed book")
