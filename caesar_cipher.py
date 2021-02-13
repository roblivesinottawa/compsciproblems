# enter a string representing letters of the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# function that prevents that the list will be out of range
def shift_amount(i):
  return i%26

# function will take a string and the number to be shifted by
def encrypt(text, shift_by):
  result = '' # to store the result 
  text = text.lower() #turn letters into lower case 
  for word in text: #loop through words in the text parameter to be entered by user
    if word not in alphabet: # if the word is not in the alphaet
      result = result + word #the result equals itself plus the word
    else:
      alphabet_index = alphabet.find(word) # find the word in the alphabet
    #  we add the letter that we get to the alphabet index after the shift
      result = result + alphabet[shift_amount(alphabet_index + shift_by)]
  return result

# ask user to enter the string to be deciphered
new_string = input("enter text to be deciphered: ")
print(encrypt(new_string, - 5)) #enter the text plus the number to be shifted by
# positive integers will cipher and negative integers will decipher
