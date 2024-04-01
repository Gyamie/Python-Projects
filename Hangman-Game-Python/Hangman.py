#Step 1 
import random
import hangman
import hangman_words


chosen_word = random.choice(hangman_words.word_list)
word_len = len(chosen_word)
lives = 6

print(hangman.logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_len):
  display += '_'
 
while True :
  
     Guess = input('Please guess a letter\n').lower()

     if Guess in display:
       print('letter already known')
       
      #Check guessed letter
     for position in range(word_len):
         letter = chosen_word[position]
         if Guess == letter:
           display[position] = letter
           
      #Check if user is wrong.
     if Guess not in chosen_word:
           print('letter is not in the word')
           lives -= 1
           if lives == 0 :
             print('you lose')
     
  #Join all the elements in the list and turn it into a String.
     print(f"{' '.join(display)}")

  #Check if user has got all letters.
     if '_' not in display:       
       print('You have won')
     
     print(hangman.stages[lives])
      


  

  

     

          

      
