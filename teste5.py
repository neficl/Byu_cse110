from math import prod


print("Welcome to the Gift Supermarket!\n")

op = 0
while op != 5:
    print("1- Add item\n"
        "2- View cart\n"
        "3- Remove item\n"
        "4- Compute total\n"
        "5- Quit\n")
    op = int(input("Please select one of the following: "))
    compras = []
    produto = []
    preco = []
    numero = []
    i = 0
    total = 0
    preco = 0
    antigo = 0
    
    if op == 1:
        print()
        quantidade = int(input("How many foods you want to register? "))
        print()
        
        for i in quantidade:
            produto = input("What item would you like to add? ")
            numero = i + 1
            preco = float(input(f"What is the price of '{produto}'? "))
            print(f'{produto} has a beem added to the cart.')
            numero.append[i]
            produto.append[i]
            preco.append[i]
            
            total = preco + antigo
            antigo = total
        
    elif op == 2:    
        for i in range(len(produto)):
            numero = i +1
            produto = produto[i]
            preco = preco[i]
            print(f"{numero}. {produto} -  ${preco:.2f}")
            
    elif op == 3:
        print("Which product do you want to remove?")
        
            for i in range(len(produto)):
                numero = i +1
                produto = produto[i]
                print(f" {numero} - {produto}")
                remove = int(input("What's your choice? Type the code product"))
            if remove > len(produto):
                print("The number you typed is not available. Please, try again.")
                remove = int(input("Which item would you like to remove? "))
                
        
    elif op == 4:
        print("Total: ${total}}")

    elif op == 5:
        print("Thank you. Goodbye!")
    
    else:
        print("Wrong code, type again!")
    
   
compras = [   ]
while True:
     produto = input("Produto: ")
     if produto == "fim":
         break
     quantidade = int(input("Quantidade: "))
     preco = float(input("Preco: "))
     compras.append([produto, quantidade, preco])
soma = 0.0
for e in compras:
     print("%20s x%5d %5.2f %6.2f" % (e[0], e[1],e[2],e[1] * e[2]))
     soma += e[1] * e[2]
print("Total: %7.2f" % soma)