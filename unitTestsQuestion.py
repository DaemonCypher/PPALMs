#HOW TO TEST FUNCTIONS
#fb = ProblemGenerator(FillInBlank())
#result = fb.generateQuestions([asdasdasd], 3)
#self.assertEqual(len(result), 3)

import unittest
from questionGeneration import *

class TestPPALMSQuestionGenerator(unittest.TestCase):

  def test_problem_generator_fill_in_the_blank(self):
    generator = ProblemGenerator(FillInBlank())
    numProblems = 1
    lineList = [
      "a b c", "d e f", "g h i", "j k l", "m n o", "p q r", "s t u", "v w x",
      "y z"
    ]
    result = generator.generateQuestions(lineList, numProblems)
    self.assertEqual(len(result), numProblems)

    self.assertEqual(result, {"_ b c": 'a'})

  def test_problem_generator_MultipleChoice(self):
    mc = ProblemGenerator(MultipleChoice())
    result = mc.generateQuestions(["a", "b", "c", "d", "e"], 3)
    # see if the number of question generated is 3
    self.assertEqual(len(result), 3)

  def test_problem_generator_MultipleChoice_anwsers(self):
    mc = ProblemGenerator(MultipleChoice())
    result = mc.generateQuestions(["a", "b", "c", "d", "e"], 3)

    for line in result:
      for ans in line.items():
        # ans[1] is the other possible anwser to the question
        # ans[0] is the right anwser to the question
        # see if the list of possible anwser contains the right anwser
        # check finds the index in ans[1] for the right anwser to the question
        check = ans[1].index(ans[0])
        self.assertEqual(ans[0], ans[1][check])


if __name__ == '__main__':
  unittest.main()
