def solution(m, musicinfos):
    sharp,r = ["C#","D#","F#","G#","A#"], ["c","d","f","g","a"]
    for x,y in zip(sharp,r):
        m = m.replace(x,y)
    answer = ["",0]
    for i in musicinfos:
        s,e,name,melody = i.split(',')
        for x,y in zip(sharp,r):
            melody = melody.replace(x,y)
        playtime = (60*int(e[:2])+int(e[-2:])) - (60*int(s[:2])+int(s[-2:]))
        play = (playtime//len(melody))*melody + melody[:playtime%len(melody)]
        if m in play and answer[-1]<playtime:
            answer = [name,playtime]
    return answer[0] if answer[0] else "(None)"