import requests
import os
import openai
import speech_recognition 
import pyttsx3

openai.api_key = os.getenv("JiaKey")
recognizer = speech_recognition.Recognizer()

# Makes request to Openai to generate prompt
def tell_story(prompt):
  try:
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    text = response.choices[0].text
    return text
    
  except Exception:
    print("Error generating story.")
    
# Makes request to Openai to generate art given prompt    
def create_pictures(prompt):
  try:
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="256x256"
    )
    image_url = response['data'][0]['url']
    return image_url
    
# Detect input from mic
"""
# Detect input from mic
with speech_recognition as mic:
  print("Speech dectection is now on.")
  audio = recognizer.listen(mic)
  try:
    # input successful 
    speech_text = recognizer.recognize_google(audio)
    print(speech_text)
  except speech_recognition.UnknownValueError:
    print("Could not understand.")
  except speech_recognition.RequestError:
    print("Request error from Google.")
  
"""
prompt = input("What kind of story would you like to hear?")
print(prompt)
story = tell_story(prompt)
print(story)
sentences = story.split(".")
for sentence in sentences:
  create_pictures(sentence)
