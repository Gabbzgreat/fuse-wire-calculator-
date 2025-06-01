# 🔧 Fuse & Wire Calculator

A Python-based GUI tool for calculating the appropriate wire size, fuse rating, and maximum wire length in 12V automotive electrical systems.

## 🚗 Features

- Select between copper or aluminum wires
- Choose circuit type: Charging, Starting, or Other
- Enter current load and get:
  - Recommended wire size (mm²)
  - Maximum permissible wire length (m)
  - Suggested fuse rating (A)
- Built-in safety margin (25%) for fuse selection
- Tkinter-based interface with real-time feedback

## 🧮 Example Calculation

Input:
- Load Current: 15A
- Circuit Type: Other
- Wire Material: Aluminum

Output:
- Wire size: 2.5 mm²  
- Max length: ~5.44 meters  
- Fuse: 25 A

## 💻 How to Run

```bash
python AES.py
