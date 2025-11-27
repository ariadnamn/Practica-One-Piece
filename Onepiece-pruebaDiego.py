dict_characters = { 1 : {"name" : "Luffy","category": 1, "weapons": [1, 1],"strength" : 6, "speed" :
7,"experience": 0},
2 : {"name" : "Zoro","category": 1, "weapons" : [4],"strength" : 5, "speed" : 6,"experience":
0},
3 : {"name" : "Sanji", "category" : 1, "weapons" : [1,3],"strength" : 4, "speed" :
6,"experience": 0 },
4 : {"name" : "Buggy", "category" : 2, "weapons" : [3], "strength" : 2, "speed" : 4,
"experience" : 0},
5 : {"name" : "Mr3", "category" : 2, "weapons" : [5], "strength" : 3, "speed" : 2, "experience"
: 0},
6 : {"name" : "Xebec", "category" : 3, "weapons" : [1,3], "strength" : 6, "speed" : 5,
"experience" : 0},
7 : {"name" : "Kaido", "category" : 3, "weapons" : [4], "strength" : 8, "speed" : 3,
"experience" : 0},
8 : {"name" : "Mama grande", "category" : 3, "weapons" : [5], "strength" : 7, "speed" : 1,
"experience" : 0},
9 : {"name" : "Akainu", "category" : 4, "weapons" : [2], "strength" : 6, "speed" : 4,
"experience" : 0},
10 : {"name" : "Kizaru", "category" : 4, "weapons" : [1,3], "strength" : 5, "speed" : 8,
"experience" : 0},
11 : {"name" : "Fujitora", "category" : 4, "weapons" : [5], "strength" : 5, "speed" : 4,
"experience" : 0},
12 : {"name" : "Garp", "category" : 5, "weapons" : [2], "strength" : 6, "speed" : 3,
"experience" : 0},
13 : {"name" : "Smoker", "category" : 5, "weapons" : [5], "strength" : 5, "speed" : 5,
"experience" : 0},
14 : {"name" : "Koby", "category" : 6, "weapons" : [4], "strength" : 3, "speed" : 4,
"experience" : 0},
15 : {"name" : "Tashigi", "category" : 6, "weapons" : [3], "strength" : 4, "speed" : 4,
"experience" : 0},
}

dict_weapons = { 1 : {"name" : "Sword","strength": 3,"speed": 5,"two_hand":False},
2 : {"name" : "Greatsword","strength": 5,"speed": 3,"two_hand":True},
3 : {"name" : "Gun","strength": 2,"speed": 6,"two_hand":False},
4: {"name": "Rifle", "strength": 3, "speed": 4,"two_hand":True},
5: {"name": "Chuchi", "strength": 4, "speed": 4,"two_hand":True},
}

dict_crews = { 1 : {"name" : "Straw hat","members": [8,6]},
2 : {"name" : "Pirates Buggy","members": [1,3,5]},
3: {"name": "Pirates Rocks","members": [2,4,7,]}
}

dict_ranks = { 1 : {"name" : "Admiral","members": [9,10,11]},
2 : {"name" : "ViceAdmiral","members": [12,13]},
3: {"name": "Lieutenant","members": [14,15]}
}

dict_categorys = {1:"Straw hat",2:"Pirates Buggy",3:"Pirates Rocks", 4:"Admiral",5:"ViceAdmiral",6:"Lieutenant"}

#================MENUS=====================
titulo = "\n"+"=" * 20 + "{}" + "=" * 20+"\n"
menu0="\n1) Play\n2) Create\n3) Edit\n4) List\n5) Exit"
menu02="\n1) Create Character\n2) Create Weapon\n3) Go back"
menu03="\n1) Edit character\n2) Edit weapon\n3) Go back"
menu031="\n1) Name\n2) Weapon\n3) Go Back"
side="\n1) Marine\n2) Pirates"

#=========FLAGS===========
fin_juego=False
jugando=True
equipo=True
edit_menu=True
#=========STATS===========
ganador=" "
while not fin_juego:
        print(titulo.format(" Menu 0 (One Piece) "), menu0)
        op_menu0=int(input("\n-> Option: "))
        if op_menu0==1:
            print()



