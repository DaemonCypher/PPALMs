
# PPALMS VERSION 0.2 (Updated 12/12/22)
### William Yang, Ryan Yang, Keean Laferriere, Leo Cui
# Description
In this system, we handle the *problem generation* for the PPALMS reordering of lines. In particular, we handle two specific usage scenarios:
1. Multiple choice problem generation: Based off of prior input according to PPALMS Version 0.1 (details below), we generate a user-specified number of multi-choice questions.
2. Fill-in-the-blank problem generation: Based off of prior input according to PPALMS Version 0.1 (details below), we generate a user-specified number of fill-in-the-blank questions.

# How to Build and Execute
Pre-steps:
1. Launch a terminal session and cd (change directory) into the folder where you installed this repository. File path should match "./PPALMS". Verify that main.py exists in this folder.
2. Verify python3 is installed on your system by typing `python3 --version` and hitting enter on your terminal. If no version is found, please find an online guide to install python3 on your system.
3. **IMPORTANT:** Make sure you have followed the steps defined at PPALMS VERSION 0.1 below. The following instructions build off of steps up to this point.

Steps:
1. The system will prompt you to enter "multi" for multiple-choice generated questions or "blank" for fill-in-the-blank generated questions. Type and enter the specified problem type you would want to generate from.
2. The system will prompt you to enter an integer between 1 and 10 depending on the number of questions you want to generate. Type and enter a valid number in the range.

# How to Run Unit Tests
Steps:
1. In the terminal, type 'python3 unitTestsQuestion.py -v' in the root directory and hit enter
     - The system will output the results of the unit tests contained within "unitTestsQuestion.py"

# Test Scenario 1 (Requirement: Multiple-Choice Question Generation)
Steps:
1. In the terminal, type "python3 main.py" and hit enter
2. The system will prompt you to "Enter the name of the file you wish to use." **Enter "test.py"**
3. The system will prompt you to "Remove Comments?". **Enter "yes"**
5. The system will prompt you to specific which lines (if any) that you want to reorder. **Enter "end"**
6. The system will prompt you to choose a question type to generate. **Enter "multi"**
7. The system will prompt you to choose a number of questinos to generate between 1-10. **Enter "2"**

**Verify that file "output.txt" resembles**


QUESTIONS
What is missing from the code below? What should be placed on the dotted line?

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ret = []

        save = list.copy(nums)

        for i in range(0,len(nums)):

            save.pop(i)

            ------------------- -- -------
                ret.append(i)

            save = list.copy(nums)

        return ret

ANSWERS
   a)  class ThisIsACoolClass
   b)  char
   c)  if((target-nums[i]) in save):
   d)  list.pop()
CORRECT ANSWER: if((target-nums[i]) in save):

QUESTIONS
What is missing from the code below? What should be placed on the dotted line?

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        --- - ---
        save = list.copy(nums)

        for i in range(0,len(nums)):

            save.pop(i)

            if((target-nums[i]) in save):

                ret.append(i)

            save = list.copy(nums)

        return ret

ANSWERS
   a)  continue
   b)  str(100)
   c)  list.pop()
   d)  ret = []
CORRECT ANSWER: ret = []


# Test Scenario 2 - (Requirement: Fill-in-the-Blank Question Generation)
Steps:
1. In the terminal, type "python3 main.py" and hit enter
2. The system will prompt you to "Enter the name of the file you wish to use." **Enter "test.py"**
3. The system will prompt you to "Remove Comments?". **Enter "yes"**
5. The system will prompt you to specific which lines (if any) that you want to reorder. **Enter "end"**
6. The system will prompt you to choose a question type to generate. **Enter "blank"**
7. The system will prompt you to choose a number of questinos to generate between 1-10. **Enter "3"**

**Verify that file "output.txt" resembles**

Question: _____ Solution: 
Answer: class
Question: class _________ 
Answer: Solution:
Question: ___ twoSum(self, nums: List[int], target: int) -> List[int]: 
Answer: def

---

