# Probabilistic Finite-State Automaton (PFSA) Auto-Complete and Word Generator

## Introduction

This project involves creating a Probabilistic Finite-State Automaton (PFSA) for letter-level auto-completion and random word generation based on a given text corpus containing valid English words. The PFSA will allow for predictive text suggestions and the generation of words according to the distribution of words in the corpus.

## Features

### 1. PFSA Creation

- States will represent letter sequences.
- Transitions will be positively weighted and directed, adhering to probability axioms.
- The PFSA will not contain dead states.
- Mark words in the corpus with "*" to distinguish prefixes from valid English words.

### 2. Auto-Complete

- The PFSA will predict and suggest possible word completions as users type.

### 3. Word Generation

- The PFSA will be used to generate random words based on the distribution in the corpus.

## Implementation

### Rules for PFSA

#### States

- States represent letter sequences and have no dead states.
- Distinguish between prefixes and valid English words by marking words in the corpus with "*."

#### Transitions

- Transitions are positively weighted and directed.
- The sum of outgoing probabilities from each state adds up to one.

### Example

Assume a corpus contains words: "Auto," "Automata," and "Automate." The PFSA will contain all prefixes of these words with transition probabilities.

### I/O Format

The provided boilerplate code handles most of the I/O operations.

### JSON Format

A JSON format is used to represent the PFSA. Example JSON:

```json
{
  "*": {
    "A": "1.0"
  },
  "A": {
    "Au": "1.0"
  },
  "Auto": {
    "Auto*": "0.33",
    "Autom": "0.67"
  }
}
