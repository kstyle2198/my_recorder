import streamlit as st
import speech_recognition as sr
import pandas as pd


def main(언어, is_pushed=False):
    list1 = []
    while True:
        if is_pushed:
            r = sr.Recognizer()
            print("Ready to record")
            with sr.Microphone() as source1:
                try:
                    audio1 = r.listen(source1)
                    print("소리를 글자로 변환중...")
                    # ko-KR    ja-JP    zh(cmn-Hans-CN) en-US
                    text1 = r.recognize_google(audio1, language=언어)
                    return text1
                except:
                    print("뭔소리고????")
        else:
            pass

if __name__ == "__main__":
    
    st.title("음성녹음 테스트")
    언어 = "ko-KR"
    
    if st.button('녹음시작'):
        is_pushed = True
        txt = main(언어, is_pushed)
        st.markdown(txt)
        
    if st.button('녹음종료'):
        st.text("녹음을 종료하겠습니다.")
    
    