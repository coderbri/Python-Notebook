# ✓ TODO 1: Create a Question Class with an init() method with two
#   attributes: text and answer
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

# Testing...
new_q = Question("True or False?", "False")
print(new_q.text)
