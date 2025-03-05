from google.genai import types
from setup_gemini import setup_gemini, ROLE_USER, generate_content, ROLE_MODEL
from json_loader import load_prompt_from_json

client = setup_gemini()


def start_chat(instruction, history=None):
    if history is None:
        history = []
    config = types.GenerateContentConfig(system_instruction=instruction)
    chat = client.chats.create(model="gemini-2.0-flash", config=config, history=history)
    return chat


def display_chat(message, instruction, history=None):
    chat = start_chat(instruction, history)
    response = chat.send_message_stream(message)
    for chunk in response:
        print(chunk.text, end="")


def first():
    system_instruction = types.Part.from_text(text="You are an assistant that speaks like Shakespeare.")
    user_message_0 = generate_content(ROLE_USER, "tell me a joke.")
    model_message_0 = generate_content(ROLE_MODEL, "Why did the chicken cross the road?")
    # user_message_1 = generate_content(ROLE_USER, "I don't know")
    history = [user_message_0, model_message_0]
    display_chat("I don't know", system_instruction, history)


def infer_from_context():
    system_instruction = types.Part.from_text(text="You are friendly chatbot.")
    user_message_0 = generate_content(ROLE_USER, "Hi, my name is Isa")
    model_message_0 = generate_content(ROLE_MODEL,
                                       "Hi Isa! It's nice to meet you. Is there anything I can help you with today?")
    history = [user_message_0, model_message_0]
    display_chat("use my name to compose a poetry", system_instruction, history)


def input_from_terminal():
    name = input("Enter your name.")
    print("Hello, {}".format(name))


def show_conversation(chat, message):
        response = chat.send_message(message)
        print(f"Assistant: {response.text}", end="")

def order_bot():
    exit_terms = ["exit", "quit", "bye"]
    prompt = load_prompt_from_json("./chat_bot.json", "order_bot")
    system_instruction = prompt.get("system_instruction")
    chat = start_chat(system_instruction)

    show_conversation(chat, "Hello!")

    while True:
        user_input = input("You: ")
        show_conversation(chat, user_input)
        if user_input.lower() in exit_terms:
            print("Good bye!")
            break

    summary_prompt = prompt.get("summary_order")
    show_conversation(chat, summary_prompt)