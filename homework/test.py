# # """
# # As you can see, the code is broken.
# # Create the missing functions, use default arguments.
# # Sometimes you have to use 'return' and sometimes you dont.
# # Start by creating the functions
# # """

# # # \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

# # days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


# # def is_on_list(target_list, target):
# #     return target in target_list


# # def get_x(target_list, target):
# #     return target_list[target]


# # def add_x(target_list, target):
# #     return target_list.append(target)


# # def remove_x(target_list, target):
# #     if target in target_list:
# #         return target_list.remove(target)


# # print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

# # print("The fourth item in 'days' is:", get_x(days, 3))

# # add_x(days, "Sat")
# # print(days)

# # remove_x(days, "Mon")
# # print(days)


# # # /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #


# """
# Again, the code is broken, you need to create 4 functions.
#   - add_to_dict: Add a word to a dict.
#   - get_from_dict: Get a word from inside a dict.
#   - update_word: Update a word inside of the dict.
#   - delete_from_dict: Delete a word from the dict.

# All this functions should check for errors, follow the comments to see all cases you need to cover.

# There should be NO ERRORS from Python in the console.
# """


# import os


# def add_to_dict(target_dict=None, target_key=None, target_value=None):
#     if type(target_dict) != dict:
#         print(f"You need to send a dictionary. You sent:{type(target_dict)}")
#         # print("You need to send a dictionary. You sent:{}".format(type(target_dict)))
#         return
#     if target_value == None:
#         target_dict[target_key] = target_value
#         print("You need to send a word and a definition")
#         return
#     if target_dict[target_key] == None:
#         target_dict[target_key] = target_value
#         print(f"{target_key} has been added")
#         return
#     else:
#         print(f"{target_key} is already on the dictionary. Won't add")
#         return
#     return


# def get_from_dict(target_dict=None, target_key=None):
#     if type(target_dict) != dict:
#         print(f"You need to send a dictionary. You sent:{type(target_dict)}")
#         return
#     if target_key == None:
#         print("You need to send a word to search for.")
#         return
#     else:
#         if target_key in target_dict:
#             print(f"{target_key}: {target_dict[target_key]}")
#             return
#         else:
#             print(f"{target_key} was not found in this dict")
#             return
#     return


# def update_word(target_dict=None, target_key=None, target_value=None):
#     if type(target_dict) != dict:
#         print(f"You need to send a dictionary. You sent:{type(target_dict)}")
#         return
#     if target_value == None:
#         print("You need to send a word and a definition to update.")
#         return
#     if target_key not in target_dict:
#         print(f"{target_key} is not on the dict. Can't update non-existing word.")
#         return
#     elif target_value != None:
#         target_dict[target_key] = target_value
#         print(f"{target_key} has been updated to: {target_value}")
#         return
#     return


# def delete_from_dict(target_dict=None, target_key=None):
#     if type(target_dict) != dict:
#         print(f"You need to send a dictionary. You sent:{type(target_dict)}")
#         return
#     if target_key == None:
#         print("You need to specify a word to delete")
#         return
#     if target_key not in target_dict:
#         print(f"{target_key} is not in this dict. Won't delete")
#     else:
#         del(target_dict[target_key])
#         print(f"{target_key} has been deleted")
#         return
#     return

#     # \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\


# os.system('clear')


# my_english_dict = {}

# print("\n###### add_to_dict ######\n")

# # Should not work. First argument should be a dict.
# print('add_to_dict("hello", "kimchi"):')
# add_to_dict("hello", "kimchi")

# # Should not work. Definition is required.
# print('\nadd_to_dict(my_english_dict, "kimchi"):')
# add_to_dict(my_english_dict, "kimchi")

# # Should work.
# print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
# add_to_dict(my_english_dict, "kimchi", "The source of life.")

# # Should not work. kimchi is already on the dict
# print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
# add_to_dict(my_english_dict, "kimchi", "My fav. food")


# print("\n\n###### get_from_dict ######\n")

# # Should not work. First argument should be a dict.
# print('\nget_from_dict("hello", "kimchi"):')
# get_from_dict("hello", "kimchi")

# # Should not work. Word to search from is required.
# print('\nget_from_dict(my_english_dict):')
# get_from_dict(my_english_dict)

# # Should not work. Word is not found.
# print('\nget_from_dict(my_english_dict, "galbi"):')
# get_from_dict(my_english_dict, "galbi")

# # Should work and print the definiton of 'kimchi'
# print('\nget_from_dict(my_english_dict, "kimchi"):')
# get_from_dict(my_english_dict, "kimchi")

# print("\n\n###### update_word ######\n")

# # Should not work. First argument should be a dict.
# print('\nupdate_word("hello", "kimchi"):')
# update_word("hello", "kimchi")

# # Should not work. Word and definiton are required.
# print('\nupdate_word(my_english_dict, "kimchi"):')
# update_word(my_english_dict, "kimchi")

# # Should not work. Word not found.
# print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
# update_word(my_english_dict, "galbi", "Love it.")

# # Should work.
# print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
# update_word(my_english_dict, "kimchi", "Food from the gods.")

# # Check the new value.
# print('\nget_from_dict(my_english_dict, "kimchi"):')
# get_from_dict(my_english_dict, "kimchi")


# print("\n\n###### delete_from_dict ######\n")

# # Should not work. First argument should be a dict.
# print('\ndelete_from_dict("hello", "kimchi"):')
# delete_from_dict("hello", "kimchi")

# # Should not work. Word to delete is required.
# print('\ndelete_from_dict(my_english_dict):')
# delete_from_dict(my_english_dict)

# # Should not work. Word not found.
# print('\ndelete_from_dict(my_english_dict, "galbi"):')
# delete_from_dict(my_english_dict, "galbi")

# # Should work.
# print('\ndelete_from_dict(my_english_dict, "kimchi"):')
# delete_from_dict(my_english_dict, "kimchi")

# # Check that it does not exist
# print('\nget_from_dict(my_english_dict, "kimchi"):')
# get_from_dict(my_english_dict, "kimchi")

# # \/\/\/\/\/\/\ END DO NOT TOUCH  \/\/\/\/\/\/\


# open 파일 열어줌 없으면 생성됨
# file = open("jogs.csv", mode="w")


def save_to_file():
    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    return
