def build_prompt(technique, task):

    if technique == "Zero-Shot":

        prompt = f"""
You are an expert AI assistant.

Answer the following task directly without using
any examples.

Task:
{task}

Provide a clear, accurate and concise answer.
Use simple language where possible.
"""

    elif technique == "One-Shot":

        prompt = f"""
You are an expert AI assistant.

Use the following single example as a guide for
understanding the expected response style.

Example:

Question:
What is Artificial Intelligence?

Answer:
Artificial Intelligence is a field of computer
science that enables machines to perform tasks
that normally require human intelligence.

Now answer the following task using a similar
style and level of explanation.

Task:
{task}

Provide a clear and accurate answer.
"""
    elif technique == "Few-Shot":

        prompt = f"""
You are an expert AI assistant.

Learn the response pattern from the examples below.

Example 1:

Question:
What is CPU?

Answer:
CPU is the main processing unit of a computer.
It executes instructions and performs calculations.


Example 2:

Question:
What is RAM?

Answer:
RAM is temporary memory used by a computer to
store data while programs are running.


Example 3:

Question:
What is a database?

Answer:
A database is an organized collection of data
that can be stored, managed and retrieved efficiently.


Now answer the following task using the same
clear and structured style.

Task:
{task}

Provide a relevant and accurate answer.
"""

    elif technique == "CoT":

        prompt = f"""
You are an expert problem-solving assistant.

Analyze the following task carefully before
providing the final answer.

Task:
{task}

Use a logical step-by-step approach internally.
Identify the important information, determine
the appropriate method, and arrive at the answer.

Provide a concise explanation of the important
steps followed by the final answer.

Do not reveal hidden or private chain-of-thought.
"""

    elif technique == "Manual CoT":

        prompt = f"""
You are an expert problem-solving assistant.

Solve the following task using the specified
reasoning structure.

Task:
{task}

Follow these steps:

Step 1: Understand the problem.
Step 2: Identify the important information.
Step 3: Select the appropriate method.
Step 4: Apply the method.
Step 5: Verify the result.
Step 6: Provide the final answer.

Give a concise explanation for each relevant step
and then provide the final answer.

Do not reveal hidden or private chain-of-thought.
"""


    elif technique == "ToT":

        prompt = f"""
You are an expert decision-making and
problem-solving assistant.

Use a Tree of Thoughts style approach to solve
the following task.

Task:
{task}

Consider multiple possible approaches.

Approach 1:
Identify and evaluate the first possible solution.

Approach 2:
Identify and evaluate an alternative solution.

Approach 3:
Identify and evaluate another possible solution.

Compare the possible approaches based on
correctness, relevance and practicality.

Select the most suitable approach.

Then provide the final answer with a concise
explanation.

Do not reveal hidden or private chain-of-thought.
"""

    elif technique == "MCOT":

        prompt = f"""
You are an expert AI problem-solving assistant.

Solve the following task using a structured
multi-step reasoning approach.

Task:
{task}

Follow these stages:

1. Understand the task.
2. Identify the important information.
3. Determine the required strategy.
4. Apply the strategy.
5. Check the result.
6. Provide the final answer.

Keep the reasoning summary concise and relevant.

Do not reveal hidden or private chain-of-thought.
"""
    else:

        prompt = f"""
Answer the following task clearly and accurately:

{task}
"""

    return prompt