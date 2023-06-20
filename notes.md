# Project Ideas

## Progress

- [x] learn the main rasa CLI commands
- [x] replicate the code for rasa rock paper scissors tutorial
- [x] write custom action that reads data from slots and sends out responses to the user
- [x] 


Level 1:
- [x] Write a basic chatbot.
- [x] Run the chatbot and interact with it.
- [x] Understand the basic file structure and skeleton of a Rasa chatbot project.

Level 2:
- [x] Define intents for user inputs.
- [x] Create simple training examples for each intent.
- [x] Train the chatbot with the training data.

Level 3:
- [ ] Define entities to extract specific information from user inputs.
- [ ] Implement entity extraction using regular expressions or pre-trained entity extractors.
- [ ] Test the entity extraction capabilities of the chatbot.

Level 4:
- [x] Build custom actions to handle complex logic or external API integrations.
- [ ] Understand the flow of information between user inputs, NLU, and custom actions.
- [ ] Implement and test a basic custom action.

Level 5:
- [ ] Create more diverse training data to improve the chatbot's understanding.
- [ ] Use data augmentation techniques to enhance the training data.
- [ ] Evaluate and iterate on the chatbot's performance based on user feedback.

Level 6:
- [ ] Design and implement a dialogue management system using Rasa's story format.
- [ ] Define conversation flows with multiple turns and different dialogue paths.
- [ ] Handle slot filling and manage dialogue state effectively.

Level 7:
- [ ] Utilize Rasa's built-in policies for intent classification and action prediction.
- [ ] Experiment with different policies and evaluate their impact on chatbot performance.
- [ ] Fine-tune the policies for better accuracy and user experience.

Level 8:
- [ ] Implement advanced NLU features like synonyms, regex features, and lookup tables.
- [ ] Enhance the chatbot's understanding of user inputs using these advanced NLU capabilities.
- [ ] Fine-tune entity extraction for improved accuracy.

Level 9:
- [ ] Integrate external tools or services like databases, APIs, or external systems with the chatbot.
- [ ] Implement custom actions to interact with external resources.
- [ ] Test and verify the integration between the chatbot and external services.

Level 10:
- [ ] Deploy the chatbot to a production environment.
- [ ] Monitor and analyze the chatbot's performance and user interactions.
- [ ] Continuously improve and refine the chatbot based on user feedback and analytics.


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