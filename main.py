from logger import log_interaction
from ai_client import get_ai_response

def main():
    print("CLI AI Helper")
    print("Type 'exit' to quit")

    while True:
        user_input = input(">> ")

        if user_input.lower() == "exit":
            print("Goodbye.")
            break

        try:
            answer = get_ai_response(user_input)
            print(answer)
            log_interaction(user_input, answer)

        except Exception as e:
            print("Something went wrong:", str(e))


if __name__ == "__main__":
    main()
