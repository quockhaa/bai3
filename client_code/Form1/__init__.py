from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    anvil.server.connect("your_anvil_server_key")

  def btnSort_click(self, **event_args):
    numbers = self.txtNumbers.text
    algorithm = self.dropdownAlgorithm.selected_value
    sorted_numbers = anvil.server.call('sort_numbers', numbers, algorithm)
    self.lblSortedNumbers.text = ', '.join(map(str, sorted_numbers))

anvil.server.connect("your_anvil_server_key")
anvil.server.wait_forever()
