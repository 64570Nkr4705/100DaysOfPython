class QuizBrain:
    #metodo
    def __init__(self, q_list):
        #atributos
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
    def still_has_questions(self):
        #devolvera V o F 
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        #obtener la pregunta actual
        current_question = self.question_list[self.question_number]
        #cada vez que llamemos a nezt_question debemos incrementar question_number
        self.question_number += 1
        #Vamos a pedir al usuario que ingrese una respuesta
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        #llamamos a nuestro metodo check_answer, le pasamos la respuesta del usuario y la respuesta correcta
        self.check_answer(user_answer, current_question.answer)
    
    #pasamos la respuesta del usuario y la respuesta correcta y la comparamos
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")