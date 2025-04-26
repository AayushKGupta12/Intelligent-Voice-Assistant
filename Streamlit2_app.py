import streamlit as st
import speech_recognition as sr
import os
import platform
import webbrowser
import datetime

from exceptiongroup import catch
from openai.cli import Image

from config import apikey
from mistralai import Mistral


import streamlit.components.v1 as components


# Button to trigger the loader
def show_skeleton_loader():
    components.html("""
        <!DOCTYPE html>
        <html>
            <head>
                <script src="https://cdn.tailwindcss.com"></script>
            </head>
                <body>
                    <div role="status" class="space-y-2.5 animate-pulse max-w-lg p-4">
                        <div class="flex items-center w-full">
                            <div class="h-2.5 bg-yellow-100 rounded-full w-132"></div>
                            <div class="h-2.5 ms-2 bg-gray-300 rounded-full w-124"></div>
                            <div class="h-2.5 ms-2 bg-emerald-300 rounded-full w-full"></div>
                            <div class="h-2.5 ms-2 bg-pink-200 rounded-full w-full"></div>
                            <div class="h-2.5 ms-2 bg-emerald-300 rounded-full w-full"></div>
                        </div>
                        <div class="flex items-center w-full max-w-[480px]">
                            <div class="h-2.5 bg-gray-200 rounded-full w-full"></div>
                            <div class="h-2.5 ms-2 bg-pink-200 rounded-full w-full"></div>
                            <div class="h-2.5 ms-2 bg-gray-300 rounded-full w-124"></div>
                            <div class="h-2.5 ms-2 bg-emerald-300 rounded-full w-full"></div>
                            <div class="h-2.5 ms-2 bg-gray-300 rounded-full w-124"></div>
                        </div>
                        <div class="flex items-center w-full max-w-[400px]">
                            <div class="h-2.5 bg-cyan-600 rounded-full w-full"></div>
                            <div class="h-2.5 ms-2 bg-fuchsia-300 rounded-full w-180"></div>
                            <div class="h-2.5 ms-2 bg-emerald-300 rounded-full w-160"></div>
                            <div class="h-2.5 ms-2 bg-gray-300 rounded-full w-full"></div>
                            <div class="h-2.5 ms-2 bg-gray-200 rounded-full w-full"></div>
                        </div>
                        <div class="flex items-center w-full max-w-[480px]">
                            <div class="h-2.5 ms-2 bg-gray-200 rounded-full w-full"></div>
                            <div class="h-2.5 ms-2 bg-orange-300 rounded-full w-full"></div>
                            <div class="h-2.5 ms-2 bg-gray-300 rounded-full w-124"></div>
                            <div class="h-2.5 ms-2 bg-emerald-300 rounded-full w-190"></div>
                            <div class="h-2.5 bg-cyan-600 rounded-full w-full"></div>
                        </div>
                        <div class="flex items-center w-full max-w-[440px]">
                            <div class="h-2.5 ms-2 bg-gray-200 rounded-full w-132"></div>
                            <div class="h-2.5 ms-2 bg-blue-500 rounded-full w-124"></div>
                            <div class="h-2.5 ms-2 bg-emerald-300 rounded-full w-full"></div>
                             <div class="h-2.5 ms-2 bg-gray-300 rounded-full w-124"></div>
                            <div class="h-2.5 ms-2 bg-gray-200 rounded-full w-full"></div>
                        </div>
                        <div class="flex items-center w-full max-w-[360px]">
                            <div class="h-2.5 ms-2 bg-purple-300 rounded-full w-full"></div>
                            <div class="h-2.5 ms-2 bg-gray-300 rounded-full w-124"></div>
                            <div class="h-2.5 ms-2 bg-emerald-300 rounded-full w-full"></div>
                             <div class="h-2.5 ms-2 bg-gray-300 rounded-full w-124"></div>
                            <div class="h-2.5 ms-2 bg-gray-200 rounded-full w-180"></div>
                            <div class="h-2.5 ms-2 bg-teal-300 rounded-full w-full"></div>
                        </div>
                        <div class="flex items-center w-full max-w-[360px]">
                            <div class="h-2.5 ms-2 bg-gray-300 rounded-full w-124"></div>
                            <div class="h-2.5 ms-2 bg-emerald-300 rounded-full w-full"></div>
                            <div class="h-2.5 ms-2 bg-blue-500 rounded-full w-124"></div>
                             <div class="h-2.5 ms-2 bg-gray-300 rounded-full w-full"></div>
                            <div class="h-2.5 ms-2 bg-gray-200 rounded-full w-80"></div>
                             <div class="h-2.5 ms-2 bg-gray-300 rounded-full w-124"></div>
                        </div>
                        <span class="sr-only">Loading...</span>
                    </div>
                </body>
        </html>
        """, height=300, scrolling=False)


st.markdown("""
    <div style='
        font-size: 28px;
        color: #2E86C1;
        font-family: Arial;
        font-weight: bold;
        text-align:left;
    '>
        👋 Hey! Am your Personal Assistant
        <br>
    </div>
    """, unsafe_allow_html=True
    )

st.sidebar.write("I'm your personal coding assistant, ready to help you with coding, debugging, and more. I can also assist in crafting emails, letters, applications, notices, and beyond. I hope you enjoy working with me!" )

with st.sidebar.expander("💡 How to Use This Assistant 💡"):
    st.write("""
        1. 🚀 Launch the application.  
        2. 🔘 Click on the button to activate your personal assistant.  
        3. 🗣️ Speak your query.  
        4. 🤖 Your personal assistant will respond to you.  
        5. ✅ Once you've completed your query,  
        6. 🙏 Say "Thank you" to end your session.  
        Ready to make your experience smoother and more fun! 🎉
    """)

