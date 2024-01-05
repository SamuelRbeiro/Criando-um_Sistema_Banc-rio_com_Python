import os
input ("Bem vindo ao nosso banco!!!\n")

#variaveis
saldo=0
limete=500
quantidade_de_saque=0
LIMITE_DE_VEZES_SAQUES=3  
extratos=""
#textos
menu_opção ="""Nossas operaçoes:
[1]Deposito
[2]Saque
[3]Extrato
[4]Sair
"""
texto_deposito="""Quanto deseja depositar?
R$"""


texto_sair="""Operaçoes encerradas"""

while True:
    operacao_escolhida=int(input(menu_opção))

    deposito= operacao_escolhida==1
    saque= operacao_escolhida==2
    extrato= operacao_escolhida==3
    sair= operacao_escolhida==4 

    os.system("cls")
    os.system("clear")  

    #Deposito
    if deposito:
        valor_deposito=int(input(texto_deposito))
         
        if valor_deposito>0 :
            saldo+=valor_deposito
            extratos+= f"Deposito de {valor_deposito:.2f}\n"
            input(f"Deposito de R${valor_deposito:.2f} realizado com sucesso!!!")
        else:
            input("Deposito invalido")

        os.system("cls")
        os.system("clear")
    
    #Saque
    elif saque:
        #texto Saque
        texto_saque=f"""Quantos reais você quer sacar?
Você tem R$ {saldo}
Sao permitidos saques de até R${limete} e 3 vezes ao dia
R$"""
        if saldo>0 and quantidade_de_saque<LIMITE_DE_VEZES_SAQUES:
            
            valor_saque= int(input(texto_saque))
            
            if valor_saque >0 and valor_saque <= limete:
                saldo-=valor_saque
                extratos+= f"Saque  de {valor_saque:.2f}\n"
                input(f"Saque de R${valor_saque:.2f} realizado com sucesso!!!")
                quantidade_de_saque +=1

            else:
                input("Valor do Saque Invalido!!!")
        
            
        elif quantidade_de_saque ==LIMITE_DE_VEZES_SAQUES:
            input("Limite exedido!!!")
        else:
            input("Sem saldo!!!")

        os.system("cls")
        os.system("clear")
        
    #Extrato
    elif extrato:
        input(f"Suas ultimas ações foram:\n{extratos}") 
        os.system("cls")
        os.system("clear")
        
    #Sair
    elif sair:
        print("Obrigado pela atenção!!!")
        print(texto_sair)
        break
        
    #Não existe essa possibilidade
    else:
        input("Opção invalida!!!")
    
        os.system("cls")
        os.system("clear")
        