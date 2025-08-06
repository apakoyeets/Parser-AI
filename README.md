# Parser-AI
# 🧠 Sentence Parser and Noun Phrase Extractor

This project implements a natural language parser using context-free grammar (CFG) to analyze English sentence structure and extract noun phrase chunks. Built with Python 3.12 and powered by NLTK, this parser is designed as part of CS50’s AI course project.

## 📚 Overview

Parsing helps computers understand sentence structure and meaning. In this project, we:
- Define CFG rules to represent valid sentence structures.
- Parse sentences to construct syntax trees.
- Identify noun phrase chunks — standalone noun phrases that don’t contain nested noun phrases.

## 🚀 Getting Started

### Requirements

- Python 3.12
- NLTK

### Installation

1. Clone this repository:
   ```bash

pip3 install -r requirements.txt
python parser.py
parser/
│
├── sentences/          # Sample sentence files for parsing
├── parser.py           # Main parsing logic and grammar definitions
├── requirements.txt    # NLTK dependency
└── README.md           # Project overview (you're reading this!)


$ python parser.py
Sentence: Holmes sat.
        S
   _____|___
  NP        VP
  |         |
  N         V
  |         |
holmes     sat

Noun Phrase Chunks:
holmes
