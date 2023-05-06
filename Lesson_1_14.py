# """
#     BOOKS CRUD

#     book = {
#         "id": 1,
#         "page": 100,
#         "price": 12.9,
#         "langue": "uz",
#         "another": "Kamol",
#         "title": "Python 3.10 tutorial",
#         "description": "Pythonni boshlang'ichini o'rganish",
#     }

#     shunday data bo'ladi. 

#     MENUda
    
#         =======================================
#         === 1) All The Books see            ===
#         === 2) Create Books                 ===
#         === 3) Select Book (id)             ===
#         === 4) Update Book (id)             ===
#         === 5) Delete Book (id)             ===
#         =======================================

#     menyudan 1 ni bosganda shu bo'lim ishga tushishi kerak.


#     ALL THE BOOKS SEE ===> SECTION

#         =======================================
#         === ID: 1                           ===
#         === Title: Python 3.10 tutorial     ===
#         === Another: Kamol                  ===
#         === Langue: uz                      ===
#         === Price: 12.9                     ===
#         === Description: Pythonni boshla... ===
#         =======================================

#         =======================================
#         === ID: 2                           ===
#         === Title: Python 3.10 tutorial     ===
#         === Anthor: Kamol                   ===
#         === Langues: uz                     ===
#         === Price: 12.9                     ===
#         === Description: Pythonni boshla... ===
#         =======================================

#         =======================================
#         === ID: 3                           ===
#         === Title: Python 3.10 tutorial     ===
#         === Anthor: Kamol                   ===
#         === Langues: uz                     ===
#         === Price: 12.9                     ===
#         === Description: Pythonni boshla... ===
#         =======================================


#     CREATE BOOK =====> SECTION:

#         inputdan: "title", "another", "langue". "price", "deccription", "page"

#         title check:
#             len 15 tadan 30 tagacha
#             ichida harf yoki sonlar bo'lishi kerak.

#         another check: 
#             len 3 tadan 20 tagacha
#             faqat harlar bo'lishi kerak
    
#         langues check: 
#             len 2 ta
#             uz, ru, en

#         price check:
#             1 dan katta bo'lsin

#         deccription check:
#             len 20 tadan 50 tagacha

#         page check:
#             5 tadan katta yoki teng bo'lsin 

#         o'ziz id berasiz.

#         keyin hamma ma' lumotlarni qabul qilib.
#         Xudi shunday menu chiqarasiz

#         =======================================
#         === ID: 2                           ===
#         === Title: Python 3.10 tutorial     ===
#         === Anthor: Kamol                   ===
#         === Langues: uz                     ===
#         === Price: 12.9                     ===
#         === Page: 5                         ===
#         === Description: Pythonni boshla... ===
#         =======================================

#         inputdan tasdiqlaydi. y yoki n
#         agar y bo'lsa listni ichiga append qilinadi.
#         agarda n bo'lsa listga append qilinmaydi.
#         Meyuga chiqarib yuboriladi.


#     SELECET BOOK =====> SECTION

#         inputdan (id) olinadi keyin o'sha aydiga tegishli bookni chiqarib beriladi.

#         =======================================
#         === ID: 2                           
#         === Title: Python 3.10 tutorial     
#         === Anthor: Kamol                   
#         === Langues: uz                     
#         === Price: 12.9                     
#         === Page: 5                        
#         === Description: Pythonni boshla
#         =======================================
# """

BOOKS__CRUD = []

book__1 = {
        "id": 1,
        "page": 100,
        "price": 12.9,
        "langue": "uz",
        "another": "Kamol",
        "title": "Python 3.10 tutorial",
        "description": "Pythonni boshlang'ichini o'rganish",
    }

book__2 = {
        "id": 2,
        "page": 110,
        "price": 14.0,
        "langue": "ru",
        "another": "Durbek",
        "title": "Java script tutorial",
        "description": "Java scriptni boshlangi'ichini o'rganish",
    }

book__3 = {
        "id": 3,
        "page": 120,
        "price": 16.4,
        "langue": "en",
        "another": "Dilshod",
        "title": "C++ tutorial",
        "description": "C++ ni boshlang'ichini o'rganish",
    }

