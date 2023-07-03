import speech_recognition as sr
import keyboard
import pandas as pd

# 사용할 언어와 저장할 파일명을 정해주세요.     한국어 ko-KR    일본어 ja-JP    중국어(북경어) zh   영어   en-US

사용언어 = "ko-KR"
저장파일명 = "meeting(자동).csv"
list1 = []

while True:
    r = sr.Recognizer()
    print("Ready to record")
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            print("소리를 글자로 변환중...")
            text = r.recognize_google(audio, language=사용언어)

            print("-"*20)
            print(text)
            print("="*20)

            list1.append(text)
            df = pd.DataFrame(list1)
            df.to_csv(
                "C:/my_develop2/meeting_record/records/{}".format(저장파일명),
                header=False,
                index=False,
                encoding="euc-kr",
            )
            print("부분 녹음 종료")
        except:
            print("뭔소리고????")


