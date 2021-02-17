# 딕셔너리 함수 제대로 익히기
# 딕셔너리 활용 연습해보기


def solution(genres, plays):
    answer = []
    playsDict = {}  # { 장르 : 총 재생 횟수 } 사전
    d = {}  # { 장르 : [ ( 플레이 횟수, 고유 번호 ) ] }

    for i in range(len(genres)):
        playsDict[genres[i]] = playsDict.get(genres[i], 0) + plays[i]
        d[genres[i]] = d.get(genres[i], []) + [ (plays[i], i) ]

    genreSort = sorted(playsDict.items(), key=lambda x: x[1], reverse=True)

    for (genre, totalPlay) in genreSort:
        d[genre] = sorted(d[genre], key=lambda x: -x[0])
        answer += [ idx for (play, idx) in d[genre][:2] ]

    return answer
