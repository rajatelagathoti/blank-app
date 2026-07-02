import streamlit as st
from gtts import gTTS
import io
text = "అల్లాహ్ హు అక్బర్"
st.markdown("""
<!DOCTYPE html>
<html>
<head>
  <title>Raja Telagathoti</title>
</head>
<body>
  <h1>
    Raja Telagathoti
  </h1>
  <h6>Click the button below to download Qur'an</h6>
  <a href="https://raw.githubusercontent.com/rajatelagathoti/Hapsa/main/Telugu%20Quran.pdf" target="_blank">
Click here to download Telugu Qur'an
</a>
  <h6>Click the button below to listen to the Qur'an</h6>
  </body>
</html>
""", unsafe_allow_html=True)
if st.button("Play Telugu Speech"):
    tts = gTTS(text=text, lang="te", slow=False)

    audio = io.BytesIO()
    tts.write_to_fp(audio)
    audio.seek(0)

    st.audio(audio, format="audio/mp3")
