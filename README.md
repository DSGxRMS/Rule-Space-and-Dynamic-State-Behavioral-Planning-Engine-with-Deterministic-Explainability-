# Rule-Space and Dynamic-State Behavioral Planning Engine with Deterministic Explainability

## Sub-System
**Perception**

## Project Objective

Development and integration of a deterministic, zero-latency behavioral planning vertical for public autonomous driving.

---

# Description

Develop a hierarchical decision-making architecture that separates:

- **Rule Space** (global environmental constraints)
  - Road type
  - Weather
  - Speed regulations

- **Dynamic State** (real-time reactive information)
  - Traffic
  - Pedestrians
  - Traffic signals
  - Obstacles

### Core Tasks

- Build a Finite State Machine (FSM) node in ROS 2 that converts multi-task perception probabilities into discrete behavioral commands.
- Generate high-level behavior outputs such as:
  - `CRUISING`
  - `ADAPTIVE_FOLLOW`
  - `EMERGENCY_STOP`
- Implement a deterministic Translation Matrix for explainable decision making.
- Produce real-time human-readable explanations such as:
  - "Reduce speed due to wet road conditions"
  - "Emergency stop due to pedestrian crossing"
- Engineer a unified data pipeline that standardizes and fuses schemas from:
  - nuScenes
  - BDD100K
  - IDD
- Train and evaluate behavioral logic in complex civil driving environments.

---

# Previously Added Videos

- https://youtu.be/fQ3HJbEkP4U
- https://youtu.be/IBVekrENZy8

---

# Mentors

- Shubh
- Shreyash
- Sushant
- Parth

---

# Resources

1. https://www.youtube.com/watch?v=jFHPEQi55Ko
2. https://www.youtube.com/watch?v=kb-Ww8HaHuE
3. https://www.youtube.com/watch?v=2rP8hyfZfeE

---

# Problem Statement

Generate explainable, high-level behavioral commands (e.g., lane changes, braking, following, emergency stops) based on:

- Overarching environmental constraints (**Rule Space**)
- Dynamic real-time observations (**Dynamic State**)

for safe public autonomous vehicle operation.

---

# Project Overview

Autonomous vehicles operating on public roads require robust behavioral logic to navigate complex and unpredictable environments safely.

While path-planning algorithms determine an optimal trajectory, a dedicated **Decision-Making Layer** determines **what the vehicle should do** before calculating **how it should do it**.

A **Hierarchical Planning Architecture** separates:

## Rule Space

Long-term environmental constraints such as:

- Weather
- Road type
- Speed limits
- Traffic regulations

## Dynamic State

Real-time observations such as:

- Vehicles
- Pedestrians
- Traffic lights
- Obstacles

A Finite State Machine (FSM), driven by multi-task neural-network probabilities, determines the vehicle's behavioral state.

An Explainable AI (XAI) Translation Matrix communicates the reasoning behind every decision.

---

# Objectives

## 1. Dual-Layer Logic Architecture

Develop a system that filters Dynamic State inputs through Rule Space constraints.

### Example

**Input**

- Pedestrian detected
- Wet road

**Output**

- Reduced speed
- Increased braking distance

---

## 2. Finite State Machine (FSM)

Generate discrete behavioral commands:

- `CRUISING`
- `ADAPTIVE_FOLLOW`
- `LANE_CHANGE`
- `STOP`
- `EMERGENCY_STOP`

---

## 3. Explainability Layer

Create a Translation Matrix that maps:

| FSM Action | Trigger | Explanation |
|------------|----------|------------|
| EMERGENCY_STOP | Pedestrian | Emergency stop due to pedestrian crossing |
| CRUISING | Clear road | Maintaining cruise speed |
| ADAPTIVE_FOLLOW | Slow vehicle ahead | Following lead vehicle safely |

---

## 4. ROS 2 Interfaces

Define custom messages:

### PerceptionContext

