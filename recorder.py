import speech_recognition as sr
import keyboard
import pandas as pd

list1 = []

while True:
    print("ready to press P")
    if keyboard.read_key() == "p":
        print("pressed P")
        r = sr.Recognizer()
        print("ready to record")
        with sr.Microphone() as source1:
            audio1 = r.listen(source1)
            print("소리를 글자로 변환중...")
            text1 = r.recognize_google(audio1, language="ko-KR")

            print("-"*20)
            print(text1)
            print("="*20)

            list1.append(text1)
            df = pd.DataFrame(list1)
            df.to_csv(
                "C:/my_develop2/meeting_record/records/meetings.csv",
                header=False,
                index=False,
                encoding="euc-kr'",
            )
            print("부분 녹음 종료")
    else:
        pass
