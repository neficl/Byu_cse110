print('Welcome to your Intellect\n')
print('Here on planet Emotion your choices are of extreme importance. Be careful what you choose, because your choices will take you to ...')
first = input(print('To get off the ship, you have three options, get into a BOAT (there is only one place), jump off the boat and go SWIMMING with your friends, or wait to be swallowed by the CURRENTS. What do you want to do?'))
if first.lower() == 'boat' :
    print('Good luck, you decided to go on the boat, your friends died, but you arrived alive!')
elif first.lower() == 'swimming' :
    print('Congratulations on your choice, you have had few injuries, but you made it to dry land alive.')
elif first.lower() == 'currents' :
    print('To your surprise, the ship did not sink, but because of the strong current, you are close to large sharks.')
else :
    print("Enter a valid option, according to the words in capital letters.")
    