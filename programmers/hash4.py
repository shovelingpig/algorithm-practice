# 나의 풀이
from operator import itemgetter

def solution(genres, plays):
    answer = []
    my_dict = {}
    for i in range(0, len(genres)) :
        if genres[i] not in my_dict :
            my_dict[genres[i]] = []
            my_dict[genres[i]].append(0);
        my_dict[genres[i]].append( (i, plays[i]) );
        my_dict[genres[i]][0] += plays[i];

    print(my_dict)
    a = list(my_dict.values())
    a.sort(key=itemgetter(0), reverse=True)
    print(a)

    while a :
        max = -1
        a[0].pop(0)
        a[0].sort(key=itemgetter(1), reverse=True)
        for i in range(0, len(a[0])) :
            if (i >= 2) :
                break
            answer.append(a[0][i][0]) 
        a.pop(0)
    return answer
    
    
# 다른 풀이 1
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer

"""
# 한줄평
- list comprehension으로 dictionary도 간편히 만들 수 있다는 것을 알게 되었다. 또한 sorted 함수의 key로 전달되는 lambda 함수에서 tuple을 return하면 앞에 위치한 순서대로 정렬이 된다는 것을 알게 되었다.
"""

    
# 다른 풀이 2
def solution(genres, plays):
    answer = []
    dic = {}
    album_list = []
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))

    dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
    album_list = sorted(album_list, reverse=True)

    while len(dic) > 0:
        play_genre = dic.pop(0)
        print(play_genre)
        cnt = 0;
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer

class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        return self.play < other.play
    def __le__(self, other):
        return self.play <= other.play
    def __gt__(self, other):
        return self.play > other.play
    def __ge__(self, other):
        return self.play >= other.play
    def __eq__(self, other):
        return self.play == other.play
    def __ne__(self, other):
        return self.play != other.play

"""
# 한줄평
- Pythion에서도 class를 선언하여 활용하면 가독성이 높게 구현할 수 있다는 사실을 깨달았다.
"""
