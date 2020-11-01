# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


#This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

quizzes={
	"c++" : "url: c++/quiz",
	"c" : "url: c/quiz",
	"python" : "url: python/quiz",
	"c#" : "url: c#/quiz",
	"java" : "url: java/quiz"
}

class ActionShowQuiz(Action):
	def name(self) -> Text:
		return "action_show_quiz"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		skill= tracker.get_slot("skill")
		quiz=quizzes.get(skill)

		if quiz is None:
			output= "Could not find a quiz for {}".format(skill)
		else:
			output="Looking for your quiz!!\nScore a minimum of 75% to go proceed to stage 2... \nGo to the link to move through the first round of specialization for {}- \n{}".format(skill,quiz)

		dispatcher.utter_message(text=output)
		
		return []
