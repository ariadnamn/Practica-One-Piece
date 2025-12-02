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
                    edit_menu=True
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
                            editing=True
                            while editing:
                                print(f"\nSelect feature to edit to character ID: {id_edit}, Name: {nombre_personaje}")
                                print(menu031)
                                op=int(input("\n-> Option: "))
                                if op ==1:
                                    edit_menu=True
                                    edit_new_name=input("Put the new name of character: ")
                                    dict_characters[id_edit]["name"]=edit_new_name
                                    print(f"\nName changed successfully! New name: {dict_characters[id_edit]['name']}")
                                    continue_editing=True
                                    while continue_editing:
                                        op_continue_editing_name=input("Do you want continue editing? Y/N: ").lower()
                                        
                                        if op_continue_editing_name=="y":
                                            #SOLO SALIMOS DEL BUCLE PARA EDITAR EL NAME
                                            continue_editing=False 
                                        elif op_continue_editing_name=="n":
                                            #SALIMOS DE TODOS LOS WHILE Y VOLVEMOS AL MENU PRINCIPAL
                                            continue_editing=False
                                            editing=False
                                            edit_menu=False
                                            menu_03=False
                                        else:
                                            print("Incorrect option")
                                            continue_editing=True                    
                                elif op ==2:
                                    menu_edit_character_weapons=True
                                    while menu_edit_character_weapons:
                                        char_weapons = dict_characters[id_edit]["weapons"]

                                        used_hands = 0
                                        for wid in char_weapons:
                                            if dict_weapons[wid]["two_hand"]:
                                                used_hands += 2
                                            else:
                                                used_hands += 1

                                        hands = 2 - used_hands

                                        print(titulo.format("Available Weapons"))
                                        if hands==0:
                                            print("\n------------------None------------------")
                                        else:
                                            for wid, weapon_data in dict_weapons.items():

                                                # Si el arma ocupa 2 manos, solo mostrar si hands == 2
                                                if weapon_data["two_hand"] and hands < 2:
                                                    continue

                                                # Si ocupa 1 mano, mostrar si hands >= 1
                                                if not weapon_data["two_hand"] and hands < 1:
                                                    continue

                                                print(f"{wid}) {weapon_data['name']}, Strength {weapon_data['strength']}, Speed {weapon_data['speed']}")

                                        print(titulo.format("Character weapons"))

                                        if len(char_weapons) == 0:
                                            print("\n----------------------None----------------------")
                                        else:
                                            for index, weapon_id in enumerate(char_weapons, start=1):
                                                weapon_data = dict_weapons[weapon_id]
                                                name = weapon_data["name"]
                                                strength = weapon_data["strength"]
                                                speed = weapon_data["speed"]
                                                print(f"{weapon_id}) {name}, Strength: {strength}, Speed {speed}")

                                    
                                        print("\nAdd Weapons:")
                                        print("Weapon Id) To add weapon") 
                                        print("Id 0 to finish add weapons")
                                        print("-Weapon Id to delete weapon Id ")
                                        op_edit_weapon=int(input("-> Option: "))

                                        menu_edit_character_weapons=False
                                        if op_edit_weapon==0:
                                            menu_edit_character_weapons=False
                                        elif op_edit_weapon>0:
                                            dict_characters[id_edit]["weapons"].append(op_edit_weapon)
                                        elif op_edit_weapon<0:
                                            weapon_to_delete = -op_edit_weapon
                                            if weapon_to_delete in dict_characters[id_edit]["weapons"]:
                                                dict_characters[id_edit]["weapons"].remove(weapon_to_delete)
                                        
                                        

                                    # #SCAMOS LA CATEGORIA ACTUAL DEL PERS. SELCCIONADO
                                    # categoria_actual_id = dict_characters[id_edit]["category"]
                                    # categoria_actual_nombre = dict_categorys[categoria_actual_id]
                                    # print(f"\nYour category now is: {categoria_actual_nombre} (ID: {categoria_actual_id})")

                                    # #MOSTRAMOS TODAS LA CATEGORIAS QUE PUEDE ESCOGER
                                    # for cat_id in dict_categorys:
                                    #     print(f"{cat_id}. {dict_categorys[cat_id]}")

                                    
                                    # nueva_categoria = int(input("\nSelect the new category ID: "))

                                    
                                    # if nueva_categoria in dict_categorys:
                                    #     dict_characters[id_edit]["category"] = nueva_categoria
                                    #     print(f"\nCategory changed successfully! New category: {dict_categorys[nueva_categoria]}")
                                    # else:
                                    #     print("\nInvalid category ID. Category not changed.")

                                    # op_continue_editing_category = input("\nDo you want to continue editing? Y/N: ").lower()
                                    # if op_continue_editing_category == "y":
                                    #     #SALIMOS SOLO DEL BUCLE PARA EDIATR LA CATEGORIA
                                    #     continue_editing=False
                                        
                                    # elif op_continue_editing_category == "n":
                                    #     editing = False
                                    #     edit_menu = False
                                    #     menu_03 = False
                                    # else:
                                    #     print("Incorrect option")
                                    #     continue_editing=True

                                elif op ==3:
                                    editing=False
                                    edit_menu=False
                                
                elif op_menu03==2:
                    print(titulo.format(" Menu032 (Select Weapon to Edit) "))
                    print(titulo.format("All Weapons"))

                    for wid in dict_weapons:
                        weapon = dict_weapons[wid]
                        print(f"{wid}) {weapon['name']}, Strength: {weapon['strength']}, Speed: {weapon['speed']}, Two-Hand: {weapon['two_hand']}")
                    weapon_id=int(input("\nID weapon to edit: "))
                    if weapon_id not in dict_weapons:
                        print("Invalid weapon ID")
                    else:
                        editing_weapon=True
                        while editing_weapon:
                            print(titulo.format("Menu 032X (Weapon Feature to Edit)"))
                            print("\n1)Name")
                            print("2)Plus Strenght")
                            print("3)Plus Speed")
                            print("4)Go back")
                            print("\nSelect feature to edit to weapon")
                            op_menu032x=int(input("-> Option: "))
                            if op_menu032x ==1:
                                new_name_weapon= input("Enter the new name: ")
                                old_name=dict_weapons[weapon_id]["name"]
                                confirm= input(f"\nDo you want to change {old_name} by {new_name_weapon}? Y/N: ").lower()
                                if confirm=="y":
                                    dict_weapons[weapon_id]["name"]=new_name_weapon
                                    print("\nName changed")
                                else:
                                    print("\nName change cancelled")
                            elif op_menu032x ==2:
                                print()
                            elif op_menu032x==3:
                                print()
                            elif op_menu032x ==4:
                                editing_weapon =False
                            else:
                                print("Invalid option")

                elif op_menu03==3:
                    menu_03=False
                else:
                    print("Opcion invalida")
                    menu_03=False
                
