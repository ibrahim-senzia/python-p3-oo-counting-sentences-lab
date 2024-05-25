#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
      self.value = value if isinstance(value, str) else ''
  
  @property
  def value(self):
      return self._value
  
  @value.setter
  def value(self, new_value):
      if isinstance(new_value, str):
          self._value = new_value
      else:
          print("The value must be a string.")
          self._value = ''
  
  def is_sentence(self):
      return self.value.endswith('.')

  def is_question(self):
        return self.value.endswith('?')
    
  def is_exclamation(self):
        return self.value.endswith('!')
    
  def count_sentences(self):
        # Replace sentence-ending punctuation with a period
        value = self.value.replace('!', '.').replace('?', '.')
        
        # Split the string by periods
        sentences = value.split('.')
        
        # Filter out empty strings
        non_empty_sentences = [s.strip() for s in sentences if s.strip()]
        
        return len(non_empty_sentences)