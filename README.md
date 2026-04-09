# Project Title
Rule-Based Restaurant Chatbot with Entity Extraction, Emotion Recognition and Dialogue Management

## Project Description
This project is a rule-based chatbot developed using Python. The chatbot can interact with users, understand basic intents, extract entities like name and city, detect emotions, maintain conversation context, and provide responses based on predefined rules. The chatbot can also be integrated with a restaurant website for menu display, ordering, and table booking.
This project is part of the Conversational AI / Conventional AI coursework.

## Features
The chatbot includes the following features:
•	Intent Detection (Greeting, Menu, Booking, Order, Weather, etc.) 
•	Entity Extraction (Name, City) 
•	Emotion Detection (Happy, Angry, Sad) 
•	Dialogue Management (Context Memory) 
•	Rule-based Response System 
•	Restaurant Menu Interaction 
•	Table Booking 
•	Order Placement 
•	Real-time data support (Weather API optional) 

## Project Folder Structure
```
chatbot_project/
│
├── app.py
├── intents.py
├── entity_extractor.py
├── emotion_detector.py
├── dialogue_manager.py
├── response_generator.py
├── api_module.py
├── knowledge_base.json
└── README.md
```
## How to Run the Chatbot
```
Follow these steps:
Step 1 – Open Terminal
Open terminal in the project folder.
Step 2 – Activate Virtual Environment (if available)
venv\Scripts\activate
Step 3 – Run the Chatbot
python app.py
You will see:
Chatbot Started (type 'bye' to exit)
You:
Now you can chat with the chatbot.
```
## Example Inputs
```
Try these example inputs:
hello
my name is partha
menu
order pizza
booking
weather in delhi
bye
```
## System Architecture
```
The chatbot works using the following pipeline:
User Input
    ↓
Intent Detection
    ↓
Entity Extraction
    ↓
Emotion Detection
    ↓
Dialogue Manager (Context)
    ↓
Rule-Based Response Generator
    ↓
Chatbot Response
```
## Technologies Used
•	Python 
•	Regular Expressions (Regex) 
•	JSON 
•	Rule-based AI 
•	Natural Language Processing (Basic) 
•	Flask (for web integration, optional) 

## Future Improvements
The chatbot can be improved by:
•	Adding a database for orders 
•	Adding a web interface 
•	Using Machine Learning for intent detection 
•	Adding voice input 
•	Deploying on a website 
•	Adding payment integration

## Author Name 
Partha Sarathi Sarkar
