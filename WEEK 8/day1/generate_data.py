import json
import random

data = []

# 🔹 QA SECTION (400)


qa_questions = [
    "What is a variable?",
    "What is a function?",
    "Explain loops in Python",
    "What is a list?",
    "Difference between list and tuple",
    "What is OOP?",
    "What is inheritance?",
    "Explain recursion",
    "What is a dictionary in Python?",
    "What is a class?",
    "What is polymorphism?",
    "What is encapsulation?"
]

qa_answers = [
    "A variable is used to store data values.",
    "A function is a reusable block of code.",
    "Loops are used to execute code repeatedly.",
    "A list is a collection of items.",
    "Tuple is immutable while list is mutable.",
    "OOP is a programming paradigm based on objects.",
    "Inheritance allows reuse of code.",
    "Recursion is when a function calls itself.",
    "Dictionary stores key-value pairs.",
    "Class is a blueprint of objects.",
    "Polymorphism allows multiple forms.",
    "Encapsulation hides internal details."
]

qa_pairs = list(zip(qa_questions, qa_answers))

for _ in range(400):
    q, a = random.choice(qa_pairs)

    data.append({
        "instruction": "Answer the coding question clearly",
        "input": q,
        "output": f"{a} This concept is widely used in programming."
    })


# 🔹 REASONING SECTION (400)


for _ in range(400):
    a = random.randint(1, 100)
    b = random.randint(1, 20)
    c = random.randint(1, 10)

    question = f"What is output of {a} + {b} * {c}?"
    answer = f"First multiply {b}*{c}={b*c}, then add {a}+{b*c}={a + b*c}"

    data.append({
        "instruction": "Solve step by step with explanation",
        "input": question,
        "output": answer
    })



# 🔹 EXTRA REASONING (Logic based) (200)


logic_questions = [
    ("If a number is even, what is {} % 2?", "{} % 2 = 0 because number is even"),
    ("If a number is odd, what is {} % 2?", "{} % 2 = 1 because number is odd"),
]

for _ in range(200):
    num = random.randint(1, 100)
    q_template, a_template = random.choice(logic_questions)

    data.append({
        "instruction": "Explain the logic",
        "input": q_template.format(num),
        "output": a_template.format(num)
    })



# 🔹 EXTRACTION SECTION (200)


function_names = [
    "add", "multiply", "compute", "process",
    "calculate", "transform", "update", "handle"
]

templates = [
    "def {}(x): return x+1",
    "def {}(a, b): return a*b",
    "def {}(data): return len(data)",
]

for _ in range(200):
    name = random.choice(function_names) + str(random.randint(1, 999))
    template = random.choice(templates)

    code = template.format(name)

    data.append({
        "instruction": "Extract function name from code",
        "input": code,
        "output": name
    })



# 🔹 NOISE (for cleaning) (50)


for _ in range(50):
    data.append({
        "instruction": "",
        "input": "random text",
        "output": ""
    })


# 🔹 LOW QUALITY SHORT OUTPUTS (10)


bad_responses = ["ok", "yes", "no", "done", "1", "0", "n/a", "none"]

for _ in range(10):
    data.append({
        "instruction": "Answer the question",
        "input": "What is Python?",
        "output": random.choice(bad_responses)
    })


# 🔹 COMPLEX REASONING (100)


for _ in range(100):
    a = random.randint(10, 100)
    b = random.randint(5, 20)
    c = random.randint(2, 10)

    question = f"What is output of {a} + {b} * {c}?"

    answer = (
        f"Step 1: Identify multiplication: {b} * {c} = {b*c}. "
        f"Step 2: Add result to {a}: {a} + {b*c} = {a + b*c}. "
        f"Final Answer: {a + b*c}"
    )

    data.append({
        "instruction": "Solve step by step with detailed explanation",
        "input": question,
        "output": answer
    })


# 🔹 VERY LONG EXPLANATIONS (50)


for _ in range(50):
    data.append({
        "instruction": "Explain in detail",
        "input": "What is a function in Python?",
        "output": (
            "A function in Python is a reusable block of code designed to perform a specific task. "
            "Functions help in modular programming, allowing developers to break complex problems into smaller parts. "
            "They improve readability, maintainability of code. "
        )
    })


# 🔹 VERY SHORT SENTENCES (20)

short_outputs = [
    "It is good",
    "Basic concept",
    "Simple",
    "Used in coding",
    "Important topic"
]

for _ in range(20):
    data.append({
        "instruction": "Explain briefly",
        "input": "What is a loop?",
        "output": random.choice(short_outputs)
    })
    




random.shuffle(data)



with open("data/raw.jsonl", "w") as f:
    for item in data:
        f.write(json.dumps(item) + "\n")

print(f"Dataset created with {len(data)} samples!")