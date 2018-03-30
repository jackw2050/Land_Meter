class Land_Sys:
    'Common base class for for all system control'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
        
        
def main():
  continue = True
  system_1 = Land_Sys("Zara", 2000)  # any initialization variables - there probably won't be any
  while (continue):
    
