---
title: Generative Design Using AI
description: |
  Learning to design from humans: developing visual design agents

people:
  - Ayush 

layout: project
image: img/learningfromhumans1.png
last-updated: 2022-12-19
---

This study explores the potential for synergetic human-agent collaboration in design through a deep learning framework. The framework learns from historical human behavior to create visual representations of future design states, essentially functioning as a visual imitation-based learning system. Trained on videos of humans designing bridges, the framework generates comparable designs without requiring specific design operation data. It then uses a rule-based algorithm to execute these designs. The results indicate that the agent successfully extracts implicit design strategies from human data, showing promise for applications in consecutive decision-making processes. Future work may explore goal-driven environments and hybrid learning approaches to further enhance agent performance.

<!-- Humans as designers have quite versatile problem-solving strategies. Computer agents on the other hand have access to large scale computational resources to solve certain design problems. Hence, if agents can learn from human behavior, a synergetic human-agent problem solving team can be created. This work proposes a visual framework that can imagine future states of design and then figure out what actions to take in order to realize that state. This visual representation allows the functioning to be more interpretable and can enable future human-machine collaborative functioning. The framework uses deep learning constructs that learn from historical human data, how to visually evolve a current design state essentially creating a visual imitation-based learning system. The process can be simply explained as: a deep learning model is shown videos of multiple humans designing bridges without context and is then asked to iteratively design bridges on its own.


Design is an iterative process where humans interact with an environment and need to make multiple sequential decisions to achieve certain objectives. The problem can be decomposed into two steps: perception and problem solving. The human designer perceives the current design state and takes an action to modify it based on previous knowledge and understanding of the problem. This new design then becomes the current design state and the whole process is repeated.The methodology involves training a deep learning framework on historical human design data just by observation. The framework learns to generate designs without any specific design operation information. The generated design is basically a visualization (imagination) of how the new design should look like. Then, that design is fed into a rule-based algorithm that acts as the control system of the agent. Its task is to apply design operations to realize the visualization. A truss design problem is used as the example here.


The comparative results show that the agent learns to create designs that are comparable in performance to human designs from the study. This implies that the agents were able to extract implicit design strategies from data and use them to generate designs. The framework has the ability to learn the relationships between consecutive design states and hence can be applied to consecutive decision-making design processes whose sequential states have incremental changes and can be represented as an N dimensional array.

Learning from historical human data enables the agent identify the important regions of a design space and implicitly learn to navigate it, helping reach good performing designs. For the current study the agents were only trained to imitate humans using metric agnostic design data. In the future, embedding these agents in a goal driven environment where real-time rewards are provided for optimal designs can lead to interesting results. Also, creating hybrid approaches of imitation learning with other methods of active learning can also be explored since it can significantly enhance the agent performance. -->