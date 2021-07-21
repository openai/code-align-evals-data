# code-align-evals-data

# Repo structure

## Datasets

 **human_eval**: Contains original 158 human-written tasks for evaluating capabilities performance. Each file contains a docstring describing a function, a human-written solution to that task, and human-written code to test whether an implementation is correct

**bad_solutions**: Buggy solutions to the first 30 human_eval tasks. These can be put in the context of an eval task and we can measure the decrease in performance

**alignment**: Eval tasks testing alignment, of four different types:

- **bad_contexts**: Human eval tasks with buggy vs non-buggy solutions in the contex

- **find_bug**: The same human_eval tasks, with an example implementation in the docstring, that contains a single bug. The model is asked to print which line contains the bug. The tests check that the model has output the correct line. 

- **instruction_following**: Tasks that ask the model to follow instructions to write particular code, along with tests to check the instructions have been followed

- **invalid_use**: Tasks testing invalid use. These are examples of tasks where the desired behaviour is for the model to refuse to generate code. The tests check    that the model has not output any code.   

**robustness**: Eval tasks that test robustness more than alignment

