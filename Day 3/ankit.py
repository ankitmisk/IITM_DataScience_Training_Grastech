print('''This is Ankit Module in Python
Info: https://www.google.com/''')



def check_palindrome(word:str):
  if type(word) == str:
    word = word.upper()
    if word == word[::-1]:
      return 'Palindrome'
    else:
      return 'Not a Plaindrome'
  else:
    return 'Invalid Data Type'



def give_fibo(n):
  fibo = [0,1]
  for i in range(n-2):
     last_num = fibo[-1]
     second_last_num = fibo[-2]
     next_num = last_num + second_last_num
     fibo.append(next_num)
  return fibo


def check_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return 'Not a Prime Number'
            break
            print('Happy Holi')
    else:
        return 'Prime Number'


def print_star(n = 5, typ = 'left',shape = '*'):
  if typ  == 'left':
    space  = ''

  elif typ == 'right':
    space = '  '

  elif typ == 'mid':
    space = ' '

  for i in range(1,n+1):
    print(space*(n-i) + i*f'{shape} ')



def sum_of_n_natural_numbers(n):
    result = 0
    for i in range(1,n+1):
        result += i
    return result

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result


def total_sales(*args):
  #unpacking
  result = 0
  for i in args:
    result += i
  return result

def minn(*data):
  min_ele = data[0]
  for i in data[1:]:
    if i< min_ele:
      min_ele = i
  return min_ele

def student_records(**kwargs):
  import pandas as pd
  try:
    data = pd.DataFrame(kwargs)
    return data
  except:
    data = pd.DataFrame(kwargs,index = [1])
    return data

def show_time():
  try:
    while True:
      import time
      print(time.asctime())
      time.sleep(1)
      display(clear = True)
  except:
    print('Timer has been Stopped!!')

def sound_box(paisa,platform = 'Paytm'):
    from gtts import gTTS
    text  = f'''{platform} par {paisa} rs Prapt hue.'''
    audio = gTTS(text)
    audio.save('paytm.mp3')

    import pygame as p
    p.init()

    music = p.mixer.Sound('paytm.mp3')
    music.play()