#====================================
# ========MENU02(CREATE)=============
# ===================================            
        elif op_menu0==2:
            
            menu_02=True
            while  menu_02:
                print(titulo.format(" Menu02 Create "), menu02)
                
                op_menu02=int(input("\n-> Option: "))
                if op_menu02==1:
                    print(titulo.format("Menu021 New Character"))
                    #accedemos al ultimo id para añadir uno despues
                    ultimo_id=0
                    for i in dict_characters:
                        if i >ultimo_id:
                            ultimo_id=i
                    nuevo_id=ultimo_id+1
                    new_name=input("Name of the new character:\n ")


                    while equipo:
                        print("\nType of the new character: ", side)
                        op_side=int(input("\n->Optioin: "))
                        if op_side==1:
                            #=========
                            #==RANKS==
                            #=========
                            for rank in dict_categorys:

                                #************************************
                                #ESTO  DE ABAJO ESTÁ MAL CORREGIR MAS TARDE

                                #****************************
                                print(dict_categorys[-1])
                                print(dict_categorys[-2])
                                print(dict_categorys[-3])
                                
                            op_rank=int(input("\n->Option: "))
                            equipo=False
                        elif op_side==2:
                            #============
                            #==category==
                            #============
                            print()
                            equipo=False
                        else:
                            print(titulo.format("INVALID OPTION"))
                            input("Press enter to continue")
                            equipo=True
                    
                elif op_menu02==2:
                    print(titulo.format(" Menu022 (New Weapon) "))
                    new_weapon=input("Name of the new weapon:\n")
                elif op_menu02==3:
                    menu_02=False
                else:
                    print("Opcion invalida")
                    menu_02=False
                
            
#====================================
# ==========MENU03 (EDIT)============
# ===================================  
        elif op_menu0==3:
             menu_03=True
             while  menu_03:
                print(titulo.format(" Menu03 (Edit Menu) "), menu03)
                op_menu03=int(input("\n-> Option: "))
                if op_menu03==1:
                    while edit_menu:
                        print(titulo.format("Menu031 (Select Charcater to edit)"))
                        print("\n" + "="*60)
                        print("ID".ljust(5), "NAME".ljust(15),"CATEGORY".ljust(10), "WEAPONS".ljust(10), "STRENGHT".ljust(10), "SPEED".ljust(10))
                        print("="*60)

                        for key in dict_characters:
                            name = dict_characters[key]["name"]
                            category = str(dict_characters[key]["category"])
                            weapons = str(dict_characters[key]["weapons"])
                            strength = str(dict_characters[key]["strength"])
                            speed = str(dict_characters[key]["speed"])
                            

                            print(str(key).ljust(5), name.ljust(15), category.ljust(10), weapons.ljust(10), strength.ljust(10), speed.ljust(10))

                        print("="*60 + "\n")

                        id_edit=int(input("ID to edit:\n "))
                        if id_edit not in dict_characters:
                            print("Opcion no valida")
                            edit_menu=True
                        else: 
                            
                            edit_menu=False
                            nombre_personaje = dict_characters[id_edit]["name"]
                            print(f"\nSelect feature to edit to character ID: {id_edit}, Name: {nombre_personaje}")
                            print(f"\n1. Name\n2. Category\n3. Weapon\n4. Strenght\n5. Speed ")
                            op=int(input("\n-> Option: "))
                            if op ==1:
                                edit_new_name=input("Put the nwe name of character")
                            elif op ==2:
                                print("Select de new category")
                            elif op ==3:
                                print("New Weapon")
                            elif op ==4:
                                print("Choose de level of strenght 1-9")
                            elif op ==5:
                                print("Choose de level of speed 1-9")
                elif op_menu03==2:
                    print(titulo.format(" Menu032 (Select Weapon to Edit) "))
                    new_weapon=input("Name of the new weapon:\n")
                elif op_menu03==3:
                    menu_03=False
                else:
                    print("Opcion invalida")
                    menu_03=False
                
            
           
        elif op_menu0==4:
            print()
        elif op_menu0==5:
            print("BYE BYE")
            fin_juego=True

        else:
            print("opcion invalida")
            fin_juego=False