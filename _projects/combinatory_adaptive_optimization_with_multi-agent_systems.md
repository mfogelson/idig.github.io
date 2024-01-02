---
title: Combinatory Adaptive Optimization With Multi-agent Systems
description: 

people:
  - Lindsay

layout: project
# image: <image>.jpg
# last-updated: <date>
status: inactive

---
Optimization problems are a critical element of engineering design and problem solving, and many approaches have been developed to solve them. Often, a single approach (i.e. an algorithm) is not suffcient to ﬁnd the optimal solution. Instead, an optimizing solution should adapt to the characteristics of the problem and the evolving solution state to best search the optimization space. Previous research has indicated that diversity, dynamism, and cooperation in optimization approaches can improve solution quality. Few approaches, however, have simultaneously exploited all three of these characteristics. In this project, two novel optimization approaches are developed to ﬁll this research gap.

The ﬁrst approach developed as part of this research is entitled Evolutionary Multi- Agent Systems (EMAS). In this approach, a team of autonomous software agents, each representing a different optimization algorithm, cooperate by sharing solutions with one another. Agents are evaluated based on their performance (i.e. the quality of their generated solutions), and genetic operators are used to replace agents with poor performance with the offspring of agents with better performance. The EMAS approach is applied to the traveling salesman problem, numerical optimization problems, and three-dimensional packing problems. It is found that the evolutionary component of EMAS improves the solution quality by up to 30% over non-evolving approaches and that the cooperative component improves solution quality by up to 40% over non-cooperative approaches.

The second approach developed as part of this research, entitled Protocol-based 
Multi-Agent Systems (PMAS), builds on EMAS by decomposing each algorithm into its protocols for generating and selecting solutions. Agents in PMAS represent these protocols, rather than full algorithms. As a result, the same solution quality reached by EMAS can also be reached in PMAS - but in a fraction of the time. Using  PMAS as a platform, the eﬀects of diversity, dynamism, and cooperation on solution quality and computational expense are examined for the one-max problem and for a three-dimensional packing problem. The resulting data indicate that traditional optimization algorithms’ solution quality is inferior to that of the heterogeneous, dynamic, and cooperative PMAS.