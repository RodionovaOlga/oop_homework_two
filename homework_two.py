cook_book = {}
with open (r"C:\Users\Ольга\OneDrive\Рабочий стол\homework_two\dishes.txt", "r", encoding="utf-8") as f:
    while True:
        key_1 = f.readline().strip()
        v_ingr = f.readline().strip()
        if v_ingr == "":
          break
        counter = int(v_ingr)
        for i in range (0, counter):
            f_str = f.readline().strip().split(" | ")
            #print (f_str)
            value = {}
            value['ingredient_name'] = f_str[0]
            value['quantity'] = f_str[1]
            value['measure'] = f_str[2]
            if key_1 in cook_book:
                cook_book[key_1].append(value)
            else:
                cook_book[key_1] = [value]
        f.readline()
        
print(cook_book)