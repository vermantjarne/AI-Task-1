# Imports
from simpleai.search import CspProblem, backtrack
import streamlit as st
import re

# Set title
st.title("Task 1 - Cryptarithmetic Puzzle")

# Request user input
equation = st.text_input("Enter the cryptarithmetic puzzle")

while not re.match(".* . .* . .*", equation):
    ""

# Retrieve individual words and sign
words = equation.split(" ")
first_word = words[0]
second_word = words[2]
result_word = words[4]
sign = words[1]

# Put words into iterative list
words = [first_word, second_word, result_word]

# Define variables
variables = []
for word in words:
    for letter in word:
        if letter not in variables:
            variables.append(letter)

# Retrieve first letter of each word for altered domain
first_letters = []
for word in words:
    first_letter = word[0]
    if first_letter not in first_letters:
        first_letters.append(first_letter)

# Retrieve domains for each variable based on whether the variable is a first letter
domains = {}
for variable in variables:
    if (variable in first_letters):
        domains[variable] = list(range(1, 10))
    else:
        domains[variable] = list(range(0, 10))

# Define unique constraint to remove duplicate values
def constraint_unique(variables, values):
    return len(values) == len(set(values))

# Define add constraint for the formula
def constraint_formula(variables: list, values):
    # Assign value to each letter of each word depending on occurence in variables
    word_values = []
    for word in words:
        word_value = ""
        for letter in word:
            word_value += str(values[variables.index(letter)])
        word_values.append(int(word_value))
    # Return formula depending on sign
    if sign == "+":
        return word_values[0] + word_values[1] == word_values[2]
    if sign == "-":
        return word_values[0] - word_values[1] == word_values[2]
    if sign == "*":
        return word_values[0] * word_values[1] == word_values[2]
    if sign == "/":
        return word_values[0] / word_values[1] == word_values[2]

# Define constraints with variable lists
constraints = [
    (variables, constraint_unique),
    (variables, constraint_formula),
]

# Define and solve problem based on variables, domains and constraints
problem = CspProblem(variables, domains, constraints)
output = backtrack(problem)

# Print solution
st.write('\nSolutions:', output)