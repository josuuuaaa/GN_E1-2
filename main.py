
import os
import json


# 저장 파일 경로
STATE_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "state.json"
)


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

    # Quiz 객체를 딕셔너리로 변환
    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "explanation": self.explanation
        }

    # 딕셔너리를 Quiz 객체로 변환
    @classmethod
    def from_dict(cls, data):
        if not isinstance(data, dict):
            raise ValueError("퀴즈 데이터 형식이 올바르지 않습니다.")

        question = data["question"]
        choices = data["choices"]
        answer = data["answer"]
        explanation = data["explanation"]

        if (
            not isinstance(question, str)
            or not question.strip()
            or not isinstance(choices, list)
            or len(choices) != 4
            or any(
                not isinstance(choice, str) or not choice.strip()
                for choice in choices
            )
            or type(answer) is not int
            or answer not in range(1, 5)
            or not isinstance(explanation, str)
        ):
            raise ValueError("퀴즈 데이터 값이 올바르지 않습니다.")

        return cls(question, choices, answer, explanation)


# 게임 전체 관리 클래스
class QuizGame:
    def __init__(self):
        # 기본 퀴즈 데이터
        self.quizzes = [
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

        # 최고 점수
        self.best_score = None

        # 저장된 데이터 불러오기
        self.load_state()

    # 퀴즈 데이터 및 최고 점수 불러오기
    def load_state(self):
        if not os.path.exists(STATE_FILE):
            print("저장된 파일이 없어 기본 퀴즈로 시작합니다.")
            return

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("저장 파일 형식이 올바르지 않습니다.")

            # 최고 점수 불러오기
            best_score = data.get("best_score")

            if (
                best_score is not None
                and (type(best_score) is not int or best_score < 0)
            ):
                raise ValueError("최고 점수 데이터가 올바르지 않습니다.")

            # 퀴즈 목록 불러오기
            if "quizzes" in data:
                saved_quizzes = data["quizzes"]

                if not isinstance(saved_quizzes, list):
                    raise ValueError("퀴즈 목록 형식이 올바르지 않습니다.")

                loaded_quizzes = [
                    Quiz.from_dict(quiz_data)
                    for quiz_data in saved_quizzes
                ]

                self.quizzes = loaded_quizzes

            self.best_score = best_score

            print("저장된 데이터를 불러왔습니다.")

        except (
            OSError,
            UnicodeError,
            json.JSONDecodeError,
            KeyError,
            TypeError,
            ValueError
        ) as error:
            print(f"저장된 데이터를 불러오지 못했습니다: {error}")
            print("기본 퀴즈로 시작합니다.")
            # __init__에서 설정한 기본 퀴즈와 최고 점수를 유지

    # 퀴즈 데이터 및 최고 점수 저장하기
    def save_state(self):
        data = {
            "quizzes": [
                quiz.to_dict()
                for quiz in self.quizzes
            ],
            "best_score": self.best_score
        }

        # 임시 파일에 먼저 저장
        temp_file = STATE_FILE + ".tmp"

        try:
            with open(temp_file, "w", encoding="utf-8") as file:
                json.dump(
                    data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )

            # 저장 완료 후 기존 파일 교체
            os.replace(temp_file, STATE_FILE)

            return True

        except (OSError, UnicodeError, TypeError, ValueError) as error:
            print(f"데이터 저장 중 오류가 발생했습니다: {error}")

            try:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            except OSError:
                pass

            return False

    # 최고 점수 확인 기능
    def show_best_score(self):
        os.system("cls")

        print("=============================")
        print("         최고 점수")
        print("=============================")

        if self.best_score is None:
            print("아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"현재 최고 점수: {self.best_score}점")

    # 퀴즈 목록 조회 기능
    def show_quiz_list(self):
        os.system("cls")

        print("=============================")
        print("         퀴즈 목록")
        print("=============================")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"{index}. {quiz.question}")
            print(f"   보기 개수: {len(quiz.choices)}개")
            print(f"   정답 번호: {quiz.answer}")
            print()

    # 퀴즈 추가 기능
    def add_quiz(self):
        os.system("cls")

        print("=============================")
        print("         퀴즈 추가")
        print("=============================")

        question = input("문제를 입력하세요: ").strip()

        if question == "":
            print("문제 내용은 비워둘 수 없습니다.")
            return

        choices = []

        for i in range(1, 5):
            choice = input(f"{i}번 보기를 입력하세요: ").strip()

            if choice == "":
                print("보기 내용은 비워둘 수 없습니다.")
                return

            choices.append(choice)

        while True:
            answer_input = input("정답 번호를 입력하세요 (1~4): ").strip()

            if answer_input == "":
                print("정답 번호를 입력해주세요.")

            elif not answer_input.isdigit():
                print("숫자를 입력해주세요.")

            elif int(answer_input) not in range(1, 5):
                print("1부터 4까지의 숫자만 입력해주세요.")

            else:
                answer = int(answer_input)
                break

        explanation = input("해설을 입력하세요: ").strip()

        if explanation == "":
            explanation = "해설이 없습니다."

        new_quiz = Quiz(question, choices, answer, explanation)
        self.quizzes.append(new_quiz)

        # 퀴즈 추가 후 파일 저장
        if self.save_state():
            print("\n퀴즈가 성공적으로 추가 및 저장되었습니다!")
        else:
            print("\n퀴즈는 추가되었지만 파일 저장에 실패했습니다.")

    # 퀴즈 풀기 기능
    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 2번으로 퀴즈를 추가해주세요!")
            return

        score = 0

        for index, quiz in enumerate(self.quizzes, start=1):
            os.system("cls")

            print("=============================")
            print(f"       문제 {index} / {len(self.quizzes)}")
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
        print(f"총 문제 수: {len(self.quizzes)}")
        print(f"맞힌 문제 수: {score}")
        print(f"틀린 문제 수: {len(self.quizzes) - score}")

        # 최고 점수 비교 및 갱신
        if self.best_score is None or score > self.best_score:
            self.best_score = score

            # 최고 점수 갱신 후 파일 저장
            if self.save_state():
                print("\n새로운 최고 점수를 달성했습니다!")
            else:
                print("\n최고 점수가 갱신되었지만 저장에 실패했습니다.")

        print(f"최고 점수: {self.best_score}점")

    # 메뉴 표시 기능
    def show_menu(self):
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

    # 게임 실행 기능
    def run(self):
        while True:
            self.show_menu()

            choice = input("메뉴를 선택하세요: ").strip()

            if choice == "":
                print("아무것도 입력하지 않았습니다. 다시 선택해주세요.")

            elif not choice.isdigit():
                print("숫자를 입력해주세요.")

            elif choice == "1":
                self.play_quiz()

            elif choice == "2":
                self.add_quiz()

            elif choice == "3":
                self.show_quiz_list()

            elif choice == "4":
                self.show_best_score()

            elif choice == "5":
                print("프로그램을 종료합니다.")
                break

            else:
                print("1부터 5까지의 숫자만 입력해주세요.")

            input("\n계속하려면 Enter를 누르세요...")


# 프로그램 시작
if __name__ == "__main__":
    game = QuizGame()
    game.run()
