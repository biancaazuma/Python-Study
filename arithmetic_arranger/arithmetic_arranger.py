import re

def arithmetic_arranger(problems, showResult=False):

  error = validation(problems)
  if error != None:
    return error

  result = formattingView(problems, showResult)

  return result

def formattingView(problems, showResult):
  firstLine = ""
  secondLine = ""
  thirdLine = ""
  fourthLine = ""
  fourSpaces = "    "

  for problem in problems:

    splittedProblem = problem.split()
    spaces = len(str(max(int(splittedProblem[0]), int(splittedProblem[2]))))
    firstLine += "  " + splittedProblem[0].rjust(spaces, ' ') + fourSpaces

    secondLine += splittedProblem[1] + " " + splittedProblem[2].rjust(
      spaces, ' ') + fourSpaces

    thirdLine += "-".rjust(spaces + 2, '-') + fourSpaces

    result = firstLine.rstrip() + "\n" + secondLine.rstrip(
    ) + "\n" + thirdLine.rstrip()

    if showResult:
      fourthLine += str(eval(problem)).rjust(spaces + 2, ' ') + fourSpaces

      result = result + "\n" + fourthLine.rstrip()
  return result


def validation(problems):
  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:
    splitedProblem = problem.split()

    if splitedProblem[1] not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."

    if re.findall("\D", splitedProblem[0]) or re.findall(
        "\D", splitedProblem[2]):
      return "Error: Numbers must only contain digits."

    if len(splitedProblem[0]) > 4 or len(splitedProblem[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
