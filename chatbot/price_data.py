from rapidfuzz import process

TICKET_PRICES = {
    "berlin->london": "$499",
    "berlin->paris": "$550",
    "berlin->tokyo": "$1400",
    "paris->tokyo": "$1300",
    "london->berlin": "$475",
}

# Generate list of all cities
KNOWN_CITIES = list({city for route in TICKET_PRICES for city in route.split("->")})

def correct_city_name(input_city: str, score_cutoff: int = 80) -> str:
    match, score, _ = process.extractOne(input_city.lower(), KNOWN_CITIES)
    return match if score >= score_cutoff else input_city.lower()

def get_ticket_price(origin_city: str, destination_city: str) -> str:
    corrected_origin = correct_city_name(origin_city)
    corrected_destination = correct_city_name(destination_city)
    route_key = f"{corrected_origin}->{corrected_destination}"
    return TICKET_PRICES.get(route_key, "Unknown")
