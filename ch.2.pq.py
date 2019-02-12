#1. What are the two values of the Boolean data type? How do you write them?
    #true and false with a capital first letter

#2. What are the three Boolean operators?
    #and, or, not

#3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
    #true and true, true or false, not true == True

#4. What do the following expressions evaluate to?


    #(5 > 4) and (3 == 5) False
    #not (5 > 4) False
    #(5 > 4) or (3 == 5) True
    #not ((5 > 4) or (3 == 5)) False
    #(True and True) and (True == False) False
    #(not False) or (not True) True

#5. What are the six comparison operators?
    #<, >, ==, !=, <=, >=

#6. What is the difference between the equal to operator and the assignment operator?
    #equal to compares statements and the assingment operator assigns values

#7. Explain what a condition is and where you would use one.
    #a condition is a statement that runs if the requirments are satisfied

#8. Identify the three blocks in this code:
    #spam = 0 <-- first block
    #if spam == 10: <-- first block
        #print('eggs') <-- second block
        #if spam > 5: <-- second block
            #print('bacon') <-- third block
        #else: <-- second block
            #print('ham') <-- third block
        #print('spam') <-- second block
    #print('spam') <-- first block

#9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
spam = 2
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("greetings")

#10. What can you press if your program is stuck in an infinite loop?
    # CTRL - C



#11. What is the difference between break and continue?
    #Break exits the loop/program and continue starts the loop/progam over at the beginning


#12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
    #nothing, they would all evauluate to the same



#13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
for i in range(1, 11):
    print(i)
i = 1
while i < 11:
    print(i)
    i += 1
#14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
    #spam.bacon()