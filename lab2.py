import random

class TravelItineraryPlanner:
    def __init__(self, destinations, activities, budget, duration):
        self.destinations = destinations
        self.activities = activities
        self.budget = budget
        self.duration = duration
        self.itineraries = self.generate_itineraries()
    
    def generate_itineraries(self):
        itineraries = []
        for destination in self.destinations:
            itinerary = {
                "destination": destination,
                "activities": random.sample(self.activities, random.randint(1, len(self.activities))),
                "cost": random.randint(1000, 5000),
                "duration": random.randint(3, 10)
            }
            itineraries.append(itinerary)
        return itineraries
    def calculate_utility(self, itinerary):
        destination_score = 10 if itinerary["destination"] in user_preferences["preferred_destinations"] else 5
        activity_match = len(set(itinerary["activities"]) & set(user_preferences["preferred_activities"]))
        budget_penalty = max(0, (itinerary["cost"] - self.budget) // 100)
        duration_score = 10 if itinerary["duration"] <= self.duration else 5
        utility_score = (2 * destination_score) + (3 * activity_match) - budget_penalty + duration_score
        return utility_score
    
    def recommend_itinerary(self):
        scored_itineraries = [(itinerary, self.calculate_utility(itinerary)) for itinerary in self.itineraries]
        best_itinerary = max(scored_itineraries, key=lambda x: x[1])
        print("\n### Recommended Itinerary ###")
        self.display_itinerary(best_itinerary[0], best_itinerary[1])
    def display_itinerary(self, itinerary, utility_score):
        print(f"Destination: {itinerary['destination']}")
        print(f"Activities: {', '.join(itinerary['activities'])}")
        print(f"Cost: ${itinerary['cost']}")
        print(f"Duration: {itinerary['duration']} days")
        print(f"Utility Score: {utility_score}")
    def run(self):
        for itinerary in self.itineraries:
            score = self.calculate_utility(itinerary)
            self.display_itinerary(itinerary, score)
            print("-" * 40)
        self.recommend_itinerary()
user_preferences = {
    "preferred_destinations": ["Paris", "Rome", "Tokyo"],
    "preferred_activities": ["Sightseeing", "Food Tour", "Museum Visit"],
}
planner = TravelItineraryPlanner(
    destinations=["Paris", "Rome", "Tokyo", "London", "New York"],
    activities=["Sightseeing", "Food Tour", "Museum Visit", "Hiking", "Shopping"],
    budget=3000,
    duration=5
)
planner.run()
