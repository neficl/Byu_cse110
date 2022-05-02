#NéfiLeite - BYU

with open("lifexpectancy.csv") as expectancy_file:
    
    year_Ex = int(input("Enter the year of interest: "))
    
    country = []
    year = []
    life = []
    yearL = []
    yearS = 0
    max = 0
    min = 100
    country_Oficial = 0
    country_Oficial1 = 100
    
    for line in expectancy_file:
        # Split up the line based on the ","
        parts = line.strip()
        part = parts.split(",")
    
        country.append(part[0])
        year.append(part[2])
        life.append(part[3])   
        
        life_Max = -1
        life_Min = 999999
        
        if part[2] == year_Ex:
            yearL.append(part[2])
            yearS += float(part[3])
            lifeT = float(part[3])
            
            if lifeT > life_Max:
                
                life_Max = lifeT 
                country_Oficial = part[0]
                year_Oficial = float(part[3])
            
            if lifeT < life_Min:
                
                life_Min = lifeT 
                country_Oficial1 = part[0]
                year_Oficial1 = float(part[3])
                
    life.pop(0)
    for i in range(len(life)):
        lifeT = float(life[i])
        if lifeT > max:
            max = lifeT
            max_country = country[i]
            max_year = year[i]
        if lifeT < min: 
            min = lifeT
            min_country = country[i]
            min_year = year[i]
                

    print(f"The overall max life expectancy is {max} from: {max_country} in {max_year}")
    print(f"The overall min life expectancy is {min} from: {min_country} in {min_year}\n")

    print(f"For the year {year_Ex}: ")
    print(f"The max life expectancy was in {country_Oficial} with: {life_Max}")
    print(f"The min life expectancy was in {country_Oficial1} with: {life_Min}")