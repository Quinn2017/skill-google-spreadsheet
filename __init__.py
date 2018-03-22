import pygsheets

from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler

# The logic of each skill is contained within its own class, which inherits
# base methods from the MycroftSkill class with the syntax you can see below:
# "class ____Skill(MycroftSkill)"

class InventorySkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(InventorySkill, self).__init__(name="InventorySkill")

#--------------------------------INITIALIZER------------------------------

    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))

    #Create a GoogleSpreadsheet
        Inventory_Intent = IntentBuilder("InventoryIntent").\
           require("InventoryKeyword").build()
        self.register_intent(Inventory_Intent, self.handle_Inventory_Intent)

#--------------------------------HANDLERS------------------------------

    # The "handle_xxxx_intent" functions define Mycroft's behavior when
    # each of the skill's intents is triggered.

    def handle_Inventory_Intent(self, message):
        self.speak("Yes, I have your Google Spreadsheet right here.")
        gc = pygsheets.authorize(outh_file='/home/pi/skills/skill-google-spreadsheet/client_id.json', outh_nonlocal=True) #you can comment out everything except these four next lines, and the import pygsheets, and use the sheets.googleapis.com-python.json instead of the client_id.json
        sh = gc.open('tonyquinn2018')
        wks = sh.sheet1
        wks.update_cell('H1', "Test 2")

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution.
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return InventorySkill()
