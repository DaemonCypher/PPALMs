# PPALMS Version 0.2
import sys
from input import *
from questionGeneration import *
from fileFormat import *

def main():
  # Takes file input
  inputFile = input("Enter the name of the file you wish to use: ")
  print()
  file = "test_files/" + inputFile
  inputClass = Input(file)
  inputClass.openFile()
  
  formatClass = FileFormat(inputClass.file)

  # Takes input for keeping/removing comments
  userQuestion = input("Would you like to comments to be removed from the file? (yes/no)\n")
  print()
  if (userQuestion.lower() == "yes"):
    inputClass.file = formatClass.removeComments()

  savedList = inputClass.file

  # Takes input for reordering certain lines
  inputClass.displayNumberedLines()
  inputClass.getInput()

  formatClass.reorderedLines = inputClass.reorderedLines
  formatedFile = formatClass.reorderLines()

  for f in formatedFile:
    print(f)

  # Takes input for multi/blank question generation type
  choice = ""
  print(
    "Would you like to generate multiple choice questions or fill-in-the-blank questions? (multi/blank)"
  )
  while (True):
    userQuestion = input()
    if (userQuestion.lower() == "multi"):
      choice = "multi"
      break
    elif (userQuestion.lower() == "blank"):
      choice = "blank"
      break
    else:
      print("Invalid input, please try again")

  # Takes input for number of questions generated
  numQuestions = 0
  print(
    "How many questions would you like to be generated? (enter valid positive integer 1-10)"
  )
  while (True):
    userQuestion = input()
    if (userQuestion.isdigit()):
      numQuestions = int(userQuestion)
      if numQuestions < 1 or numQuestions > 10:
        print("Invalid input, please try again")
        continue
      break
    else:
      print("Invalid input, please try again")

  # Prints based off of choice
  outputTxt = None
  if choice == "multi":
    mc = ProblemGenerator(MultipleChoice())
    f = open("output.txt", 'w')
    sys.stdout = f
    outputTxt = mc.generateQuestions(savedList, numQuestions)
    f.close()
    
  elif choice == "blank":
    fb = ProblemGenerator(FillInBlank())
    f = open("output.txt", 'w')
    sys.stdout = f
    outputTxt = fb.generateQuestions(savedList, numQuestions)
    f.close()

if __name__ == "__main__":
  main()
