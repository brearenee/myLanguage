
class Error(Exception):
  def __init__(self, error_name, details):
    self.error_name = error_name
    self.details = details
    
  def as_string(self):
    result = f'{self.error_name}: {self.details}\n'
    return result

class IllegalCharError(Error):
  def __init__(self, details):
    super().__init__('Illegal Character', details)

  def as_string(self):
    result = f'{self.error_name}: {self.details}\n'
    return result


class IllegalGrammarError(Error):
  def __init__(self, details):
    super().__init__('Illegal grammar', details)

  def as_string(self):
    result = f'{self.error_name}: {self.details}\n'
    return result