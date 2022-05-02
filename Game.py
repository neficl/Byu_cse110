print('Welcome to your Intellect\n')
print('Here on planet Emotion your choices are of extreme importance. Be careful what you choose, because your choices will take you to ...')
first = input(print('To get off the ship, you have three options, get into a BOAT (there is only one place), jump off the boat and go SWIMMING with your friends, or wait to be swallowed by the CURRENTS. What do you want to do?'))
if first.lower() == 'boat' :
    print('Good luck, you decided to go on the boat, your friends died, but you arrived alive!')
    second_choice=input(print("On your first night you have two options having a FIRE to light up your night or a hiding PLACE in the dark, which will be better?"))
    if second_choice.lower() == 'fire' :
        print("Since you have chosen the campfire, you are lighting up your environment, getting warm, and are able to use the fire against dangerous animals. ")
    else :
        print("Now that you are in the dark, but safe. You will have to keep still all night, you have no equipment to illuminate or protect yourself. Good luck!")     
elif first.lower() == 'swimming' :
    print('Congratulations on your choice, you have had few injuries, but you made it to dry land alive.')
    second_choice=input(print("Now that you and your friends have arrived on dry land, you have two options - you can either search for materials for your SURVIVAL and bear the pain of your wounds, or you can search for medicinal PLANTS to heal yourselves. Which will it be?"))
    if second_choice.lower() == 'survival' :
      print("Congratulations you are ready to spend your first night, although you are in pain. When you wake up you realize that you are not alone, you have a few minutes to escape!")
    else:
        print("The pain has been relieved, but fear strikes your hearts. I believe this could be the worst night of your lives!")                 
elif first.lower() == 'currents' :
    print('To your surprise, the ship did not sink, but because of the strong current, you are close to large sharks.')
    second_choice=input(print("You have survived you, your girlfriend and your best friend. You are struggling with the weather, what will you do to get to dry land? Will you be SWIMMING or will you leave your FRIEND who can't swim to the sharks?"))
    if second_choice.lower() == 'swimming' :
        print("Now that you and your girlfriend have arrived, you have forgotten your friend and he has died in the depths of the sea.")
    else:
        print('It was difficult to get to dry land, they swallowed a lot of water, they suffered from some bites, but there is one more person to help in this battle of the unknown, how is it going to be?')   
else :
    print("Enter a valid option, according to the words in capital letters.")