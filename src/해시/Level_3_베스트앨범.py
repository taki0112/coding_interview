from collections import defaultdict

def sort_by_value(x) :
    sort_x = {}
    for key, value in sorted(x.items(), key=lambda x : x[1], reverse=True) :
        sort_x[key] = value

    return sort_x

def solution(genres, plays):
    answer = []
    total_num = len(genres)
    genres_dict = defaultdict(int)
    genres_index_dict = {}

    for i in range(total_num) :
        genres_dict[genres[i]] += plays[i]
        genres_index_dict[genres[i] + '_' + str(i)] = plays[i]

    genres_dict = sort_by_value(genres_dict)
    genres_index_dict = sort_by_value(genres_index_dict)

    for k in genres_dict.keys() :
        limit_song = 0
        for key, value in genres_index_dict.items() :
            if k in key :
                answer.append(int(key.split('_')[-1]))
                limit_song += 1
            if limit_song >= 2 :
                break

    return answer

genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]

x = solution(genres, plays)
print(x)