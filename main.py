
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
        ["input()", "print()", "len()", "type()"],
        2,
        "print() 함수는 화면에 값을 출력할 때 사용합니다."
    ),
    Quiz(
        "Python에서 사용자 입력을 받을 때 사용하는 함수는?",
        ["print()", "input()", "int()", "str()"],
        2,
        "input() 함수는 사용자가 입력한 값을 문자열로 받습니다."
    ),
    Quiz(
        "Git에서 현재 변경 상태를 확인하는 명령어는?",
        ["git status", "git add", "git commit", "git push"],
        1,
        "git status는 현재 파일 변경 상태와 스테이징 상태를 확인할 때 사용합니다."
    ),
    Quiz(
        "Git에서 변경된 파일을 스테이징 영역에 추가하는 명령어는?",
        ["git commit", "git add", "git log", "git init"],
        2,
        "git add는 변경된 파일을 커밋하기 전에 스테이징 영역에 올리는 명령어입니다."
    ),
    Quiz(
        "Git에서 커밋을 만들 때 사용하는 명령어는?",
        ["git status", "git add", "git commit", "git branch"],
        3,
        "git commit은 스테이징된 변경 사항을 하나의 기록으로 저장합니다."
    )
]


# 퀴즈 풀기 기능
def play_quiz():
    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
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
