PRICE_FUNCTION_SPEC = {
    "name": "get_ticket_price",
    "description": "Get the price of a return ticket from one city to another.",
    "parameters": {
        "type": "object",
        "properties": {
            "origin_city": {
                "type": "string",
                "description": "The city the customer wants to depart from."
            },
            "destination_city": {
                "type": "string",
                "description": "The city the customer wants to travel to."
            }
        },
        "required": ["origin_city", "destination_city"],
        "additionalProperties": False
    }
}

tools = [{"type": "function", "function": PRICE_FUNCTION_SPEC}]
