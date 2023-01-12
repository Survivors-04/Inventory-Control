import ipdb
from rest_framework.views import  Request, Response, status
class InvalidValueUpdate(Exception):
   def __init__(self, message):
      
      self.message = message

     
   
   
      