book__4 = {
        "id": 4,
        "page": 130,
        "price": 19.5,
        "langue": "fr",
        "another": "Behro'z",
        "title": "SMM tutorial",
        "description": "SMMni boshlang'ichini o'rganish",
    }

book__5 = {
        "id": 5,
        "page": 150,
        "price": 20.5,
        "langue": "ne",
        "another": "Lochin",
        "title": "Css tutorial",
        "description": "Cssni boshlang'ichini o'rganish",
    }

BOOKS__CRUD.append(book__1)
BOOKS__CRUD.append(book__2)
BOOKS__CRUD.append(book__3)
BOOKS__CRUD.append(book__4)
BOOKS__CRUD.append(book__5)

def console__print(book__data):
    print(f"=======================================")
    print(f"===> ID: {book__data['id'] }")
    print(f"===> Title: {book__data['title']}")
    print(f"===> Another: {book__data['another']}")
    print(f"===> Langue: {book__data['langue']}")
    print(f"===> Price: {book__data['price']}")
    print(f"===> Page: {book__data['page']}")
    print(f"===> Description: {book__data['description']}")
    print(f"=======================================\n")

def ALL__THE__BOOKS__SEE():
    print("===>>> ALL__THE__BOOKS__SEE bo'limiga xush kelibsiz <<<===")

    for i in BOOKS__CRUD:
        console__print(i)

    MENU()
                
def CREATE__BOOKS():

    print("===>>> CREATE__BOOKS bo'limiga xush kelibsiz <<<===")

    while True:
        check__boolean = {
            "title": False,
            "another": False,             
            "langue": False,
            "price": False,
            "page": False,
            "description": False,
            "check": False,
            }
        
        last__book = BOOKS__CRUD.pop()
        id = last__book['id'] + 1
        title = input("Siz titleyingizni kiriting: ")
        another = input("Siz anotheringizni kiriting: ")
        langue = input("Siz languengizni kiriting: ")
        price = input("Siz pricengizni kiriting: ")
        page = input("Siz pagengizni kiriting: ")
        description = input("Siz discriptioningizni kiriting: ")

        if len(title) >= 15 and len(title) <= 30: 
            check__boolean['title'] = True
        else: 
            print("Siz titleni ma'lumotlarini to'g'ri kiritmadingiz.")

        if len(another) >= 3 and len(another) <= 20:
            check__boolean["another"] = True

        else:
            print("Siz anotherni ma'lumotlarini to'g'ri kiritmadingiz. ")

        if len(langue) >= 2:
            check__boolean["langue"] = True

        else:
            print("Siz lagueni ma'lumotlarini to'g'ri kiritmagansiz.")

        if len(price) >= 1:
            check__boolean['price'] = True

        else:
            print("Siz priceni ma'lumotini to'g'ri kiritmadingiz.")

        if len(page) <= 5:
            check__boolean["page"] = True

        else:
            print("Siz pageni ma'lumotini to'g'ri kiritmadingiz.")

        if len(description) >= 20 and len(description) <= 50:
            check__boolean["description"] = True

        else:
            print("Siz descriptionni ma'lumotini to'g'ri kiritmadingiz.")
        
        tasdiqlash = input("Siz tasdiqlang. To'g'ri bo'lsa (t) noto'g'ri bo'lsa (n): ")

        if tasdiqlash == 't':
            check__boolean["check"] = True

        else:
            print("Tasdiqlanmadi")
            MENU()
            break

        if check__boolean['check']:
            if check__boolean['title'] and check__boolean['another'] and check__boolean['langue'] and check__boolean['price'] and check__boolean['page'] and check__boolean['description'] :
                BOOKS__CRUD.append({
                    "id": id,
                    "title": title,
                    "another": another,             
                    "langue": langue,
                    "price": price,
                    "page": page,
                    "description": description,
                })

                print("Sizni ma' lumotlaringiz tasdiqlandi.")
                MENU()
                break
            
