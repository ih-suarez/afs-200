csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'

# Removing Symbols That Are Not Commas
friends_list = csv.replace(':', ',')
new_friends_list = friends_list.replace(';', ',')

# Spliting String W/ Commas
final_friends = new_friends_list.split(',')
print(final_friends)