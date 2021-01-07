from random import randint
 
def hangman(user,fruit):
    global space_fruit
    list_index=[]
    for i in range(len(fruit)):
        if fruit[i]==user:
            space_fruit.pop(i)
            space_fruit.insert(i,user)  
    return space_fruit
    
    
    
    
fruit_list=['Apple','Watermelon','Orange','Pear','Cherry','Strawberry','Nectarine','Grape',
            'Mango','Blueberry','Pomegranate','Banana','Raspberry','Mandarin','Jackfruit','Papaya',
            'Kiwi','Pineapple','Lime','Lemon','Apricot','Grapefruit','Melon','Coconut','Avocado','Peach']
hidden_fruit = list(fruit_list[randint(0,(len(fruit_list)-1))].lower())
guesses =7
space_fruit=["_ "]*len(hidden_fruit)
print("\nGusses your first char !\n")
for i in space_fruit:
    print(i,end=" ")   
print('\n',hidden_fruit)
length_fruit= len(hidden_fruit)

while guesses :   
    if '_'  in str(space_fruit):    
        user_input=input("\n\n\nUser input:").lower()
        if user_input != ''and len(user_input)==1: 
            if user_input in hidden_fruit:   
                print("It is present in the word. Hurray! ")
                print(f"Number of wrong guesses left : {guesses}")       
                hangman(user_input,hidden_fruit)

            else:
                print("Oops! It is not present in the word.",end=" ")
                guesses-=1
                if guesses==0:
                    print("You have lost!!!")
                    break
                elif guesses==2:
                    print(f"\nNumber of wrong guesses left : {guesses}")
                    print("This is getting really close :( ")
                elif guesses==1:
                    print(f"\nNumber of wrong guesses left : {guesses}")
                    print("This is getting really really closle :( :O")
                else:
                    print(f"\nNumber of wrong guesses left : {guesses}")

            for i in space_fruit:
                print(i,end=" ")
        else:
            print("\n Please Enter single letter for guesse!!\n")
    else:
        print("\n\n\nGreat! You guessed the word. You Won!")
        break
    