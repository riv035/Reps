with open(file="cook_book.txt", mode="r", encoding="UTF-8") as cook_txt:
    cook_book = {}
    for meal in cook_txt.read().split("\n\n"):
        dish = meal.splitlines()[0]
        ing_list = []
        for recieps in meal.splitlines()[2:]:
            reciepe = recieps.split(" | ")
            ingredients = {"ingredient_name": reciepe[0], "quantity": int(reciepe[1]), "measure": reciepe[2]}
            ing_list.append(ingredients)
        cook_dict = {dish: ing_list}
        cook_book.update(cook_dict)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for meals in dishes:
        for ingredient in cook_book[meals]:
            shop_list_item = dict(ingredient)
            shop_list_item["quantity"] *= person_count
            if shop_list_item["ingredient_name"] not in shop_list:
                shop_list[shop_list_item["ingredient_name"]] = shop_list_item
            else:
                shop_list[shop_list_item["ingredient_name"]]["quantity"] += shop_list_item["quantity"]
            del shop_list_item["ingredient_name"]
    print(shop_list)


get_shop_list_by_dishes(["Омлет", "Фахитос"], 2)

get_shop_list_by_dishes(["Утка по-пекински"], 6)

print(cook_book)
