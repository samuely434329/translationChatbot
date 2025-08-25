# Translation Chatbot Tutor
#### Video Demo: https://www.youtube.com/watch?v=Ev1-GYBdQA8 
#### Description: 
A webpage site designed to help indivduals hone their non-native language skills via a translation chatbot. The user inputs the text they want translated, and uses the target language dropdown menu to select a target language. They submit the chat and the gemini api responds in the chat box with a message of 1. A translation of the text 2. Providing context and extra details 3. Keeping the conversation going in the target language.

## Purpose: 
To help individuals learn or practise non-native languages with an interactive chatbot that can translate, explain and clarify, all in a conversation setting. For example, if someone wants to improve their fluency in french, they would use this chatbot to learn and translate phrases and sentences to understand. This conversation style approach is better than static translation because it simulates real world conversations unlike simply learning grammer or meaning. 

## Technologies Used: 
The chatbot itself was created using a gemini api key and running it in a python file. HTML was used for the homepage, CSS was used for simple styling, javascript for receiving user input (select language and chatbox). Flask was used for the connection between my javascript (user input) and the gemini api chatbot.

## Project Files: 
In the static folder there is the style css formatting, in the templates folder exists the index.html with only the main webpage/chat. The interface was designed to look like chatgpt or gemini, a clean and simple chatbot homepage. There are the new chats to the left side seperated by a divider, and there is the chatbox with and input area and output area. The javascript is located inside the index.html and is responsible for taking the information from the user, to the flask backend where it uses the gemini api; located in chatbot.py to create a response. The javascript gets the info from the two event readers of the language submit button and the chat submission. The javascript creates a new <div> element with the <fetch>ed api response inside of it, then its added to the chat box using appendChild(). then it uses Venv just makes sure libraries stay seperate for this project and .env simply contains the gemini api key for organization sake.  

## Design Choices 
I have three reasons for choosing Flask, reason one is because its the simplest way to create a backend for a website, reason two is that we learned it in the cs50x course, and reason three ist that my tutorial for using a gemini api key involved using flask. I used inline javascript because i have no idea how to connect the script if its not inside HTMl. Gemini api is the only free api ai i saw online, so i chose it. Chatgpt would have been even simpler to create with less words, but its less customizable and also it costs money.

## Challenges and Lessons:
 What was difficult was the process of connecting user input from javascript to flask, using that input and getting a response from chatbot, then displaying output back on html. Longest time spent was creating the select language dropdown. The issue being using different variables for different files creating typo errors. The solution ended up being searching through all files and renaming the different variables to one common name. It ended up being target_lang.

## Future Improvements: 
1. Allowing user to create multiple chats, this would likely require sqlite which we learned in this course. 2. Fix an issue with language session saving but not displaying to html. The language selection is saved in the session, but the html doesnt not update when refreshed. 3. Allow voice input and output, I have no idea how to do this. 4. Save the history of conversations, either use sqlite3 to save to specific chat databases with a chat history, or use some sort of session thing. 5. Add tools that chatbot can use for example a news website that chatbot can access.

## Conclusion 
This project was designed to show my ability to use an ai to create an interactive translation website. It's supposed to help people with translations. It was a simple idea which i belive was executed somewhat well. Basically what i wanted to do was have the ai work for me, and create everything around it.