import streamlit as st
from gtts import gTTS
import io
text = "Namasthe, Mera naam Raja, Log mujhe kehte hai Rockey Bhai"
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
  <a href = "https://github.com/rajatelagathoti/Hapsa/blob/main/Telugu%20Quran.pdf">Click here</a>
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
