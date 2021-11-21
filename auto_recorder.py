import speech_recognition as sr
import keyboard
import pandas as pd

# ko-KR    ja-JP    zh   en-US

사용언어 = "ko-KR"
저장파일명 = "meeting_auto1.csv"

list1 = []

while True:
    r = sr.Recognizer()
    print("Ready to record")
    with sr.Microphone() as source1:
        try:
            audio1 = r.listen(source1)
            print("소리를 글자로 변환중...")
            text1 = r.recognize_google(audio1, language=사용언어)

            print("-"*20)
            print(text1)
            print("="*20)

            list1.append(text1)
            df = pd.DataFrame(list1)
            df.to_csv(
                "C:/my_develop2/meeting_record/records/{}".format(저장파일명),
                header=False,
                index=False,
                encoding="euc-kr'",
            )
            print("부분 녹음 종료")
        except:
            print("뭔소리고????")


# git push -u origin main
