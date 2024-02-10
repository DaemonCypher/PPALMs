# Class for reordering line tuples and removing comments
class FileFormat:

  def __init__(self, lineList=[], reorderedLines=[]):
    self.fileInput = lineList
    self.reorderedLines = reorderedLines


# Create the line Tuples
# lineList - List of read lines
# linesReordered - List of tuples of line numbers to be kept together

  def reorderLines(self):
    newLineList = []
    linesAdded = []

    # Check if line is empty and return empty array if true
    if self.fileInput == []:
      return []

    # Iterate through each tuple
    for linetuple in self.reorderedLines:
      print(linetuple)
      templist = []
      # Iterate through each index in line tuple
      for line in linetuple:
        # Check if index is in bounds and has not already been added to a tuple
        if line - 1 in range(
            0, len(self.fileInput) + 1) and line - 1 not in linesAdded:

          templist.append(self.fileInput[line - 1])
          linesAdded.append(line - 1)
      # Converts list of lines to be kept together to a tuple and appends to newlineList
      newLineList.append(tuple(templist))
    # Add the rest of the lines that have not been tupled
    for lineNum in range(0, len(self.fileInput)):
      if (lineNum not in linesAdded):
        newLineList.append(self.fileInput[lineNum])
    return newLineList

  # Remove the one line comments from the list of lines
  # lineList - List of read lines
  def removeComments(self):
    for l in reversed(self.fileInput):
      temp = l.replace(" ", "")
      if "#" == temp[0:1]:
        self.fileInput.remove(l)
      if ("//" == temp[0:2]):
        self.fileInput.remove(l)
      if (l.isspace()):
        self.fileInput.remove(l)

    return self.fileInput