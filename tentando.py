from multiprocessing.sharedctypes import Value

max = 0
min = 100
countries= []
years= []
life= []
years_list= []
years_sum = 0
max_year_user = 0
min_year_user = 100


with open("life-expectancy.csv") as expect_file:
    year=input("What year would you like the info? ")
    for line in expect_file:
        clean_line = line.strip()
        collumns = clean_line.split(",")
        countries.append(collumns[0])
        years.append(collumns[2])
        life.append(collumns[3])        
        if collumns[2] == year:
            years_list.append(collumns[2])
            years_sum += float(collumns[3])
            amount = float(collumns[3])
            if amount > max_year_user:
                max_year_user = amount
                max_country_user = collumns[0]
                max_life_user = float(collumns[3])
            if amount < min_year_user:
                min_year_user= amount
                min_country_user = collumns[0]
                min_life_user = float(collumns[3])
    life.pop(0)
    for i in range(len(life)):
        ammount = float(life[i])
        if ammount > max:
            max = ammount
            max_country = countries[i]
            max_year = years[i]
        if ammount < min: 
            min = ammount
            min_country = countries[i]
            min_year = years[i]
    print(f"The greatest life expectancy is: {max} from {max_country} in {max_year}.")
     
    print(f"The lowest life expectancy is: {min} from {min_country} in {min_year}.")
    print("")
    print(f"For the year {year}:")
    
    average = years_sum / len(years_list)
    print(f"The average life expectancy was: {average:.2f}")
    print(f"The maximum life expectancy was in {max_country_user} with {max_life_user}.")
    print(f"The minimun life expectancy was in {min_country_user} with {min_life_user}.")