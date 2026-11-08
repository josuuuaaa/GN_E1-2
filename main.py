import os

while True:
    os.system("cls")  # 기존 터미널 화면 지우기

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
        print("퀴즈 풀기 기능은 아직 준비 중입니다.")

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