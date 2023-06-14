# Bank Assistant

## Idea

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

## Workflow

create new rasa project - `rasa init`  