with st.sidebar.expander("✨ About the Developer ✨"):
    image = "Coding_Ass/CodingAsistant.jpg"
    st.image(image, caption="Aayush K. Gupta", use_container_width=True)
    st.write("""
        **Name:** Aayush Kumar Gupta  
        **From:** Patna, Bihar 🌏  
        **Currently Studying At:** Kalinga Institute of Industrial Technology, Odisha🎓  
        **Graduation Year:** 2027 🎉  
        **Interests:**  
        - 🌟 Machine Learning  
        - 🤖 Deep Learning  
        - 📊 Data Science  
        - 📈 Data Analytics  
        - 💻 Full Stack Web Development  
        🧑‍💻 Passionate about crafting innovative solutions and exploring cutting-edge technology! 🚀
    """)


def ai(query):
    api_key = apikey
    model = "mistral-large-latest"
    client = Mistral(api_key=api_key)

    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": query,
            },
        ]
    )

    response = chat_response.choices[0].message.content

    st.markdown(
        f"""
        <div style='
            background-color: #e8f8f5;
            border-radius: 15px;
            border-color: white;
            padding: 15px;
            color: black;
        '>
            🤖 <b>Assistant:</b><br>{response}
        </div>
        """,
        unsafe_allow_html=True
    )


def say(text):
    if platform.system() == "Windows":
        # Replace single quotes with double quotes to avoid PowerShell issues
        text = text.replace("'", '"')

        # Execute PowerShell TTS command once
        os.system(
            f'powershell -c "Add-Type –AssemblyName System.speech; '
            f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
            f'$speak.Speak(\\"{text}\\");"'
        )


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        st.write("🎤 Listening...")

        try:
            audio = r.listen(source, timeout=30, phrase_time_limit=30)
            query = r.recognize_google(audio, language="en-in")

            left, right = st.columns([1, 1])
            with left:
                st.markdown(
                    f"""
                    <div style='
                        background-color: #eaf2f8;
                        padding: 7px 7px 7px 7px;
                        border-radius: 15px;
                        max-width: 700px;
                        color: black;
                        margin-bottom: 7px;
                    '>
                        👤 <b>You:</b><br>{query}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            return query.lower()
        except Exception:
            return ""


if __name__ == '__main__':

    if st.button("Start"):

        st.success("System started successfully.")
        st.write("Initializing the system...")
        say("Initializing the system...")
        st.write("I am now ready to take your commands.")
        say("I am now ready to take your commands.")

        while True:
            text = takeCommand()

            executed = False

            sites = [["youtube","https://www.youtube.com/"],["wikipedia","https://www.wikipedia.org"],["google","https://www.google.com"]]
            for site in sites:
                if text and f"open {site[0]}".lower() in text.lower():
                    say(f"Opening {site[0]}")
                    webbrowser.open(site[1])
                break
                executed = True


            try:
                if any(phrase.lower() in text for phrase in ["Hello", "Hi", "Whatsapp","How are you","help"]):
                    st.write("I'm your coding assistant, here to help you code and chat about anything you need!")
                    say("Hi! I'm your coding assistant, here to help you code and chat about anything you need!")

                    executed = True

            except Exception as e:
                pass

            try:
                if any(phrase in text for phrase in ["explain me", "what is", "where is", "how to"]):
                    st.write("coming back with your result, just 1 second")
                    query = text +"Explain this as simply and short as possible, do add EMOJIS wherever it is possible"

                    placeholder = st.empty()
                    with placeholder.container():
                        show_skeleton_loader()

                    response_text = ai(query)
                    placeholder.empty()

                    executed = True

                elif any(phrase in text for phrase in ["Contrast", "Evaluate", "Examine", "Analyze", "Match","compare"]):
                    say("just 1 second, Let me look for it in my Database")
                    st.write("just 1 second, Let me look for it in my Database")
                    query = text +"Explain this as simply as possible, with comparisons for easy differentiation wherever it is possible, try to add little bit of emojis for user friendly output and do suggest the better option for wide variety of uses"
                    placeholder = st.empty()
                    with placeholder.container():
                        show_skeleton_loader()

                    response_text = ai(query)
                    placeholder.empty()

                    executed = True

                elif any(phrase.lower() in text.lower() for phrase in
                       ["Application", "Letters","letter", "email", "Papers", "Research", "Notice","Notice", "Essay"]):
                    say("Ok, Just one second")
                    st.write("Ok, Just one second")
                    query = text + " in as simple as possible and in formal tone"
                    placeholder = st.empty()
                    with placeholder.container():
                        show_skeleton_loader()

                    response_text = ai(query)
                    placeholder.empty()

                    executed = True

                elif any(phrase.lower() in text.lower() for phrase in
                         ["code", "program", "write a program", "write a code", "java", "c plus plus", "python", "javascript"]):
                    #print("Please specify the programming language")
                    #say("Please specify the programming language")

                    #lang = takeCommand()

                    print("Oh, That's Easy")
                    say("Oh, That's Easy")
                    say("Count 5, I'll be back with the perfectly executable code,")
                    query = f"{text}+write only the code, with little bit of explanation not more than 10 words in commented format"

                    api_key = apikey
                    model = "mistral-large-latest"
                    client = Mistral(api_key=api_key)
                    chat_response = client.chat.complete(
                        model=model,
                        messages=[
                            {
                                "role": "user",
                                "content": query,
                            },
                        ]
                    )

                    st.write(chat_response.choices[0].message.content)
                    executed = True



                if any(phrase in text for phrase in ["thank", "thanks", "thank you","thanks a lot"]):
                    print("Its my pleasure")
                    say("Its my pleasure")
                    executed = True
                    exit()

            except Exception as e:
                pass

        else:
            pass