import json
from difflib import SequenceMatcher


class RuleEngine:
    """
    A comprehensive inference engine for evaluating rules, providing suggestions, and handling dynamic rule extensions.
    """

    def __init__(self, rule_file):
        """
        Initializes the RuleEngine with a JSON-based rule file.

        Args:
            rule_file (str): Path to the JSON file containing rules.
        """
        self.rule_file = rule_file
        self.rules = self.load_rules()

    def load_rules(self):
        """
        Load rules from the rule file.

        Returns:
            list: List of rules loaded from the JSON file.
        """
        try:
            with open(self.rule_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print(
                f"Error: {self.rule_file} not found. Starting with an empty rule set.")
            return []
        except Exception as e:
            print(f"Error loading rules: {e}")
            return []

    def save_rules(self):
        """
        Save the current rules back to the rule file.
        """
        try:
            with open(self.rule_file, "w") as f:
                json.dump(self.rules, f, indent=4)
        except Exception as e:
            print(f"Error saving rules: {e}")

    def validate_rule(self, new_rule):
        """
        Validate a new rule before adding it to the knowledge base.

        Args:
            new_rule (dict): The rule to validate.

        Returns:
            bool: True if the rule is valid, False otherwise.
        """
        if "if" not in new_rule or "then" not in new_rule:
            return False  # Rule must contain 'if' and 'then' keys
        if not isinstance(new_rule["if"], dict) or not isinstance(new_rule["then"], str):
            return False  # 'if' must be a dictionary and 'then' must be a string
        return True

    def add_rule(self, new_rule):
        """
        Add a new rule to the knowledge base after validation.

        Args:
            new_rule (dict): The rule to add.

        Returns:
            str: Success or error message.
        """
        if not self.validate_rule(new_rule):
            return "Invalid rule format. Rule must contain 'if' (dict) and 'then' (str)."

        self.rules.append(new_rule)
        self.save_rules()
        return "Rule successfully added to the knowledge base."

    def exact_match(self, criteria):
        """
        Find an exact match for the given criteria in the rules.

        Args:
            criteria (dict): The input conditions to evaluate.

        Returns:
            str: The conclusion or recommendation if an exact match is found.
        """
        for rule in self.rules:
            if all(criteria.get(key) == value for key, value in rule["if"].items()):
                return rule["then"]
        return None

    def score_rule(self, criteria, rule_conditions):
        """
        Calculate a match score for a rule based on the number of matching conditions.

        Args:
            criteria (dict): The input conditions.
            rule_conditions (dict): The conditions of the rule to evaluate.

        Returns:
            int: The score representing the number of matching conditions.
        """
        return sum(1 for key, value in rule_conditions.items() if criteria.get(key) == value)

    def find_closest_match(self, criteria):
        """
        Suggest the rule with the highest match score when no exact match is found.

        Args:
            criteria (dict): The input conditions to evaluate.

        Returns:
            tuple: (suggested_rule, match_score)
        """
        best_match = None
        highest_score = 0

        for rule in self.rules:
            score = self.score_rule(criteria, rule["if"])
            if score > highest_score:
                highest_score = score
                best_match = rule

        if best_match:
            return best_match["then"], highest_score
        return "No close matches found.", 0

    def evaluate(self, criteria):
        """
        Evaluate the given criteria against the rules, prioritizing exact matches.

        Args:
            criteria (dict): The input conditions to evaluate.

        Returns:
            dict: The evaluation result, including suggestions if no exact match is found.
        """
        result = {
            "exact_match": None,
            "suggestion": None,
            "match_score": 0
        }

        # Check for exact match
        result["exact_match"] = self.exact_match(criteria)
        if result["exact_match"]:
            return result

        # If no exact match, find the closest match
        suggestion, score = self.find_closest_match(criteria)
        result["suggestion"] = suggestion
        result["match_score"] = score

        return result

    def similarity_ratio(self, str1, str2):
        """
        Calculate the similarity ratio between two strings using SequenceMatcher.

        Args:
            str1 (str): First string.
            str2 (str): Second string.

        Returns:
            float: Similarity ratio (0.0 to 1.0).
        """
        return SequenceMatcher(None, str1, str2).ratio()

    def suggest_improvements(self, criteria):
        """
        Suggest possible improvements to the input criteria by identifying common mismatches.

        Args:
            criteria (dict): The input conditions to evaluate.

        Returns:
            list: List of suggestions to improve the criteria.
        """
        suggestions = []
        for rule in self.rules:
            mismatched_keys = [
                key for key, value in rule["if"].items()
                if key in criteria and criteria[key] != value
            ]
            if mismatched_keys:
                suggestions.append({
                    "rule": rule["then"],
                    "mismatched_keys": mismatched_keys,
                    "correct_values": {key: rule["if"][key] for key in mismatched_keys}
                })
        return suggestions


# Example Usage
if __name__ == "__main__":
    # Create engines for each context
    inventory_engine = RuleEngine("knowledge_base/inventory_rules.json")
    logistic_engine = RuleEngine("knowledge_base/logistic_rules.json")
    diagnostic_engine = RuleEngine("knowledge_base/diagnostic_rules.json")

    # Define criteria for testing
    user_criteria_inventory = {
        "demand_forecast": "high",
        "stock_level": "low",
        "lead_time": "short"
    }

    user_criteria_logistics = {
        "distance": "short",
        "load": "light",
        "carrier_availability": "high",
        "cost": "low"
    }

    user_criteria_diagnostics = {
        "issue": "inventory shortage",
        "cause": "unexpected demand",
        "response_time": "slow"
    }

    # Evaluate Inventory
    inventory_result = inventory_engine.evaluate(user_criteria_inventory)
    print("Inventory Evaluation:", inventory_result)

    # Evaluate Logistics
    logistics_result = logistic_engine.evaluate(user_criteria_logistics)
    print("Logistics Evaluation:", logistics_result)

    # Evaluate Diagnostics
    diagnostic_result = diagnostic_engine.evaluate(user_criteria_diagnostics)
    print("Diagnostics Evaluation:", diagnostic_result)