def SELECT__BOOKS():
    print("===>>> SELECT__BOOKS bo'limiga xush kelibsiz <<<===")

    num = int(input("Idyingizni kiriting: "))

    for i in BOOKS__CRUD:

        if i['id'] == num:
            
            print(f"=======================================")
            print(f"===> ID: {i['id'] }")
            print(f"===> Title: {i['title']}")
            print(f"===> Another: {i['another']}")
            print(f"===> Langue: {i['langue']}")
            print(f"===> Price: {i['price']}")
            print(f"===> Page: {i['page']}")
            print(f"===> Description: {i['description']}")
            print(f"=======================================\n")

            MENU()
            break

        # else:
        #     print("Siz xato id kiritdingiz.Boshqatdan urinib ko'ring.")

def equal__book (id__update, title, another, langue, price, page, description):
    for i in BOOKS__CRUD:
        if i['id'] == id__update:
            i['title'] = title
            i['another'] = another
            i['langue'] = langue
            i['price'] = price
            i['page'] = page
            i['description'] = description

            print("Sizni ma' lumotlaringiz tasdiqlandi.")
                
            MAIN()

def UPDATE__BOOKS():

    print("===>>> UPDATE__BOOKS bo'limiga xush kelibsiz <<<===")

    id__update = int(input("Siz idyingizni kiriting: "))
 
    while True:
        page = ""
        title = ""
        price = ""
        langue = ""
        another = ""
        description = ""

        check__boolean = {
            "title": False,
            "another": False,             
            "langue": False,
            "price": False,
            "page": False,
            "description": False,
            "check": False,
        }

        title = input("Siz titleyingizni o'zgartirmoqchimisiz? ")
        another = input("Siz anotheringizni o'zgartirmoqchimisiz? ")
        langue = input("Siz langueingizni o'zgartirmoqchimisiz? ")
        price = input("Siz priceingizni o'zgartirmoqchimisiz? ")
        page = input("Siz pageingizni o'zgartirmoqchimisiz? ")
        description = input("Siz descriptioningizni o'zgartirmoqchimisiz? ")

        if len(title) >= 15 and len(title) <= 30: 
            check__boolean['title'] = True
        else: 
            print("Siz titleni ma'lumotlarini to'g'ri kiritmadingiz.")

        if len(another) >= 3 and len(another) <= 20:
            check__boolean["another"] = True

        else:
            print("Siz anotherni ma'lumotlarini to'g'ri kiritmadingiz. ")

        if len(langue) >= 2:
            check__boolean["langue"] = True

        else:
            print("Siz lagueni ma'lumotlarini to'g'ri kiritmagansiz.")

        if len(price) >= 1:
            check__boolean['price'] = True

        else:
            print("Siz priceni ma'lumotini to'g'ri kiritmadingiz.")

        if len(page) <= 5:
            check__boolean["page"] = True

        else:
            print("Siz pageni ma'lumotini to'g'ri kiritmadingiz.")

        if len(description) >= 20 and len(description) <= 50:
            check__boolean["description"] = True

        else:
            print("Siz descriptionni ma'lumotini to'g'ri kiritmadingiz.")

        if check__boolean['title'] and check__boolean['another'] and check__boolean['langue'] and check__boolean['price'] and check__boolean['page'] and check__boolean['description'] :
            equal__book(id__update, title, another, langue, price, page, description)  
    
def DELETE__BOOKS():
    print("===>>> DELETE_BOOKS bo'limiga xush kelibsiz <<<===")

    id__delete = int(input("Idyingizni kiriting: "))

    for i in BOOKS__CRUD:
        if i['id'] == id__delete:
            BOOKS__CRUD.remove(i)
            print("Sizdagi barcha idlar o'chirib yoborildi")

            MENU()
            break

def MENU():
    print("===>>> MENU bo'limiga xush kelibsiz <<<===")
    print("""
        =====================================
        ===     1) All The Books see      ===
        ===     2) Create Books           ===
        ===     3) Select Book            ===
        ===     4) Update Book            ===
        ===     5) Delete Book            ===
        =====================================
    """)

    input__menu__number = int(input("Menudan birini tanlang: "))

    if input__menu__number == 1: ALL__THE__BOOKS__SEE()
    elif input__menu__number == 2: CREATE__BOOKS()
    elif input__menu__number == 3: SELECT__BOOKS()
    elif input__menu__number == 4: UPDATE__BOOKS()
    elif input__menu__number == 5: DELETE__BOOKS() 
    else: print("Menudagi sonlardan birini tanlang: ")

def MAIN():
    MENU()

MAIN()