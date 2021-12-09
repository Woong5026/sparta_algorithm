sharp = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a'}


# 시간을 고쳐주는 함수> 시간을 분단위로
def timeTomin(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)


def LowerSharp(m):
    for s in sharp.keys():
        m = m.replace(s, sharp[s])
        # 실행된 분 수 만큼만 자르기
    return m


def musicfullstream(mel, duration):
    mel = LowerSharp(mel)
    # 기간에 길이를 나눠주며 몇 번 재생되었는지 확인
    mel = mel * (duration // len(mel) + 1)
    return mel[:duration]


def solution(m, musicinfos):
    m = LowerSharp(m)
    print(m)
    play_title = []
    play_duration = []
    # 재생시간, 음이 중간에 끊겼는지
    # 실제 플레이를 해보고 플레이를 한 것과 매칭을 시킨다
    for music in musicinfos:
        start, end, title, mel = music.split(',')
        duration = timeTomin(end) - timeTomin(start)

        # 음이 내부에 있는지
        # 재생한 것 만큼의 플레이가 필요
        mel = musicfullstream(mel, duration)
        # m이 mel 안에 있다면 음이 재생된 걸로 확인, 중복된 케이스를 위해 리스트를 하나 만들어야 함
        if m in mel:
            play_title.append(title)
            play_duration.append(duration)

    return play_title[play_duration.index(max(play_duration))]