# -*- coding: utf-8 -*-
"""AssignmentForSnippetCompletion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KDsHwAswCQ5IzRxQDWsucak-g4KDV5xg

# Assignment: Complete the Snippet (Snippet completed)

Shubh started building a basic Python Script which goes through the entire text of a particular book and mugs up all its words. After that it asks you for a word, goes over the times when this word came in the text and gives you the complete sentence in which it was used. You may choose to ask for as many such sentences as the number of occurences of the word.

He's managed to come up with the part where he loads the file into Memory. He also managed to come up with snippets of code which could potentially do something if completed, but he has many deadlines to look after and not enough caffeine to turn to code. Can you help him?
"""

File = open("HarryPotterAndTheSorcerersStone.txt", encoding = 'UTF-8') #This is to open the file which is to be read.

"""Next he makes a list of all the words present in the novel mapping them to their index(position) in the list of words (i.e. ListOfWords). This is done by mapping every word (a string) to a list (list of indices), and this is stored as a Dictionary (DictionaryoOfWords)



He makes use of the readlines() method which is used to extract all the lines from any text and the split() function which could be used to split any sentence into distinct words. The replace() method is used on strings to replace certain segments of the string with something else.
"""

DictionaryOfWords = {}  #Dictionary mapping every word to a list (of indices of the words' occurences).
Novel = []  #List of all words in the order, in which they appear.

i = 0 #Counter Variable to keep track of index of words.

for line in File.readlines(): #Iterating over all lines present in the text.
    
  line = line.replace(".", "").replace(",", "").replace('?', '').replace('!', '').replace('[', '').replace(']', '').replace('(', '').replace(')', '').replace('%', '').replace('/', '').replace('\', '')      

  for word in line.split(' '):  #This would split the line into many different words, and iterate over these words
                                                                             
    if word in DictionaryOfWords.keys():  #If the word is already present in the dictionary
      DictionaryOfWords.get(word).append(i)        
                                                                             
    else:
      custom_list = []        
      custom_list.append(i)
      DictionaryOfWords.update({word:custom_list})  #Creating a new entry in the dictionary.
                                
    Novel.append(word)  #Adding the Word in the Novel's ordered list of words
                                                                             
    i+=1

"""That guy truly left a lot of work for you!

Now that you've done that, We have the words in the novel alongwith where they appeared in the text loaded into memory (Thanks to You!).

The Next Step would be to answer any queries the user may have.

To do this, we define the function GetQuery() which returns the word as well as the number of results the user wants to see (as a tuple):


"""

#Function to take Query from the User.

def GetQuery():
   
  word = str(input("Enter your word and press Enter: "))  #Getting Input from the user regarding what word the user wants to query for.

  Number = int(input("Enter maximum number of results you wish to see and press Enter: "))  #Getting Input from the user regarding how many results the user wants to see.

  return (word, Number) #Returning output as a tuple of the word and the Number of results

"""Now, We need a function which takes as input the index of any particular word and prints the words surrounding it as if they were in an actual sentence. 

This is done by iterating over the words surrounding it, and printing them with gaps in between. We also assume that this occurence isn't a boundary case and thus, the 10 words surronding it actually exist.
"""

def PrintContext(index):
    
  global Novel  #Declares the list Novel as a Global Variable
    
  for i in range(index - 5, index + 6): #Defines the range so that the task above is fulfilled
    print(Novel[i], end = ' ') #Prints the word (using List Indexing) with a space after that
    print('\n') #newline

"""The result of the GetQuery() function will be passed into a second function which would take as input the word and the number of results to be displayed and do so!"""

def PrintResult(word, NumQuery):
  
  global DictionaryOfWords  #Declares the dictionary DictionaryOfWords as a Global Variable
    
  L = DictionaryOfWords.get(word) 
    
  for i in range(0,min(len(L),NumQuery)):
    PrintContext(L[i])  #Prints the words surrounding the ith occurence of the given word

"""Finally, you need an infinite loop which runs until the user wants it to and asks for the next word (if the user wants to query more) or end the loop."""

while 1>0: #Infinite while loop.   
    
  Choice = str(input("Press Y in order to Continue with the next query or N to end. (Please press Enter after entering your choice.)"))  
  
  if Choice == "Y":  #If the user wants to query 
    word, max_num = GetQuery()
    PrintResult(word, max_num)       
        
  else:
    break #Else the loop ends.