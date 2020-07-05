def make_album(artist,title,song_nums = None):
    info={'artist':artist,'title':title}
    if song_nums:
        info['number_of_songs']=song_nums
    return info

print(make_album('Jay Chou','QiLixiang'))
print(make_album('Justin Biber','Baby',10))

while True:
    art = input("Please Enter an artist's name.Or q to quit.\t")
    if art == 'q':
        break
    title = input("Please enter the album's title.And q to quit.\t")
    if title == 'q':
        break
    print(make_album(art,title))