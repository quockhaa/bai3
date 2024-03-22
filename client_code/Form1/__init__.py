from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
    def __init__(self, **properties):
       
        self.init_components(**properties)
      
    

 
    def insertion_sort(self, arr):
        # Thuật toán sắp xếp chèn
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def insertion_sort_Descending(self, arr):
       
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key > arr[j]:  
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def btnSort(self, **event_args):

          numbers = [int(num) for num in self.text_box_1.text.split()]
        
        
          sorted_numbers = self.insertion_sort(numbers)
        
        
          self.text_box_2.text = ' '.join(map(str, sorted_numbers))
  
          sorted_numbers_3 = self.insertion_sort_Descending(numbers)
          self.text_box_3.text = ' '.join(map(str, sorted_numbers_3))
      
