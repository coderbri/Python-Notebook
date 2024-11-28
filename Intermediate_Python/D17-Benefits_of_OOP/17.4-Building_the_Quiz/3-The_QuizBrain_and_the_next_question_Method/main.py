# ✓ TODO 2: Import question_data and Question model files.
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# ✓ TODO 3: Write a for loop to iterate over the question_data.
# There are 12 dicts in the question_data list
for question_dict in question_data:
    question_text = question_dict["text"]
    question_answer = question_dict["answer"]
    # ✓ TODO 4: Create a Question object from each entry in question_data.
    new_question = Question(q_text=question_text, q_answer=question_answer)
    # ✓ TODO 5: Append each Question object to the question_bank.
    question_bank.append(new_question)

# ✓ TODO 11: Import QuizBrain and simulate the question prompt.
quiz = QuizBrain(question_bank)
quiz.next_question()
