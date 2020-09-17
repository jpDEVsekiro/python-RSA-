# lista de caracteres //base//
alfaB=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','ç','P','Q','R','S','T','U','V','W','X','Y','Z'
       ,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
       ,'á','à','â','ã','Á','À','Ã','Â','é','ê','è','É','È','Ê','í','ì','î','Í','Ì','Î','ó','ò','õ','ô','Ó','Ò','Õ','Ô','ú','ù','û','Ú','Ù','Û','0'
       ,'1','2','3','4','5','6','7','8','9'
       ,'ª','°','º','´','`','~','^','!','@','#','$','%','¨','&','*','(',')','-','—','_','=','+','¢','£','¬','§','[','{',']','}','?','/','.',',',' ',':','"',';','º',"'",'"',"<",">",'®']
#lista de numeros para cada caractere
alfaN=[640,111,768,492,94,715,750,224,553,80,437,106,225,613,575,99,629,158,265,114,51,668,602,466,137,155,937,779,379,626,884,707,19,210,752,981,782,400,234,281,783,630,868,598,899,778,623
       ,976,319,205,13,590,321,351,582,836,998,446,537,702,748,593,282,441,573,84,264,914,286,845,650,953,849,949,529,496,181,346,643,774,897,68,706,271,720,732,541,98,393,410,975,712,185
       ,384,758,151,648,641,128,280,905,293,342,834,279,919,506,355,819,144,409,177,856,716,377,172,102,572,979,64,88,928,493,586,118,687,671,965,825,208,42,912,245,515,187,209,32,451,757
       ,508,312]
# pre codificaçao

fim=0
crip=[]        
while fim==0:
    resposta=input("digite C para criptografar D descriptografar e S para sair:  ")
    if resposta=="C" or resposta=="c" :
        crip=[]
        x=0
        #a=primo1
        #b=primo2
        f=0
        #gerador de primo1
        while f==0:
            from random import randrange, uniform
            a=randrange(0, 1000) #faixa de inteiro
            con=0
            for c in range(1, a+1):
                if a%c==0:
                    con+=1
            if con==2:
                f=5
        q=0
        #gerador de primo2
        while q==0:
            from random import randrange, uniform
            b=randrange(0, 1000) #faixa de inteiro
            con2=0
            for d in range(1, b+1):
                if b%d==0:
                    con2+=1
            if b!=a:
                if con2==2:
                    q=5
        primo1=a
        primo2=b
        #criacao da chava
        n=primo1*primo2 
        p=(primo1-1)*(primo2-1)
        e=2
        mdc = p
        while (mdc != 1):
            mdc = p
            e=e+1
            while p % mdc != 0 or e % mdc != 0:

                mdc = mdc - 1        

        preCod=[]
        x=0
        y=0
        mensagem=input("entre com a mensagem:  ")
        #precod
        while x<len(mensagem):
            if mensagem[x]==alfaB[y]:

                preCod.insert(x,alfaN[y])
                x=x+1
                y=0
            else:
                y=y+1

        t=0
        #encriptacao
        while t<len(preCod):
            cod=preCod[t]**e%n
            crip.insert(t,cod)
            t=t+1
        ç=0
        l=0
        while ç!=1:
            ç=(l*e)%p
            if ç!=1:
                l=l+1
                    
        print("chave privada N:",n)
        print ("chave privada D:",l)
        print (crip)
        crip=[]
    elif resposta=="S" or resposta=="s" :
        fim=1
    elif resposta=="D" or resposta=="d":
        crip=[]        
        n=int(input("digite N="))
        l=int(input("digite D="))
        x=0
        y=0
        z=1
        mensagem=""
        B=input("entre com a mensagem criptografada ||| coloque entre Colchetes e com virgulas [...,...] |||")
        digitos=['1','2','3','4','5','6','7','8','9','0']
        while x<len(B):
            if B[y:z]==(','):
                crip.append(int(mensagem))
                mensagem=""
            if B[y:z]==(']'):
                crip.append(int(mensagem))
                mensagem=""
            if B[y:z] in digitos:
                mensagem=mensagem+B[y:z]
                y=y+1
                x=x+1
                z=z+1
            else:
                y=y+1
                x=x+1
                z=z+1
        
        print("descriptografando")
        print(" 0%")
        #descobre o D da formula 
        
        u=0
        descrip=[]
        coddes=[]
        
        cod2=0
        r=0
        z=10
        x=0
        y=0
        #volta aos valores iniciais
        while u<len(crip):
            cod2=(crip[u]**l)%n
            descrip.insert(u,cod2)
            x=((len(descrip)*100)/len(crip))
            if x>=y:
                D="{0:2.0f}".format(x)
                print(D,"%")
                y=y+15
            u=u+1
                    
        G=0
        g=0
        descod='mensagem:'
        while g<len(descrip):
            #pega a posição dos numeros em relação as letras
            if descrip[g]==alfaN[G]:
                coddes.insert(g,alfaB[G])
                descod=descod+coddes[g]
                g=g+1
                G=0
               
            else:
                G=G+1       
        print(descod)    
    else:
        print("digite C ou D ou S por favor")
