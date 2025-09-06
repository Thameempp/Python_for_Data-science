from question import question

question_prompts = [
    "what color are mango?\n(a) white \n(b) blue  \n(c) yellow\n\n",
    "what color are apple?\n(a) pink \n(b)red  \n(c) orange\n\n",
    "what color are carrot?\n(a) blue \n(b) black \n(c) orange\n\n",
    
]

questions = [  
    question(question_prompts[0], "c"),
    question(question_prompts[1], "b"),
    question(question_prompts[2], "c"),
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            

    print("you got" + str(score)+ "/" + str(len(questions)) + "correct")
     
run_test(questions)