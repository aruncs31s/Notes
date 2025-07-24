---
aliases: 
Date: "17-05-2025"
---
# 05 HUman Interaction


## 
[Mac File Link](file:///Users/aruncs/Documents/AmritaOjectRecgRobot.pdf) [Paper Link](https://www.researchgate.net/publication/251892709_Object_recognition_and_obstacle_avoidance_robot) 
. Obstacle detection, pattern recognition and
obstacle avoidance

## Voice Assistant
### Home Assistant

```bash
 docker run -it -p 10200:10200 -v /home/aruncs/docker/data:/data rhasspy/wyoming-piper \
    --voice en_US-lessac-medium

docker run -it -p 10300:10300 -v /home/aruncs/docker/data:/data rhasspy/wyoming-whisper \
    --model tiny-int8 --language en

```
```
http://homeassistant.local:8123/
```

- [[Frigate]]
### Pyttsx3

```python

 engine = pyttsx3.init() 
 engine.setProperty('rate', 160)
 voices = engine.getProperty('voices')
 if voices:
     engine.setProperty('voice', voices[0].id)
```


#### Open Browser 

```python
def open_google(query):
    url = f"https://www.google.com/search?q={query}"
    speak(f"Searching Google for {query}")
    webbrowser.open(url)

def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

```
#### Play Music
```python

def play_music():
    music_folder = r"C:\Users\ABHAYA\apci\shaky"
    if not os.path.exists(music_folder):
        speak("Music folder not found.")
        return

    songs = [file for file in os.listdir(music_folder) if file.endswith(('.mp3', '.wav'))]
    if not songs:
        speak("No music files found in the folder.")
        return

    song_to_play = random.choice(songs)
    song_path = os.path.join(music_folder, song_to_play)
    speak(f"Playing {song_to_play}.")

    try:
        # Initialize mixer
        pygame.mixer.init()
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play(loops=0)  # Ensure it plays only once

        # Wait until either song finishes or 30 seconds pass
        start_time = time.time()
        while pygame.mixer.music.get_busy():
            if time.time() - start_time > 30:
                break
            time.sleep(1)

        # Force stop after 30 seconds or when done
        pygame.mixer.music.stop()
        pygame.mixer.quit()  # Important: release the audio device
    except Exception as e:
        speak(f"Failed to play music due to error: {e}")

```

#### Removed
```python
    # elif "time" in query:
    #     tell_time()
    # elif "wikipedia" in query:
    #     topic = query.replace("wikipedia", "").strip()
    #     if topic:
    #         search_wikipedia(topic)
    #     else:
    #         speak("What should I search on Wikipedia?")
    # elif "google" in query:
    #     topic = query.replace("google", "").strip()
    #     if topic:
    #         open_google(topic)
    #     else:
    #         speak("What should I search on Google?")
    # elif "youtube" in query:
    #     open_youtube()
    # elif "music" in query or "song" in query:
    #     play_music()
    # elif "weather" in query:
    #     speak("Checking the weather...")
    #     response = ask_ollama("What's the weather like today?")
    #     speak(response)
    # elif any(word in query for word in ["exit", "quit", "stop", "goodbye", "bye"]):
    #     speak("Goodbye! Have a great day.")
    #     exit()
```