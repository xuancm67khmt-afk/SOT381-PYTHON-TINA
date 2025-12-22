n = int(input('Enter the numbers of song: '))
music_list = []
for i in range(1, n+1):
    name = input(f'Name of song {i}=: ')
    music_list.append(name)
    #name = name.upper()
print('My music list: ',music_list)
#Add the word love
print('Name of song have the word love')
for i in range(n):
    name = music_list[i]
    if name.find('love') != -1:
       print('Song{i}; {name}')
#The name song longest and corresponding number
the_name_song_longest = music_list[0]
the_number_of_words_in_the_longest_song = len (the_name_song_longest.split())
address_of_song = 0
#Iterate through the elements of a list
for i in range(n):
    name_song = music_list[i]
    number_of_word = len (name_song.split())
    if number_of_word>the_number_of_words_in_the_longest_song:
        address_of_song = i
        the_name_song_longest = name
        the_number_of_words_in_the_longest_song = number_of_word
print(f'Name: {the_name_song_longest}in {address_of_song} have {the_number_of_words_in_the_longest_song} words')