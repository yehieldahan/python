'''Create 2 variables : string of your full name, another string of your mail.
Create variable of your age (integer)
print all of them to the screen

then Print your name from the end to the beginning and print it only with your age*3

then check if your name is stored inside this full string:
"idan ben dudu yuval shimon yael gal adam shahar yana"
'''
name="yehiel dahan"
age=28
mail="dc02dc03@gmail.com"
print("Full name: " + name + "\nage: " + str(age) + "\nmail: " + mail)
print("\n\nFull name: " + name[::-1] + "\nage: " + str(age*2))
print("yehiel" in "yehiel ben dudu yuval shimon yael gal adam shahar yana")
