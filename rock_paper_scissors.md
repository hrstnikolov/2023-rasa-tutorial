# Rock Paper Scissors Chatbot

## Step-by-step process
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
