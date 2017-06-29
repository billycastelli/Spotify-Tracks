#spotify api

#compare the populatiry of two inputted tracks

#first get the id from

import spotify_builder
from operator import itemgetter


def compare_count():
    count = int(input("How many songs do you want to compare: "))
    return count


def get_info()->[[]]:
    print()
    artist = str(input("Artist name: "))
    track = str(input("Track name: "))

    return (artist, track)



if __name__ == "__main__":
    count = compare_count()
    pop_list = []
    for x in range(count):
        info = get_info()
        
        search_url = spotify_builder.build_search_url(info)
        search_json = spotify_builder.get_json(search_url)
        track_id = spotify_builder.get_id(search_json)

        track_url = spotify_builder.build_track_url(track_id)
        track_json = spotify_builder.get_json(track_url)
        popularity = spotify_builder.get_popularity(track_json)

        pop_list.append((popularity, info[0], info[1]))

    pop_list = sorted(pop_list, key = itemgetter(0), reverse = True)

    for info in pop_list:
        print()
        for att in info:
            print(att)
        
        
        

        

        
                


