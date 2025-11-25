titulo = "=" * 20 + "{}" + "=" * 20+"\n"
menu0="\n1) Play\n2) Create\n3) Edit\n4) List\n5) Exit"
menu02="\n1) Create Character\n2) Create Weapon\n3) Go back"
print(titulo.format(" Menu 0 (One Piece) "), menu0)
op_menu0=int(input("\n-> Option: "))

fin_juego=False
jugando=True
while not fin_juego:
    while jugando:
        if op_menu0==1:
            print()
        elif op_menu0==2:
            print(titulo.format(" Menu02 Create "), menu02)
            jugando=False
            

        elif op_menu0==3:
            print()
        elif op_menu0==4:
            print()
        elif op_menu0==5:
            print("BYE BYE")
            fin_juego=True

        else:
            print()