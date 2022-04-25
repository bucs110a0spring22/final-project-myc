import time
import sys

class Akinator: 

  def dininghalls():
    def game():
      not_used = ['Is your dining hall newly renovated?', 'Does your dining hall have two different sides for two separate living communities?', 'Does your dining hall have fireplace seating on the floor above?', 'Does your dining hall have rooftop seating?', 'Does your dining hall have night owl?', 'Is your dining hall close to the lecture hall?', 'Is your dining hall up a hill?', 'Does your dining hall have mailboxes in the same building?', 'Is your dining hall made up of chain restaurants?', 'Is your dining hall painted green?', 'Is your dining hall closed on the weekends?', 'Is your dining hall more expensive than the others?', 'Does your dining hall have Kosher Korner?']
    for question in not_used:
      for i in question:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
      print('')
      reply = int(input('Answer: '))
      if reply == 1: 
        answer.append(reply)
      elif reply == 2:
        answer.append(reply)

    '''takes no params, prints out questions and takes the users answer, either 1 or 2, and appends the answer list based on the value given'''

    def results():
      if answer == c4_Dining_Hall:
        print('Is your dining hall C4 Dining Hall?')
      elif answer == hinman_Dining_Hall:
        print('Is your dining hall Hinman Dining Hall?')
      elif answer == cIW_Dining_Hall:
        print('Is your dining hall College in the Woods Dining Hall?')
      elif answer == appalachian_Dining_Hall:
        print('Is your dining hall Appalachian Dining Hall?')
      elif answer == marketplace:
        print('Is your dining hall the Marketplace?')

    '''takes no params and returns nothing, takes the appended list from the game function and comapares it to the variables to find the correct option, prints out a question statement'''

# 1 = Yes  -- 2 = No
# initializing variables
    c4_Dining_Hall = [2,1,1,2,1,2,2,2,2,2,2,2,1]
    hinman_Dining_Hall = [1,2,2,1,2,1,2,2,2,2,2,2,2]
    cIW_Dining_Hall = [2,2,2,2,2,2,2,2,2,1,1,2,2]
    appalachian_Dining_Hall = [2,2,2,2,1,2,1,1,2,2,2,2,2]
    marketplace = [2,2,2,2,2,2,2,1,1,2,2,1,2]
    answer = []

    game()
    results()

  '''Takes no params and returns nothing, Gives questions and uses the answers to guess the user's choice of dining hall'''

  def schools():
    def game():
      answer = []
      not_used = ['Is computer science a major in your school?', 'Does your school have the most students in it?', 'Is the acronym of your school three letters?', 'Do careers linked to your school focus on the design of drugs and pharmaceuticals?', 'Can the students from your school often be found walking around in formal attire?', 'Is your college located on the Health Sciences campus?', 'Is Human Development a major within your college?', 'Is the Speech and Hearing Sciences minor a program within your school?', 'Are the buildings Academic A and Academic B directly associated with your school?', 'Is your college heavily associated with the Engineering Building?', 'Does your school offer the largest number of majors and minors?', 'Is your college technology-based?', 'Is your college the newest school?', 'Is your college located at the University Downtown Center?']
      for question in not_used:
        for i in question:
          sys.stdout.write(i)
          sys.stdout.flush()
          time.sleep(0.05)
        print('')
        reply = int(input('Answer: '))
        if reply == 1:
          answer.append(reply)
        elif reply == 2:
          answer.append(reply)
    '''takes no params, prints out questions and takes the users answer, either 1 or 2, and appends the answer list based on the value given'''

    def results():
    
      if answer == watson:
        print('Is your school Watson College of Engineering and Applied Sciences?')
      elif answer == harpur:
        print('Is your school Harpur College of Arts and Sciences?')
      elif answer == som:
        print('Is your college the School of Management?')
      elif answer == pharm:
        print('Is your college the School of Pharmacy and Pharmaceutical Sciences?')
      elif answer == ccpa:
        print('Is your school the College of Community and Public Affairs')
      elif answer == decker:
        print('Is your school Decker College of Nursing and Health Sciences?')

    '''takes no params and returns nothing, takes the appended list from the game function and comapares it to the variables to find the correct option, prints out a question statement'''
        
# initialize variables
# 1 = yes and 2 = No

    watson = [1,2,2,2,2,2,2,2,2,1,2,1,2,2]
    harpur = [2,1,2,2,2,2,2,2,2,2,1,2,2,2]
    som = [2,2,1,2,1,2,2,2,1,2,2,2,2,2]
    pharm = [2,2,2,1,2,1,2,2,2,2,2,2,1,2]
    ccpa = [2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    decker = [2,2,2,2,2,1,2,1,2,2,2,2,2,2]
  

    game()
    results()

  '''Takes no params and returns nothing, Gives questions and uses the answers to guess the user's school''

  def places():
    def game():
      not_used = ['Does your place have a printing area?', 'Does your place have a Dunkin Donuts?', 'Do students often work on building technology in your place?', 'Is your place connected to the lecture hall?', 'Does your place have 14 classrooms?', 'Does your place have research materials focused on the sciences?', 'Is the mailroom located in your place?', 'Is your place associated with Watson College?', 'Does your place have four floors for quiet studying?', 'Does your place have three floors of just basic classrooms?', 'Does your place have a classroom that can hold around 450 students?', 'Does your place have a theatre?', 'Does your place have a bowling alley?']
      for question in not_used:
        for i in question:
          sys.stdout.write(i)
          sys.stdout.flush()
          time.sleep(0.05)
        print('')
        reply = int(input('Answer: '))
        if reply == 1:
          answer.append(reply)
        elif reply == 2:
          answer.append(reply)

      '''takes no params, prints out questions and takes the users answer, either 1 or 2, and appends the answer list based on the value given'''

    def results():
      if answer == library: 
        print('Is your place Bartle Library?')
      elif answer == union:
        print('Is your place the University Union?')
      elif answer == engineering:
        print('Is your place the Engineering Building?')
      elif answer == lecture_hall:
        print('Is your place the Lecture Hall?')
      elif answer == classroom_wing:
        print('Is your place the Classroom Wing?')
      elif answer == science_library:
        print('Is your place the Science Library?')
      elif answer == fine_arts:
        print('Is your place the Fine Arts Building?')

    '''takes no params and returns nothing, takes the appended list from the game function and comapares it to the variables to find the correct option, prints out a question statement'''

        
  # initialize variables
  # 1 = yes, 2 = no
    library = [1,2,2,2,2,2,2,2,1,2,2,2,2]
    union = [2,1,2,2,2,2,1,2,2,2,2,2,1]
    engineering = [2,2,1,2,2,2,2,1,2,2,2,2,2]
    lecture_hall = [2,2,2,2,1,2,2,2,2,2,1,2,2]
    classroom_wing = [2,2,2,1,2,2,2,2,2,1,2,2,2]
    science_library = [1,2,2,2,2,1,2,2,2,2,2,2,2]
    fine_arts = [2,2,2,2,2,2,2,2,2,2,2,1,2]
    answer = []

    game()
    results()

  '''Takes no params and returns nothing, Gives questions and uses the answers to guess the user's place'''


# not fully working yet, need to make some changes with the variables

# when we make the screens and implement the buttons fully, we can replace the 1s and 2s with clicking the correct buttons, and we can print the text onto the screens for the questions and answers