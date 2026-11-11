
import os


class Quiz:
    def __init__(self, question, choices, answer, explanation):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.explanation = explanation

    def show_question(self):
        print(self.question)

        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer


# 기본 퀴즈 데이터
quizzes = [
    Quiz(
        "Python에서 화면에 글자를 출력할 때 사용하는 함수는?",
        ["echo()", "console.log()", "print()", "write()"],
        3,
        "print() 함수는 화면에 값을 출력할 때 사용합니다."
    ),
    Quiz(
        "Python에서 사용자 입력을 받을 때 사용하는 함수는?",
        ["scan()", "input()", "read()", "get()"],
        2,
        "input() 함수는 사용자가 입력한 값을 문자열로 받습니다."
    ),
    Quiz(
        "Python에서 문자열의 길이를 구할 때 사용하는 함수는?",
        ["count()", "size()", "length()", "len()"],
        4,
        "len() 함수는 문자열, 리스트 등의 길이를 구할 때 사용합니다."
    ),
    Quiz(
        "Python에서 숫자 10을 문자열로 변환할 때 사용하는 코드는?",
        ["str(10)", "string(10)", "toString(10)", "char(10)"],
        1,
        "str() 함수는 숫자나 다른 값을 문자열로 변환할 때 사용합니다."
    ),
    Quiz(
        "Python에서 조건문을 작성할 때 사용하는 키워드는?",
        ["when", "if", "check", "condition"],
        2,
        "if 키워드는 조건에 따라 다른 코드를 실행할 때 사용합니다."
    )
]


# 퀴즈 풀기 기능
def play_quiz():
    if not quizzes:
        print("등록된 퀴즈가 없습니다. 2번으로 퀴즈를 추가해주세요!")
        return

    score = 0

    for index, quiz in enumerate(quizzes, start=1):
        os.system("cls")

        print("=============================")
        print(f"       문제 {index} / {len(quizzes)}")
        print("=============================")

        quiz.show_question()
        print()

        while True:
            user_input = input("정답을 입력하세요 (1~4): ").strip()

            if user_input == "":
                print("아무것도 입력하지 않았습니다.")

            elif not user_input.isdigit():
                print("숫자를 입력해주세요.")

            elif int(user_input) not in range(1, 5):
                print("1부터 4까지의 숫자만 입력해주세요.")

            else:
                user_answer = int(user_input)
                break

        print()

        if quiz.is_correct(user_answer):
            print("정답입니다!")
            score += 1
        else:
            print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print(f"해설: {quiz.explanation}")

        input("\n다음으로 진행하려면 Enter를 누르세요...")

    os.system("cls")

    print("=============================")
    print("         퀴즈 결과")
    print("=============================")
    print(f"총 문제 수: {len(quizzes)}")
    print(f"맞힌 문제 수: {score}")
    print(f"틀린 문제 수: {len(quizzes) - score}")


# 메인 메뉴
while True:
    os.system("cls")

    print("=============================")
    print("          퀴즈 게임")
    print("=============================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 최고 점수 확인")
    print("5. 종료")
    print()

    choice = input("메뉴를 선택하세요: ").strip()

    if choice == "":
        print("아무것도 입력하지 않았습니다. 다시 선택해주세요.")

    elif not choice.isdigit():
        print("숫자를 입력해주세요.")

    elif choice == "1":
        play_quiz()

    elif choice == "2":
        print("퀴즈 추가 기능은 아직 준비 중입니다.")

    elif choice == "3":
        print("퀴즈 목록 기능은 아직 준비 중입니다.")

    elif choice == "4":
        print("최고 점수 확인 기능은 아직 준비 중입니다.")

    elif choice == "5":
        print("프로그램을 종료합니다.")
        break

    else:
        print("1부터 5까지의 숫자만 입력해주세요.")

    input("\n계속하려면 Enter를 누르세요...")
