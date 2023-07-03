from abc import ABC, abstractmethod
import random


class QuestionType(ABC):

  @abstractmethod
  def generateQuestions(self) -> None:
    pass


class ProblemGenerator():

  def __init__(self, questionTypeChoice: QuestionType) -> None:
    self._questionTypeChoice = questionTypeChoice
    self.allQuestions = []

  # Will -> might remove questionAmount; not used anywhere
  @property
  def questionAmount(self) -> int:
    return self.questionAmount

  @property
  def questionTypeChoice(self) -> QuestionType:
    return self._questionTypeChoice

  @abstractmethod
  def generateQuestions(self, lineList, numProblems) -> dict:
    return self._questionTypeChoice.generateQuestions(lineList, numProblems)


class QuestionAmount():
  def questionAmount():
    pass


# Class to generate Fill in the Blank Questions
class FillInBlank(QuestionType):

  # Overrides abstract method generateQuestion() from ProblemGenerator Class
  def generateQuestions(self, lineList, numProblems):
    questions = {}
    #Iterates though each line in the list
    for line in lineList:
      splitLine = line.strip().split(" ")
      #Iterates though each word in the line
      for i in range(0, len(splitLine)):
        #Temp store for the line to remove a word
        temp = splitLine[:]
        #Choose the blank to fill iterativly
        correctAnswer = splitLine[i]
        underscores = ""
        #Creates a string with underscores to replace the word choosen for the blank
        for x in range(len(correctAnswer)):
          underscores += "_"
        temp[i] = underscores
        question = " ".join(temp)
        #Check if desired num of questions is reached
        if len(questions) == numProblems:
          for question in questions:
            print("Question:", question, "\nAnswer:", questions[question])
          return questions
        questions[question] = correctAnswer

    # with open("generated-questions.txt", "w+") as f:
    #   for question in questions:
    #     f.write(question)
    for question in questions:
      print(question)
    return questions


# Class to generate Multiple Choice Questions
class MultipleChoice(QuestionType):
  # Overrides abstract method generateQuestion() from ProblemGenerator Class
  def generateQuestions(self, lineList, numProblems):
    # Random word bank of possible anwsers
    wordBank = [
      "print(ret)", "break", "continue", "listlist.append",
      "for i in range(len(listy))", "random.randint(0,100)",
      "[news, nature, nurture, nintendo, neck, name]", "list.copy()",
      "list.pop()", "for l in lineList:", "while(true)", "return helloskis",
      "class ThisIsACoolClass", "def funFunction(self, create, array):",
      "{key1: value1, key2:   value2}", "str(100)",
      "print('hello world - I am an alien from outerspace. My name is will and i am the master')",
      "not type(string)", "&&", "||", "if true or false:",
      "if will == 'alien from outer space':", "int", "char", "string",
      "list.inster('abcdefghijklmnopqrstuvwxyz')"
    ]
    # List of all questions
    allQuestions = []

    allLines = []
    for i in range(numProblems):
      # Lines is a copy of the file lines
      lines = lineList.copy()
      # randNum is random index of lineList
      randNum = random.randint(0, len(lineList) - 1)
      # randomLine is the line used for the question
      randomLine = lineList[randNum]
      underscores = ""
      # hiding the question by replacing the line with -'s
      for x in range(len(randomLine)):
        if (randomLine[x] == " "):
          underscores += " "
        else:
          underscores += "-"
      lines[randNum] = underscores
      allLines.append(lines)

      question = {}
      # randomWordx is a possible anwser to the multiple choice question
      randomWord1 = wordBank[random.randint(0, len(wordBank) - 1)]
      randomWord2 = wordBank[random.randint(0, len(wordBank) - 1)]
      randomWord3 = wordBank[random.randint(0, len(wordBank) - 1)]
      # anwserList is the list of possible anwsers to be displayed
      answerList = [randomLine, randomWord1, randomWord2, randomWord3]
      # make sure the right anwsers is not always A,B,C, or D
      random.shuffle(answerList)
      question[randomLine] = answerList
      allQuestions.append(question)

    # question index
    index = 1
    # allQuestions is a list of dictionary
    for q in allQuestions:
      #print(q)
      for key in q:
        print()
        print("QUESTIONS")
        print(
          "What is missing from the code below? What should be placed on the dotted line?\n"
        )
        # print out the question
        for l in allLines[index - 1]:
          print(l)
        # print out the anwser and possible anwsers
        print()
        print("ANSWERS")
        print("   a) ", q[key][0].strip())
        print("   b) ", q[key][1].strip())
        print("   c) ", q[key][2].strip())
        print("   d) ", q[key][3].strip())
        print("CORRECT ANSWER:", key.strip())
        index += 1

    return allQuestions
