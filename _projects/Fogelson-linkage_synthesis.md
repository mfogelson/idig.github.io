---
title: Generating High-Order Linkage Graphs for Path Synthesis
description: |
  Using Deep RL and Graph Networks for Linkage Design

people:
  - Mitch

layout: project
image: img/block_diagram_revised.png
last-updated: 2023-04-19
status: active

---

One degrees-of-freedom (1DOF) linkages are persistent in mechanical systems. However, designing linkages to follow a desired path, known as path synthesis, is challenging due to non-linearities, combinatorial nature, and strict geometric constraints. Current state-of-the-art algorithms cannot scale well to linkages with higher-order linkage graphs, which are required to satisfy more complicated paths for new mechanical systems, such as hopping and flying robots. One reason for this is that state-of-the-art algorithms spend the majority of the time exploring constraint-violating designs. This work uses an Assur group 0DOF linkage as a graph grammar rule to modify both linkage graph and spatial parameters, ensuring all designs are valid 1DOF linkages. Using this graph grammar, this paper formulates linkage path synthesis as a tree search and uses a deep reinforcement learning (DRL) agent to search the space of kinematically feasible planar 1DOF linkages. This paper introduces a method using a graph convolution policy for high-order linkage graph optimization (GCP-HOLO). An anytime algorithm, GCP-HOLO outputs linkages with 1–8 loops (4–16 bars) efficiently. When comparing the GCP-HOLO formulation to a recent state-of-the-art paper that solves a mixed integer conic program, GCP-HOLO generates sets of solutions of varying linkage complexities to eight test trajectories in a quarter of the time. Extending GCP-HOLO with a global node optimization, such as covariance matrix adaptation evolutionary strategy, the results quickly converge to finding better solutions for 4/8 tests, with the whole pipeline capable of a 13X speed increase.

[Paper](https://asmedigitalcollection.asme.org/mechanicaldesign/article/145/7/073303/1160180/GCP-HOLO-Generating-High-Order-Linkage-Graphs-for)

[Code](https://github.com/mfogelson/gcp_holo)