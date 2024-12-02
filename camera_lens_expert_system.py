import json

# Load the knowledge base from JSON


def load_knowledge_base(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Evaluate rules based on input conditions


def evaluate_rules(conditions, knowledge_base):
    rules = knowledge_base["rules"]
    applicable_rules = []

    for rule in rules:
        match = True
        for key, value in rule["conditions"].items():
            if key in conditions:
                if isinstance(value, list):  # For range checks
                    if not (value[0] <= conditions[key] <= value[1]):
                        match = False
                        break
                elif conditions[key] != value:
                    match = False
                    break
        if match:
            applicable_rules.append(rule)

    return applicable_rules

# Display results of rule evaluation


def display_recommendations(applicable_rules, knowledge_base):
    materials = {
        material["id"]: material for material in knowledge_base["materials"]}
    lens_types = {lens["id"]: lens for lens in knowledge_base["lens_types"]}
    processes = {
        process["id"]: process for process in knowledge_base["manufacturing_processes"]}

    for rule in applicable_rules:
        print("\n--- Recommendation ---")
        print(f"Rule ID: {rule['id']}")

        # Lens Type
        lens_type_id = rule["actions"]["lens_type"]
        lens = lens_types[lens_type_id]
        print(f"Lens Type: {lens['name']}")
        print(f"Advantages: {', '.join(lens['advantages'])}")
        print(f"Disadvantages: {', '.join(lens['disadvantages'])}")

        # Material
        material_id = rule["actions"]["material"]
        material = materials[material_id]
        print(f"Material: {material['name']}")
        print(f"Refractive Index: {material['refractive_index']}")
        print(f"Applications: {', '.join(material['applications'])}")

        # Manufacturing Process
        process_id = rule["actions"]["manufacturing_process"]
        process = processes[process_id]
        print(f"Manufacturing Process: {process['name']}")
        print(f"Description: {process['description']}")
        print(f"Tolerance: {process['tolerance']}mm")
        print("----------------------")

# Main function to run the expert system


def main():
    knowledge_base = load_knowledge_base("./knowledge_base.json")

    print("Camera Lens Expert System")
    print("=========================")

    # Get input conditions from the user
    conditions = {}
    conditions["application"] = input(
        "Enter application (e.g., photography, telescopes, smartphones): ").strip().lower()

    focal_length = input(
        "Enter focal length in mm (leave blank if unknown): ").strip()
    if focal_length:
        conditions["focal_length_range"] = float(focal_length)

    budget = input(
        "Enter budget (low, medium, high) (leave blank if unknown): ").strip().lower()
    if budget:
        conditions["budget"] = budget

    # Evaluate rules based on conditions
    applicable_rules = evaluate_rules(conditions, knowledge_base)

    if applicable_rules:
        display_recommendations(applicable_rules, knowledge_base)
    else:
        print("\nNo matching recommendations found for the given conditions.")


# Run the program
if __name__ == "__main__":
    main()