#====================================
# ==========MENU04 (LIST)============
# ===================================              
           
        elif op_menu0==4:
            menu_04 = True
            while menu_04:
                print(titulo.format(" Menu04 (List) "))
                print("\n1) List Characters\n2) List Weapons\n3) List Crews\n4) List Ranks\n5) Go back")
                op_menu04 = int(input("\n-> Option: "))

                #===========================
                # 1) LIST CHARACTERS
                #===========================
                if op_menu04 == 1:
                    menu_list_char = True
                    while menu_list_char:
                        print(titulo.format(" List Characters "))
                        print("\n1) List by ID\n2) List by Name\n3) List by Strength\n4) List by Speed\n5) Go back")
                        op_char = int(input("\n-> Option: "))

                        lista_ids = list(dict_characters.keys())

                        # Ordenar por ID
                        if op_char == 1:
                            for pasada in range(len(lista_ids)-1):
                                cambio=False
                                for i in range(len(lista_ids)-1-pasada):
                                    if lista_ids[i] > lista_ids[i+1]:
                                        cambio=True
                                        aux=lista_ids[i]
                                        lista_ids[i]=lista_ids[i+1]
                                        lista_ids[i+1]=aux
                                if not cambio:
                                    break

                        # Ordenar por Name
                        elif op_char == 2:
                            for pasada in range(len(lista_ids)-1):
                                cambio=False
                                for i in range(len(lista_ids)-1-pasada):
                                    n1=dict_characters[lista_ids[i]]["name"].lower()
                                    n2=dict_characters[lista_ids[i+1]]["name"].lower()
                                    if n1 > n2:
                                        cambio=True
                                        aux=lista_ids[i]
                                        lista_ids[i]=lista_ids[i+1]
                                        lista_ids[i+1]=aux
                                if not cambio:
                                    break

                        # Ordenar por Strength
                        elif op_char == 3:
                            for pasada in range(len(lista_ids)-1):
                                cambio=False
                                for i in range(len(lista_ids)-1-pasada):
                                    f1=dict_characters[lista_ids[i]]["strength"]
                                    f2=dict_characters[lista_ids[i+1]]["strength"]
                                    if f1 > f2:
                                        cambio=True
                                        aux=lista_ids[i]
                                        lista_ids[i]=lista_ids[i+1]
                                        lista_ids[i+1]=aux
                                if not cambio:
                                    break

                        # Ordenar por Speed
                        elif op_char == 4:
                            for pasada in range(len(lista_ids)-1):
                                cambio=False
                                for i in range(len(lista_ids)-1-pasada):
                                    s1=dict_characters[lista_ids[i]]["speed"]
                                    s2=dict_characters[lista_ids[i+1]]["speed"]
                                    if s1 > s2:
                                        cambio=True
                                        aux=lista_ids[i]
                                        lista_ids[i]=lista_ids[i+1]
                                        lista_ids[i+1]=aux
                                if not cambio:
                                    break

                        elif op_char == 5:
                            menu_list_char=False
                            op_char=-1

                        else:
                            print("Invalid option")
                            op_char=-1

                        if op_char in (1,2,3,4):
                            print("\n" + "="*70)
                            print("ID".ljust(5), "NAME".ljust(15), "CATEGORY".ljust(10),
                                "WEAPONS".ljust(15), "STR".ljust(5), "SPD".ljust(5))
                            print("="*70)

                            for cid in lista_ids:
                                p = dict_characters[cid]
                                print(str(cid).ljust(5),
                                    p["name"].ljust(15),
                                    str(p["category"]).ljust(10),
                                    str(p["weapons"]).ljust(15),
                                    str(p["strength"]).ljust(5),
                                    str(p["speed"]).ljust(5))

                            print("="*70)
                            input("Press Enter to continue")

                #===========================
                # 2) LIST WEAPONS
                #===========================
                elif op_menu04 == 2:
                            menu_list_weap=True
                            while menu_list_weap:
                                print(titulo.format(" List Weapons "))
                                print("\n1) List by ID\n2) List by Name\n3) List by Strength\n4) List by Speed\n5) Go back")
                                op_weap = int(input("\n-> Option: "))

                                lista_ids=list(dict_weapons.keys())

                                if op_weap == 1:
                                    for pasada in range(len(lista_ids)-1):
                                        cambio=False
                                        for i in range(len(lista_ids)-1-pasada):
                                            if lista_ids[i] > lista_ids[i+1]:
                                                cambio=True
                                                aux=lista_ids[i]
                                                lista_ids[i]=lista_ids[i+1]
                                                lista_ids[i+1]=aux
                                        if not cambio:
                                            break

                                elif op_weap == 2:
                                    for pasada in range(len(lista_ids)-1):
                                        cambio=False
                                        for i in range(len(lista_ids)-1-pasada):
                                            n1=dict_weapons[lista_ids[i]]["name"].lower()
                                            n2=dict_weapons[lista_ids[i+1]]["name"].lower()
                                            if n1 > n2:
                                                cambio=True
                                                aux=lista_ids[i]
                                                lista_ids[i]=lista_ids[i+1]
                                                lista_ids[i+1]=aux
                                        if not cambio:
                                            break

                                elif op_weap == 3:
                                    for pasada in range(len(lista_ids)-1):
                                        cambio=False
                                        for i in range(len(lista_ids)-1-pasada):
                                            if dict_weapons[lista_ids[i]]["strength"] > dict_weapons[lista_ids[i+1]]["strength"]:
                                                cambio=True
                                                aux=lista_ids[i]
                                                lista_ids[i]=lista_ids[i+1]
                                                lista_ids[i+1]=aux
                                        if not cambio:
                                            break

                                elif op_weap == 4:
                                    for pasada in range(len(lista_ids)-1):
                                        cambio=False
                                        for i in range(len(lista_ids)-1-pasada):
                                            if dict_weapons[lista_ids[i]]["speed"] > dict_weapons[lista_ids[i+1]]["speed"]:
                                                cambio=True
                                                aux=lista_ids[i]
                                                lista_ids[i]=lista_ids[i+1]
                                                lista_ids[i+1]=aux
                                        if not cambio:
                                            break

                                elif op_weap == 5:
                                    menu_list_weap=False
                                    op_weap=-1

                                else:
                                    print("Invalid option")
                                    op_weap=-1

                                if op_weap in (1,2,3,4):
                                    print("\n" + "="*60)
                                    print("ID".ljust(5), "NAME".ljust(15), "STR".ljust(5),
                                        "SPD".ljust(5), "2H?".ljust(5))
                                    print("="*60)

                                    for wid in lista_ids:
                                        w=dict_weapons[wid]
                                        print(str(wid).ljust(5),
                                            w["name"].ljust(15),
                                            str(w["strength"]).ljust(5),
                                            str(w["speed"]).ljust(5),
                                            str(w["two_hand"]).ljust(5))
                                    print("="*60)
                                    input("Press Enter to continue")

                #===========================
                # 3) LIST CREWS
                #===========================
                elif op_menu04 == 3:
                            print(titulo.format(" Crews List "))
                            print("ID".ljust(5), "NAME".ljust(20), "MEMBERS")
                            print("="*60)

                            for cid in dict_crews:
                                print(str(cid).ljust(5),
                                    dict_crews[cid]["name"].ljust(20),
                                    str(dict_crews[cid]["members"]))

                            input("Press Enter to continue")

                #===========================
                # 4) LIST RANKS
                #===========================
                elif op_menu04 == 4:
                            print(titulo.format(" Ranks List "))
                            print("ID".ljust(5), "NAME".ljust(20), "MEMBERS")
                            print("="*60)

                            for rid in dict_ranks:
                                print(str(rid).ljust(5),
                                    dict_ranks[rid]["name"].ljust(20),
                                    str(dict_ranks[rid]["members"]))

                            input("Press Enter to continue")

                #===========================
                # 5) GO BACK
                #===========================
                elif op_menu04 == 5:
                            menu_list_weap=False
                            menu_04=False

                else:
                            print("Invalid option")
        elif op_menu0==5:
            print("BYE BYE")
            fin_juego=True

        else:
            print("opcion invalida")
            fin_juego=False