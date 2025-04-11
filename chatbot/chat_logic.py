import json
from config import openai, MODEL, system_message
from price_data import get_ticket_price
from tools import tools

def handle_tool_call(tool_call):
    args = json.loads(tool_call.function.arguments)
    origin = args.get("origin_city", "")
    destination = args.get("destination_city", "")
    price = get_ticket_price(origin, destination)
    
    return {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": f"The return ticket from {origin.title()} to {destination.title()} is {price}."
    }

def chat(user_message, history):
    messages = [{"role": "system", "content": system_message}]

    # Ensure that history is structured properly
    if history:
        for pair in history:
            # Check if the history contains tuples of two elements
            if len(pair) == 2:
                messages.append({"role": "user", "content": pair[0]})
                messages.append({"role": "assistant", "content": pair[1]})
            else:
                print("Invalid history format:", pair)  # Debug log if history format is wrong

    messages.append({"role": "user", "content": user_message})

    response = openai.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    if response.choices[0].finish_reason == "tool_calls":
        tool_response = handle_tool_call(message.tool_calls[0])
        messages.append(message)
        messages.append(tool_response)
        response = openai.chat.completions.create(model=MODEL, messages=messages)

    return response.choices[0].message.content

