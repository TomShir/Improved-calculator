#creating a calculator 
import time 
import sys
from colorama import Fore 
import random 
import tqdm 
import os 
import logging 
import tqdm
program_title='calculator'
colors=[Fore.RED,Fore.GREEN,Fore.BLUE,Fore.YELLOW,Fore.RESET]
class Math_Functions:
  def __init__(self,first_number,second_number):
    self.first_number=first_number
    self.second_number=second_number 
    
  def addition(self):
    addition_function=lambda x,y:x+y 
    print(f'{addition_function(self.first_number,self.second_number)}')
    
  def subtraction(self):
    subtraction_function=lambda x,y:x-y 
    print(f'{subtraction_function(self.first_number,self.second_number)}')
    
  def multiplication(self):
    multiplication_function=lambda x,y:x*y 
    print(f'{multiplication_function(self.first_number,self.second_number)}')
    
  def division(self):
    division_function=lambda x,y:x/y 
    print(f'{division_function(self.first_number,self.second_number)}')
    
  def exponent(self):
    exponent_function=lambda x,y:x**y 
    print(f'{exponent_function(self.first_number,self.second_number)}')
    
  def return_remainder(self):
    remainder_function=lambda x,y:x%y 
    print(f'{remainder_function(self.first_number,self.second_number)}')
    
    
#Creating a function  to loop over a subscriptable sequence and print it horizontally 
def loop_over(text_color,sequence,delay_time):
  for text in sequence:
    sys.stdout.flush()
    time.sleep(delay_time)
    sys.stdout.write(f'{text_color}{text}')
  else:
    print(f'{Fore.RESET}')
    
#Creating a function to log errors that might occur in the calculator program 
def log_error_messages(error_msg):
  error_logger=logging.getLogger('Error_logger:')
  file_handler=logging.FileHandler('ERROR.log')
  myformat=logging.Formatter('%(asctime)s-%(name)s-%(message)s')
  error_logger.setLevel(logging.ERROR)
  file_handler.setFormatter(myformat)
  file_handler.setLevel(logging.ERROR)
  error_logger.addHandler(file_handler)
  loop_over(text_color=colors[0],sequence=error_msg,delay_time=0.1)
  time.sleep(1)
  error_logger.error(f'{error_msg}')
  
arithmetic_operators=['+','-','*','/','**','%']
mysequence=list(range(1,101,1))
for num in tqdm.tqdm(mysequence,colour='CYAN',desc='Loading Calculator',ncols=100):
    time.sleep(0.01)
else:
  time.sleep(1)
  os.system('cls')
  time.sleep(1)
  for text in f'{program_title}\n\t':
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write(f'\t{random.choice(colors[:-1])}{text.upper()}')
  else:
    time.sleep(1)
    os.system('cls')
    time.sleep(1)
    print(f'{colors[-1]}')
    math_function_obj=Math_Functions(first_number=None,second_number=None)
    while True:
      try:
        first_number=int(input('first_number:'))
        time.sleep(1)
        print(f'{first_number}')
        time.sleep(1)
        arithmetic_operator=input('arithmetic_operator:')
        if arithmetic_operator not in arithmetic_operators:
          log_error_messages(error_msg='Error,not a valid arithmetic operator please try again')
        else:
          time.sleep(1)
          print(f'{first_number} {arithmetic_operator}')
          time.sleep(1)
          last_number=int(input('last_number:'))
          math_function_obj=Math_Functions(first_number=first_number,second_number=last_number)
          time.sleep(1)
          print(f'{first_number} {arithmetic_operator} {last_number} =')
          if arithmetic_operator==arithmetic_operators[0]:
            math_function_obj.addition()
          elif arithmetic_operator==arithmetic_operators[1]:
            math_function_obj.subtraction()
          elif arithmetic_operator==arithmetic_operators[2]:
            math_function_obj.multiplication()
          elif arithmetic_operator==arithmetic_operator[3]:
            math_function_obj.division()
          elif arithmetic_operator==arithmetic_operators[4]:
            math_function_obj.exponent()
          elif arithmetic_operator==arithmetic_operators[5]:
            math_function_obj.return_remainder()
      except ValueError:
        log_error_messages(error_msg='ValueError:Not an appropiate value entered please try again')