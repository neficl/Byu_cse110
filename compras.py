#Néfi Leite - Byu

from math import prod


comprasProdutos = []
comprasQuantidade = []
comprasPrecos = []
carrinho = []

preco = 0
produto = " "

print("\nWelcome to the Gift Supermarket!\n")

op = 0
while op != 5:
     print("-----------------------"
        "\n1- Add item\n"
        "2- View cart\n"
        "3- Remove item\n"
        "4- Compute total\n"
        "5- Quit\n"
        "-----------------------\n")
     op = int(input("Please select one of the following: "))
     
     if op == 1:
          print()
        
          produto = str(input("What item would you like to add? "))
          quantidade = int(input("How many units of this product? "))
          preco = float(input(f"What is the price of '{produto}'? "))
          print(f'{produto} has a beem added to the cart.\n')
     
          comprasProdutos.append(produto)
          comprasQuantidade.append(int(quantidade))
          comprasPrecos.append(float(preco))
          carrinho.append(str("---"))
     
     elif op == 2:
        if len(comprasProdutos) == 0:
               print("Empty list!\n")    
          
        i = 1
        print("----------------------------------------------------") 
        for x in range(len(comprasProdutos)):
            print(i,"- Products: ",comprasProdutos[x]," - Units: ",comprasQuantidade[x]," - Price: R$ ",comprasPrecos[x],"", carrinho[x]) 
            i += 1
        print("----------------------------------------------------") 
     
     elif op == 3: #I had difficult to remove the items
          index = 1
          print("----------------------------------------------------") 
          for x in range(len(comprasProdutos)):
            print(index,"- Products: ",comprasProdutos[x]," - Units: ",comprasQuantidade[x]," - Price: R$ ",comprasPrecos[x],"", carrinho[x]) 
            index += 1
          print("----------------------------------------------------") 
          remove = int(input("What's your choice? Type the code product "))
          index = remove
          comprasProdutos.pop(index)
          comprasQuantidade.pop(index)
          comprasPrecos.pop(index)
              
     elif op == 4:
        resultado = 0
        for x in range(len(comprasProdutos)):
            resultado = (resultado + (comprasQuantidade[x] * comprasPrecos[x]))
        print("\nTotal: R$", resultado)    

     elif op == 5:
          print("Thank you. See you later!")
    
     else:
          print("Wrong code, type again!") 

