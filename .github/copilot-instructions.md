# Copilot Instructions for aws_python

## Project Overview
This repository contains Python scripts organized by topic, likely for educational or demonstration purposes. Key folders include:
- `conditional/`: Examples of conditional logic
- `data_types/`: Scripts demonstrating Python data types and loops
- `functions/`: Function usage and examples

## Key Patterns and Conventions
- Each script is self-contained and demonstrates a specific Python concept (e.g., conditionals, loops, functions).
- Variable and function names are descriptive and match the concept being demonstrated (e.g., `demo`, `buy_score`).
- Input/output is often handled via `input()` and `print()` for interactive examples.
- Scripts do not rely on external dependencies or packages.
- No centralized entry point; each file can be run independently.

## Developer Workflows
- **Run any script:**
  ```
  python <filename>.py
  ```
- No build or test automation is present; manual execution is the norm.
- No external requirements (no `requirements.txt` or package management).

## Project-Specific Guidance
- When adding new examples, place them in the appropriate topic folder and use clear, educational naming.
- Avoid introducing external dependencies unless absolutely necessary for the example.
- Keep code readable and focused on the concept being demonstrated.
- If you add a new topic, create a new folder at the root level.

## Example: Adding a New Function Example
Place a new file in `functions/`:
```python
# functions/new_example.py
def add(a, b):
    return a + b
print(add(2, 3))
```

## Integration Points
- No cross-file imports or shared modules; all scripts are standalone.
- No external service integration.

## Reference Files
- See `conditional/`, `data_types/`, and `functions/` for canonical examples of project structure and style.

---
For more, see https://aka.ms/vscode-instructions-docs
