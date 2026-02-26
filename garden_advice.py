"""
Garden Advice Application
Provides gardening advice based on season and plant type.
Refactored for modularity and readability.
"""

# Dictionary storing seasonal advice
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers."
}

# Dictionary storing plant-specific advice
PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!"
}


def get_season_advice(season):
    """
    Returns gardening advice based on the season.
    """
    return SEASON_ADVICE.get(season, "No advice for this season.")


def get_plant_advice(plant_type):
    """
    Returns gardening advice based on plant type.
    """
    return PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")


def main():
    """
    Main function to run the gardening advice program.
    """
    season = input("Enter the current season (summer/winter): ").lower()
    plant_type = input("Enter the plant type (flower/vegetable): ").lower()

    print("\nGardening Advice:")
    print(get_season_advice(season))
    print(get_plant_advice(plant_type))


if __name__ == "__main__":
    main()