Contains:

- Weather
- Road type
- Vehicle detections
- Pedestrian detections
- Traffic signal state

### BehaviorCommand

Contains:

- Selected FSM state
- Target speed
- Explanation string

---

## 5. Simulation Integration

Integrate the behavioral controller with the Path Planning stack and evaluate performance in civil driving scenarios.

---

## 6. Validation

Test the complete system in ROS 2 + Gazebo.

---

# Technical Requirements

## Theory

- Behavioral Planning
- Finite State Machines
- Explainable AI (XAI)
- Hierarchical Decision Making

## Programming

- Python
- C++
- ROS 2

## AI / Compute

- PyTorch Lightning
- Kaggle
- Cloud Compute

## Simulation

- ROS 2
- Gazebo

---

# Dataset Sources

The following datasets will be used for training, evaluation, and rule definition.

## Environmental Data

### BDD100K

Used for:

- Weather classification
- Road scene understanding
- Traffic signal detection

---

## Traffic Behavior Data

### IDD

Used for:

- Indian traffic scenarios
- Unstructured road conditions
- Diverse driving behaviors

### Waymo Open Dataset

Used for:

- Vehicle trajectories
- Pedestrian interactions
- Traffic behavior modeling

---

## Simulation Data

### Gazebo ROS Bags

Used for:

- Sensor fusion outputs
- Behavioral testing
- Closed-loop evaluation

---

# Project Timeline (1 Month)

| Week | Deliverable | Tasks |
|--------|-------------|--------|
| Week 1 | Base FSM Node & Custom Interfaces | Define ROS 2 messages (`PerceptionContext`, `BehaviorCommand`) and implement FSM skeleton |
| Week 2 | Constrained Logic Engine | Implement Rule Space constraints and Dynamic State interaction logic |
| Week 3 | Explainability Pipeline & Logging Node | Build Translation Matrix and generate human-readable explanations |
| Week 4 | Integration & Simulation Testing | Integrate with Path Planning and validate across multiple scenarios |

---

# Week-wise Breakdown

## Week 1

### Base FSM Node & Interfaces

Tasks:

- Design ROS 2 custom messages
- Create FSM state definitions
- Build probability-to-state conversion logic

Deliverables:

- FSM node skeleton
- Message definitions

---

## Week 2

### Constrained Logic Engine

Tasks:

- Implement Rule Space constraints
- Define allowable state transitions
- Integrate Dynamic State observations

Deliverables:

- Dual-layer decision engine

---

## Week 3

### Explainability Pipeline

Tasks:

- Develop Translation Matrix
- Build logging node
- Publish explanation strings

Deliverables:

- Explainable decision system

---

## Week 4

### Integration & Validation

Tasks:

- Integrate with Path Planning
- Simulate:
  - Wet roads
  - Pedestrian crossings
  - Vehicle following
  - Emergency situations
- Evaluate behavior accuracy

Deliverables:

- Fully integrated behavioral planning stack

---

# Final Deliverables

## 1. Functional FSM Node

Publishes validated behavioral state commands to the Path Planning vertical.

---

## 2. Dual-Layer Evaluation Engine

Restricts Dynamic State responses according to Rule Space constraints.

---

## 3. Real-Time Explainability Logger

Publishes human-readable reasoning strings such as:

```text
Reduce speed due to wet road conditions
```

```text
Emergency stop due to pedestrian crossing
```

---

## 4. Evaluation Report

Includes:

- Performance across simulation scenarios
- FSM transition accuracy
- Explainability quality metrics
- Failure cases
- Edge-case analysis
- Future improvements

---

# Expected Outcome

A deterministic, explainable behavioral planning system capable of:

- Processing perception outputs
- Applying environmental constraints
- Producing safe behavioral commands
- Explaining every decision in real time
- Operating within ROS 2 autonomous driving stacks

with zero-latency decision generation suitable for public-road autonomous vehicles.
