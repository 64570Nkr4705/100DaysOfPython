from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#creamos una lista vacia
question_bank = []
#recorremos el diccionario question_data
for question in question_data:
    #creamos y asignamos las llaves y los valores a nuestras variables
    question_text = question["text"]
    question_answer = question["answer"]
    '''cramos auna variable para nuevas preguntas y asignamos la clase Question
        y le pasamos las variables creadas anteriormente'''
    new_question = Question(question_text, question_answer)
    #ahora asignamos a nuestro deiccionario vacio las nuevas preguntas
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")