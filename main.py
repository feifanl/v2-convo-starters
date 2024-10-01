"""I made a program for a 24h hackathon about a year ago, v1-convo-starters. At that time, I barely knew the basics of Python and even had to Google some concepts. 
After getting more interested in programming, I decided that I should try and optimize this program as my first project."""  

input_dayrate = input("RATE YOUR DAY! (Scale of 1 to 10)")
#I created a list to make the process of printing the outputs must faster. Refer to v1-convo-starters to see why. 
dayrate_list = ["That's not on the scale, silly! On the bright side it can only go up from here!", "Awww man...Tomorrow will be better :)", "So sorry to hear that. I hope tomorrow will treat you better!", "So sorry to hear that. I hope tomorrow will treat you better!", "You're almost there! I believe tomorrow will be better.", "About average, eh? I'm sure tomorrow will be better!", "Wowza! That's pretty good...Let's make tomorrow the same!", "Wowza! That's pretty good...Let's make tomorrow the same!", "I hope tomorrow is just as good!", "That's actually really impressive...Let's make tomorrow a 10!", "Let's keep it this way ;)", "Off the charts!?"]

#I needed to make sure the input was actually a number and between the range of 0-11.
while input_dayrate.isdigit() == False or not(0 <= int(input_dayrate) and int(input_dayrate) <= 11): 
    print("1 to 10 please!\n")
    input_dayrate = input("GO AGAIN! (Scale of 1 to 10)")
else: 
#Since I had 0-11 for inputs and the list was 0-11, I could just use the input as the index of the list. 
    print(dayrate_list[int(input_dayrate)] + "\n")

input_convostarters = input("Choose a conversation starter! \nFind a group of friends (pre-existing or at school or online or something!) Pick a card, any card. (1 to 10) ")
#The same premise as the other list. 
convostarters_list = ["How has the COVID-19 pandemic impacted your daily routine?", "How has your social interaction changed during this pandemic?", "What new hobbies have you picked up over quarantine?", "How has the pandemic affected your job status?", "What music/podcasts did you listen to over quarantine?", "What company/store has helped you most over quarantine?", "Do you want to go back to school/work?", "How did your productivity change over quarantine?", "Have you found out about any small businesses over the pandemic?", "What was your favorite pastime during quarantine?"]

#I used a while loop here because I wanted the program to keep giving the user conversation starters. 
while True: 
    #Giving the user an opportunity to break out of the loop. 
    if input_convostarters == "no": 
        print("Au revoir!")
        break
    #Once again checking if the input is a number and whether it is from 1-10. 
    while input_convostarters.isdigit() == False or not(1 <= int(input_convostarters) and int(input_convostarters) <= 10): 
        print("1 to 10, bucko.\n")
        input_convostarters = input("Want another? (no if no)")
    else:
        #Using index - 1 because the input is 1-10 but the indices are 0-9. 
        print(convostarters_list[int(input_convostarters) - 1] + "\n")
        input_convostarters = input("Want another? (no if no)")