# PPALMS VERSION 0.1
# Description
In this system, we handle the *annotations* for the PPALMS reordering of lines. In particular, we handle three specific usage scenarios:
1. No annotations necessary: In this case, no necessary lines in the included file need to be removed or paired with other lines.
2. All single-line comments are not included in the generated questions: In this case, we omit any lines in the code that begin with comment syntax (IE: #,//, etc.)
3. Some lines of code can be in any order: In this case, the user may want to identify specific sets of lines that can be interchangable while still maintaining correctness.
4. Navigate to the file "output.txt" to see the questions that have been generated according to your inputs.

# How to Run Unit Tests
Steps:
1. In the terminal, type 'python3 unitTests.py -v' in the root directory and hit enter
     - The system will output the results of the unit tests contained within "unitTests.py"

# How to Build and Execute
Pre-steps:
1. Launch a terminal session and cd (change directory) into the folder where you installed this repository. File path should match "./PPALMS". Verify that main.py exists in this folder.
2. Verify python3 is installed on your system by typing `python3 --version` and hitting enter on your terminal. If no version is found, please find an online guide to install python3 on your system.

Steps:
1. (Optional) Import your desired code file (.txt, .c, .cs, .css, .html, .java, .cpp, .rs, .sql, .py supported) into test_files folder to be annotated
2. In the terminal, type "python3 main.py" and hit enter
3. The system will prompt you to "Enter the name of the file you wish to use." Type the file name you want to run and hit enter
4. The system will prompt you to "Remove Comments?". Type "yes" and hit enter to omit comments for annotations. Type "no" and hit enter to keep comments for annotations
5. The system will prompt you to specifie which lines (if any) that you want to reorder.
    - If yes, enter the numbers corresponding to the lines you want reordered seperated by a space (IE: enter '1 3') for lines 1 & 3
    - If no, type "end" to finish executing the program

# How to Run Unit Tests
Steps:
1. In the terminal, type 'python3 unitTests.py -v' in the root directory and hit enter
     - The system will output the results of the unit tests contained within "unitTests.py"

# Test Scenario 1 (Requirement: Some lines of code can be used in any order)
Steps:
1. In the terminal, type "python3 main.py" and hit enter
2. The system will prompt you to "Enter the name of the file you wish to use." **Enter "test.py"**
3. The system will prompt you to "Remove Comments?". **Enter "no"**
4. The system will prompt you to specific which lines (if any) that you want to reorder. **Enter "1 4"**
5. The system will prompt you to specific which lines (if any) that you want to reorder. **Enter "end"**


**Verify that the output recieved resembles**

('# this is a text format\n', '    def twoSum(self, nums: List[int], target: int) -> List[int]:\n')


class Solution:

        ret = []

        save = list.copy(nums)

        for i in range(0,len(nums)):

            save.pop(i)

            if((target-nums[i]) in save):

                ret.append(i)

            save = list.copy(nums)

          

        return ret

# Test Scenario 2 - (Requirement: Remove Single-Line Comments)
Steps:
1. In the terminal, type "python3 main.py" and hit enter
2. The system will prompt you to "Enter the name of the file you wish to use." **Enter "test.py"**
3. The system will prompt you to "Remove Comments?". **Enter "yes"**
5. The system will prompt you to specific which lines (if any) that you want to reorder. **Enter "end"**


**Verify that the output recieved resembles**

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ret = []

        save = list.copy(nums)

        for i in range(0,len(nums)):

            save.pop(i)

            if((target-nums[i]) in save):

                ret.append(i)

            save = list.copy(nums)

        return ret

# Test Scenario 3 - (Requirements: No Annotations Necessary)
Steps:
1. In the terminal, type "python3 main.py" and hit enter
2. The system will prompt you to "Enter the name of the file you wish to use." **Enter "test.py"**
3. The system will prompt you to "Remove Comments?". **Enter "no"**
4. The system will prompt you to specific which lines (if any) that you want to reorder. **Enter "end"**


**Verify that the output recieved resembles**

#this is a text format

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ret = []

        save = list.copy(nums)

        for i in range(0,len(nums)):

            save.pop(i)

            if((target-nums[i]) in save):

                ret.append(i)

            save = list.copy(nums)

          

        return ret