my_fav_numbers = {7, 3, 9, 5, 1}
friend_fav_numbers = {2, 4, 6, 8, 10}

my_fav_numbers.add(11)
my_fav_numbers.add(13)

my_fav_numbers.remove(13)

print("last element in my_fav_numbers removed: ", my_fav_numbers)

our_fav_numbers = my_fav_numbers | friend_fav_numbers

print("our_fav_numbers: ", our_fav_numbers)