# Class for gathering user input, opening files, and displaying lines
class Input:

  # Constructor for Input Class
  def __init__(self, fileName):
    self.fileName = fileName
    self.file = []
    self.reorderedLines = []

  # Provides a basic interface for the user to input line numbers for line reordering
  def getInput(self):
    endBool = False
    alreadyTupled = []

    while (endBool == False):
      userInput = input(
        "Specify lines that can be put in any order by (IE: enter '1 3') \nEnter 'End' if you are finished reordering lines: "
      )
      print(userInput)
      if (userInput.lower() == "end"):
        endBool = True
      else:
        userInput = list(map(int, userInput.split(' ')))
        for num in userInput:
          if (num not in range(1, len(self.file) + 1)):
            raise Exception("Error: Inputed line number does not exist")
          elif (num in alreadyTupled):
            print(alreadyTupled)
            raise Exception("Error: Inputed line has already been used")
          else:
            alreadyTupled.append(num)
        userInput = tuple(userInput)
        self.reorderedLines.append(userInput)

  # Read the lines of the input file into a list
  def openFile(self):
    try:
      f = open(self.fileName)
      file = f.readlines()
      f.close()
      self.file = file
    except:
      print("File not in directory.")
      exit(1)

  # Format the lines of the file so that each line is numbered incrementally
  def displayNumberedLines(self):
    for i, l in enumerate(self.file):
      print(i + 1, l)