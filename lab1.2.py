class HealthcareDiagnosticsAgent:
    def __init__(self):
        self.conditions = {
            "Common Cold": ["cough", "sneezing", "runny nose", "sore throat"],
            "Flu": ["fever", "chills", "muscle aches", "cough", "fatigue"],
            "Diabetes": ["increased thirst", "frequent urination", "fatigue", "blurred vision"],
            "Hypertension": ["headache", "dizziness", "shortness of breath", "chest pain"],
            "COVID-19": ["fever", "dry cough", "loss of taste", "shortness of breath", "fatigue"],
        }

    def sense_input(self):
        print("Enter the symptoms (separated by commas): ")
        user_input = input()  # Get symptoms from the user
        self.symptoms = [symptom.strip().lower() for symptom in user_input.split(",")]
        return self.symptoms

    def match_conditions(self):
        matches = {}
        for condition, condition_symptoms in self.conditions.items():
            match_count = len(set(self.symptoms) & set(map(str.lower, condition_symptoms)))
            if match_count > 0:
                matches[condition] = match_count
        sorted_matches = sorted(matches.items(), key=lambda x: x[1], reverse=True)
        return sorted_matches

    def suggest_diagnosis(self, sorted_matches):
        if not sorted_matches:
            print("\nDiagnosis: No condition matches the given symptoms. Please consult a doctor.")
        else:
            print("\nPossible Diagnoses (in order of likelihood):")
            for condition, match_count in sorted_matches:
                print(f"- {condition} ({match_count} symptom match)")
    def run(self):
        self.sense_input()
        sorted_matches = self.match_conditions()
        self.suggest_diagnosis(sorted_matches)
agent = HealthcareDiagnosticsAgent()
agent.run()
