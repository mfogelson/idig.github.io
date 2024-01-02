---
title: Coupling Simulated Annealing and Homogenization to Design Thermally Conductive Hybrid Lattice Support Structure for LPBF
description: |
  A framework to create hybrid lattice support structures by modifying simulated annealing and incorporating homogenization approximation.

people:
  - Lisha

layout: project
image: img/lattice_tmp.png
last-updated: 2023-05-22
status: active

---
​
When designed effectively, support structures for Laser Powder Bed Fusion (LPBF) quickly dissipate heat and mitigate part distortion without driving up excessive costs. Lattices, composed of individual unit cells strategically arranged to achieve a desired function, are a promising solution as support structure. Prior research utilizing gradient-based optimizers to design lattice support structures for heat dissipation pose challenges regarding limited design exploration and non-differentiable design variables. Non-gradient-based optimizers are an alternative solution but are known to be too slow compared to gradient-based optimizers and have not yet been applied to optimize the heat dissipation of lattice support structures. Thus, this paper presents a computational framework that facilitates the design of lattice support structures with stochastic optimization to maximize heat dissipation. Simulated annealing (SA) is utilized to quickly optimize the distribution of three com-monly employed unit cells while adhering to user-defined manufacturing constraints. By incorporating both stage-dependent actions and homogenization approximation with SA, a broader exploration of the design space is accomplished without compromising computation time. The framework is validated through the case study of a cantilever beam by generating optimal hybrid lattice support structures with about 16% better heat dissipation than the uniformly distributed benchmark design with manufacturing constraints satisfied. 