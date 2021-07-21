Dataset structure

The jsonl files contain 164x3 examples - three for each task in HumanEval.

{
    "task_id": "3_{type}_solutions_in_context_3_samples/{n}#{entry_point}" # n indicates which of the 3 samples, and entry_point indicates which task. 
    "env_data": {
        "prompt": three pairs of [docstring, implementation] followed by a docstring for the function we're evaluating the model on
        "entry_point": name of the function that we are evaluating the model on,
        "canonical_solution": human-written solution
        "test": human-written code to check whether a solution is correct 
        }
}

One file contains bad solutions (where the implementations in the prompt have subtle bugs), and the other contains good solutions (the implementations in the prompt are correct, human-written solutions) 
