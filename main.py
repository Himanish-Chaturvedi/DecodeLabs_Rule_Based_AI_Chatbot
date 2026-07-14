# -------------------------------------------------------
# Rule-Based AI Chatbot
# Developed by: Himanish Chaturvedi
# Internship: DecodeLabs AI Internship
# -------------------------------------------------------

from responses import responses

# Displays the welcome banner
def welcome():
    print("=" * 55)
    print("🤖          RULE-BASED AI CHATBOT")
    print("Type 'help' to see available commands.")
    print("Type 'bye' to exit.")
    print("=" * 55)
    print("=" * 55)
    

# Displays all supported commands
def show_help():
    print("🤖 Chatbot: Here are some commands you can use:")
    for command in responses.keys():
        print(f"- {command}")

# Displays the goodbye message
def goodbye():
    print("🤖 Chatbot: Goodbye!, have a glorious day!")


welcome()

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "help":
        show_help()
        continue

    if user_input in ("exit", "bye"):
        goodbye()
        break

    response = responses.get(user_input, "Sorry, I don't know about that yet.\nType 'help' to see the available commands.")
    print(f"🤖 Chatbot: {response}")