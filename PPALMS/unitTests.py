# Unit Tests for "main.py"
import unittest
from unittest import mock
import builtins
import io
import sys
from main import *
import os


class TestPPALMS(unittest.TestCase):

  # Test case 1 - Open file on various file types
  def test_open_file(self):
    # Folder Path
    path = "test_files"
    os.chdir(path)
    # tests on empty file, .c, .cs, .css, .html, .java, .cpp, .rs, .sql, .py, .txt
    for file in os.listdir():
      inputClass = Input(file)
      inputClass.openFile()
      self.assertNotEqual(inputClass.file, None)

  #Test case 2 - checks removeComments against various file syntaxes
  def test_remove_comments(self):
    # no comments
    fileFormater1 = FileFormat(["a", "b", "c", "d", "e"])
    # hash comments
    fileFormater2 = FileFormat(["a", "b", "#c", "d", "e"])
    # double backslash comments
    fileFormater3 = FileFormat(["a", "b", "c", "d", "//e"])
    # both comment types, comment on every line
    fileFormater4 = FileFormat(["#a", "#b", "#c", "//d", "//e"])
    # multi-line comments (shouldn't change)
    fileFormater5 = FileFormat(["a", "b", "c", "/*d", "e*/"])
    # empty file
    fileFormater6 = FileFormat([])

    self.assertEqual(fileFormater1.removeComments(), ["a", "b", "c", "d", "e"])

    self.assertEqual(fileFormater2.removeComments(), ["a", "b", "d", "e"])

    self.assertEqual(fileFormater3.removeComments(), ["a", "b", "c", "d"])

    self.assertEqual(fileFormater4.removeComments(), [])

    self.assertEqual(fileFormater5.removeComments(),
                     ["a", "b", "c", "/*d", "e*/"])

    self.assertEqual(fileFormater6.removeComments(), [])

  # Test case 3 - checks reorderLines against a normal case
  def test_reorder_lines(self):
    lineArray = ["1", "2", "3", "4", "5"]

    linesReordered1 = [(1, 4)]
    linesReordered2 = [(1, 2, 3, 4, 5)]
    linesReordered3 = []

    fileFormater1 = FileFormat(lineArray, linesReordered1)
    fileFormater2 = FileFormat(lineArray, linesReordered2)
    fileFormater3 = FileFormat(lineArray, linesReordered3)

    expectedOutput1 = [("1", "4"), "2", "3", "5"]
    expectedOutput2 = [("1", "2", "3", "4", "5")]
    expectedOutput3 = ["1", "2", "3", "4", "5"]
    self.assertEqual(expectedOutput1, fileFormater1.reorderLines())
    self.assertEqual(expectedOutput2, fileFormater2.reorderLines())
    self.assertEqual(expectedOutput3, fileFormater3.reorderLines())

  # Test case 4 - checks reorderLines against a blank file
  #output should be blank
  def test_reorder_lines_empty_line_array(self):
    lineArray = []
    linesReordered = [(1, 3)]
    fileFormater = FileFormat(lineArray, linesReordered)

    expectedOutput = []
    self.assertEqual(expectedOutput, fileFormater.reorderLines())

  # Test case 5 - Open file on non-existing/invalid file
  def test_open_file_invalid_file_expect_exception(self):
    file = "invalidfile.txt"
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    inputClass = Input(file)
    with self.assertRaises(SystemExit) as cm:
      inputClass.openFile()
    self.assertEqual(cm.exception.code, 1)
    self.assertEqual('File not in directory.\n', capturedOutput.getvalue())

    pass


if __name__ == '__main__':
  unittest.main()
