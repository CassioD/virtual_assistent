# instalar as bibliotecas gTTS e pydub
# !pip install gTTS pydub
# Baixe o FFmpeg do site oficial: https://ffmpeg.org/download.html

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Texto em inglês
text_to_say = "How are you doing?"

language = "en"

gtts_object = gTTS(text=text_to_say,
                   lang=language,
                   slow=False)

gtts_object.save("gtts.mp3")  # Salvando no diretório do projeto como MP3

# Convertendo para WAV
audio = AudioSegment.from_mp3("gtts.mp3")
audio.export("gtts.wav", format="wav")

# Reproduzindo o áudio
play(audio)

# Texto em francês
french_text = "Je vais au supermarché"

french_language = "fr"

french_gtts_object = gTTS(text=french_text,
                          lang=french_language,
                          slow=True)

french_gtts_object.save("french.mp3")  # Salvando no diretório do projeto como MP3

# Convertendo para WAV
french_audio = AudioSegment.from_mp3("french.mp3")
french_audio.export("french.wav", format="wav")

# Reproduzindo o áudio em francês
play(french_audio)
