import json
import argparse

def load_dataset(path):
    with open(path, 'r') as f:
        return json.load(f)

def evaluate(predicted, expected):
    return expected.lower() in predicted.lower()

def run_tasks(path, mode):
    tasks = load_dataset(path)   # ✅ FIX: tasks defined here

    score = 0

    for task in tasks:
        print(f"\nTask {task['id']}")

        if mode == "partial":
            print("Bug:", task['bug_description'])
        else:
            print("Bug:", task['bug_description'])
            print("Context:", task.get("context", "No context available"))

        user_input = input("Model Output: ")

        if evaluate(user_input, task["expected_output"]):
            print("✅ Correct")
            score += 1
        else:
            print("❌ Incorrect")

    print(f"\nFinal Score: {score}/{len(tasks)}")

    with open("report.txt", "w") as f:
        f.write(f"Score: {score}/{len(tasks)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", required=True)
    parser.add_argument("--mode", choices=["partial", "full"], default="full")

    args = parser.parse_args()

    run_tasks(args.task, args.mode)   # ✅ FIX: correct call