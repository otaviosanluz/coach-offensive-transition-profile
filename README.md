# Coach Offensive Transition Models

## Objective
Build interpretable models to explain and compare coaches’ offensive transition behaviour across leagues and seasons.

This project focuses on behavioural modelling, not generative AI.

---

## Research Question
How do football coaches differ in their offensive transition behaviour?

---

## Scope
- **Unit of analysis:** Coach  
- **Game phase:** Offensive transition  
- **Context:** Multi-league, multi-season  
- **Approach:** Comparative and model-based  

Offensive transition is analysed as a full game phase.

---

## Methodology

### Data
- Event and match-level football data (non-public)
- Accessed locally via configurable paths

### Feature Engineering
Models are built using features describing:
- Transition speed
- Verticality
- Risk-taking
- Spatial progression
- Efficiency

### Models
- Interpretable statistical models
- Behavioural scores per coach
- Clustering to identify offensive transition styles

---

## Outputs
The project produces model-based explanations, such as:
- Coach rankings by offensive transition behaviour
- Offensive transition style archetypes
- Structured comparisons across leagues

Outputs are stored as readable artifacts, not raw datasets.

---

## Repository Structure

```
coach-offensive-transition-profile/
├── src/
├── data/
│   └── sample/
├── outputs/
├── main.py
└── README.md
```

