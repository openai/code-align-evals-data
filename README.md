# code-align-evals-data

# Repo structure
Datasets

human_eval: Contains original 164 human-written tasks for evaluating capabilities performance. 

bad_solutions: buggy solutions to the first 30 human_eval tasks. These can be put in the context of an eval task and we can measure the decrease in performance

alignment: eval tasks testing alignment

- bad_contexts: human eval tasks with buggy solutions in the contex

- instruction_following: tasks that ask the model to follow instructions to write particular code

- invalid_use: Eval tasks testing misuse. The model should refuse to generate code for these use cases

robustness: Eval tasks that are more testing robustness than alignment

