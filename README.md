# gemini-long-context-eval


# Gemini CLI Evaluation Toolkit

## Overview

This project is a developer-focused evaluation toolkit designed to test Large Language Models (LLMs) on long-context reasoning and real-world coding tasks.

Unlike traditional dataset-only approaches, this toolkit provides a **CLI-based evaluation system** that simulates real developer workflows and enables structured testing of model performance.

---

 Key Features

*  Structured dataset for long-context reasoning tasks
*  Multi-step reasoning evaluation
*  CLI-based execution
*  Automated scoring system
*  Context simulation:

  * Partial context (limited information)
  * Full context (complete information)
*  Report generation (`report.txt`)

---

 Project Structure

```
gemini-long-context-eval/
│
├── dataset/
│   ├── tasks.json
│   └── research_tasks.json
│
├── evaluator/
│   └── evaluator.py
│
├── report.txt
└── README.md
```

---

 Usage

 Run Evaluation

```bash
python evaluator/evaluator.py --task dataset/tasks.json --mode full
```

Modes

* `--mode full` → Shows complete context
* `--mode partial` → Simulates limited context

---

 Example Output

```
Task 1
Bug: Token not expiring
Context: User sessions remain active indefinitely
Model Output: Missing expiration check

✅ Correct

Final Score: 1/2
```

---

 Dataset Format

Each task includes:

* Files involved
* Bug description
* Context
* Expected output
* Difficulty level

---

 Motivation

This project is built as part of preparation for contributing to **Gemini CLI evaluation systems** in GSoC.

The goal is to create a **practical, developer-friendly alternative** to traditional evaluation pipelines.

---

 Future Improvements

* Accuracy percentage and advanced metrics
* Integration with Gemini CLI
* Automated LLM evaluation (no manual input)
* Difficulty-wise performance analysis

---

 Contribution

Feel free to fork and extend this toolkit with new datasets, evaluation metrics, or integrations.

---

 Acknowledgment

Inspired by real-world challenges in evaluating long-context reasoning and multi-file code understanding in LLM systems.
