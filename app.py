import streamlit as st
import speech_recognition as sr
import pandas as pd
from streamlit_webrtc import webrtc_streamer
import av
import cv2

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
        
def callback(frame):
    img = frame.to_ndarray(format="bgr24")

    img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)

    # return av.VideoFrame.from_ndarray(img, format="bgr24")

if __name__ == "__main__":
    
    
    
    st.title("음성녹음 테스트")
    언어 = st.selectbox("언어선택", options=["ko-KR", "en-US", "ja-JP", "zh(cmn-Hans-CN)"])
    
    # webrtc_streamer(key="speech-to-text")
    
    
    webrtc_streamer(
         key="speech-to-text",
        video_frame_callback=callback,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
        )
    
    if st.button('녹음시작'):
        is_pushed = True
        txt = main(언어, is_pushed)
        st.markdown(txt)
        
    if st.button('녹음종료'):
        st.text("녹음을 종료하겠습니다.")
    
    