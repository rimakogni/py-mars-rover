# Mars Rover 🚀

> **Note**: This is a Python implementation of the classic Mars Rover problem. It processes string input, controls rovers on a grid plateau, and avoids collisions.

## **✨ Project Overview**

This project simulates rovers landing on Mars and navigating a plateau grid.

* **Rotate left or right**
* **Move forward**
* **Check plateau boundaries**
* **Avoid collisions**

Architecture separates:

* **Domain Models** (data classes and enums)
* **Input Parsers**
* **Logic Layer** (movement, collisions, mission control)
* **Integration Layer** (`main.py` entry point)

## 📂 **Project Structure**

```
py-mars-rover/
│
├── src/
│   ├── logic/
│   ├── parsers/
│   ├── utils/
│   └── main.py
│
├── test/
└── README.md
```

## 🛠️ **How to Run**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/py-mars-rover.git
   cd py-mars-rover
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the program:**

   ```bash
   python src/main.py
   ```

> \[!TIP]
> The default input is:
>
> ```
> Plateau size: 5 5
> Rover position: 1 2 N
> Instructions: LMLMMLLMMMR
> ```
>
> The expected output:
>
> ```
> Rover final position: 0 3 E
> ```

## ✅ **How to Run Tests**

Run all tests using:

```bash
pytest
```

## 👩‍💻 **Developer Notes**

* Entry point: `src/main.py`
* Rover logic: `src/logic/rover.py`
* Parsers:

  * `PlateauParser`
  * `PositionParser`
  * `InstructionParser`
* Customize inputs:

  * Modify `main()`
  * Or use `MissionControl` directly

## 📄 **License**

MIT License
