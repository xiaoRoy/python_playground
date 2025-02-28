import json
import os

from openai import OpenAI


def hello_world():
    key = os.environ.get("OPENAI_API_KEY")
    client = OpenAI(api_key=key)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative "
                        "flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )
    print(completion.choices[0].message)


def find_product(sql_query):
    # Execute query here
    results = [
        {"name": "pen", "color": "blue", "price": 1.99},
        {"name": "pen", "color": "red", "price": 1.78}, ]
    return results


# hello_world()
def from_text_completion_to_functions():
    user_question = "I need the top 2 products where the price is less than 2.00"
    messages = [{"role": "user", "content": user_question}]
    functions = [
        {
            "name": "find_product",
            "description": "Get a list of products from a sql query",
            "parameters": {
                "type": "object",
                "properties": {
                    "sql_query": {
                        "type": "string",
                        "description": "A SQL query",
                    }},
                "required": ["sql_query"],
            },
        }]

    client = OpenAI(
        api_key=""
    )
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        functions=functions
    )
    response_message = completion.choices[0].message
    print(response_message)
    messages.append(response_message)

    function_args = json.loads(response_message.function_call.arguments)
    products = find_product(function_args.get('sql_query'))
    function_name = 'find_product'
    messages.append(
        {
            "role": "function",
            "name": function_name,
            "content": json.dumps(products),
        })
    completion_second = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        functions=functions
    )
    print(completion_second)


from_text_completion_to_functions()
