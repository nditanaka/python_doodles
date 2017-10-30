first_name="Tanaka"
last_name="Chingonzo"
full_name= first_name +" "+ last_name

print("\nMy \nname \nis" + " \n" + full_name.title())
print("\n\tMy \n\tname \n\tis" + " \n\t" + full_name.title())

#\t adds a whitespace in the form of a tab
#\n adds a whitespace in the form of a new line
#\n\t inserts both a new line and a tab at its beginning

#whitespace can alter the outputs of variables like usernames where whitespace is crucial

favorite_language= " Python "
print(favorite_language)
favorite_language_r = favorite_language.rstrip()
favorite_language_l = favorite_language.lstrip()
favorite_language_both = favorite_language.strip()


print(favorite_language_r)
print(favorite_language_l)
print(favorite_language_both)
print(favorite_language)

#rstrip() removes whitespace from the right
#lstrip() removes whitespace from the left
#strip() removes whitespace on both sides of the string


