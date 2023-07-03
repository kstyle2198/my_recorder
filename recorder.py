import speech_recognition as sr
import keyboard
import pandas as pd

list1 = []

while True:
    print("Please press P")
    if keyboard.read_key() == "p":
        print("You have pressed P")
        r = sr.Recognizer()
        print("Ready to record")
        with sr.Microphone() as source1:
            try:
                audio1 = r.listen(source1)
                print("소리를 글자로 변환중...")
                # ko-KR    ja-JP    zh(cmn-Hans-CN) en-US
                text1 = r.recognize_google(audio1, language="ko-KR")
                print("-"*20)
                print(text1)
                print("="*20)

                list1.append(text1)
                df = pd.DataFrame(list1)
                df.to_csv(
                    "C:/my_develop2/meeting_record/records/meetings_0703(수동).csv",
                    header=False,
                    index=False,
                    encoding="euc-kr'",
                )
                print("부분 녹음 종료")
            except:
                print("뭔소리고????")
    else:
        pass


# git push -u origin main
