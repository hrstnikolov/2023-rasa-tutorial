# Project Ideas

## Project ideas
- flight booking
- sushi ordering
- dentist booking
- bank transfer
- rock paper scissors game

## Sushi ordering
todo

## Bank transfer

Scenario:
- hi
- Hello, I am your bank assistant. How may I help you?
- make transfer
- Sure! How much would you like to send?
- 120 EUR
- Who is the recipient?
- Gustav Flamer
- Please confirm the following is correct: 120 EUR to Gustav Flamer.
- I confirm
- The transaction is completed!
- Is there another task I can help you with?
- No, buy.
- Have a nice day! Goodbye!

happy story:
- greeting
- utter_greeting
- make_transfer
- utter_amount
- amount
- utter_recipient
- recipient
- utter_confirm
- confirm
- utter_completed
- utter_other_requests
- deny / affirm
- utter_goodbye

intents:
- greet
- make_transfer
- inform
- affirm
- deny
- goodbye

responses:
- greet
- request_amount
- request_recipient
- confirm_transaction
- transaction_completed
- further_help

## Rock paper scissors
s
### Step-by-step process
In `domain.yml`:
 - update intents
 - update responses
 - add slot `choice`
 - add entity `choice`
 - add actions

In other files:
 - write custom action `ActionPlayRPS`
 - create stories
		- add examples for the slots
 - update the intents in `nlu.yml`
 - enable the `action_endpoint`

Run:
 - train model
 - start action server
 - start rasa shell

## Ideas from ChatGPT

Virtual Assistant: Build a conversational virtual assistant using Rasa that can understand natural language inputs and provide relevant responses. You can integrate it with popular messaging platforms like Slack or deploy it as a chatbot on a website.

Customer Support Chatbot: Develop a chatbot using Rasa that can handle customer support inquiries. Train the chatbot to understand common questions and provide appropriate responses or escalate to a human agent when necessary.

Language Learning Bot: Create a language learning bot with Rasa that helps users practice and improve their language skills. The bot can engage in conversations, ask questions, and provide feedback based on the user's responses.

Personalized Recommendation Chatbot: Build a chatbot that recommends personalized products or services based on user preferences and needs. Use Rasa to understand user preferences and provide tailored recommendations.

FAQ Chatbot: Develop a chatbot that can answer frequently asked questions about a specific topic or domain. Train the bot with a knowledge base of common questions and their corresponding answers.

Appointment Scheduler: Design a chatbot using Rasa that allows users to schedule appointments or book reservations. The bot should be able to understand the user's request, check availability, and confirm the appointment.

Quiz Bot: Create a quiz bot with Rasa that can ask questions on various topics and evaluate the user's answers. Provide feedback and keep track of the user's progress throughout the quiz.

Job Application Assistant: Build a chatbot to assist job seekers in the application process. The bot can help users create resumes, provide job search suggestions, and offer interview tips.

Social Media Assistant: Develop a chatbot that integrates with social media platforms like Twitter or Facebook. The bot can perform actions such as posting tweets, responding to comments, or sending direct messages based on user instructions.

Interactive Storytelling Bot: Create an interactive storytelling bot with Rasa that engages users in an interactive narrative. The bot can present options to the user at various points in the story and adapt the storyline based on their choices.