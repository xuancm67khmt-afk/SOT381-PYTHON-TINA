n = int(input('Enter the numbers of song: '))
music_list = []
for i in range(1, n+1):
    name = input('Name of song: ')
    music_list.append(name)
print('My music list: ',music_list)