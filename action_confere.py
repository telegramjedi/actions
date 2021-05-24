from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionCheckAnswer(Action):
   def name(self) -> Text:
      return "action_check_answer"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      dispatcher.utter_message("Hello World! from custom action")      return []