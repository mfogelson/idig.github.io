---
title: Intelligent 3d Systems
description: 

people:
  - JonCagan

layout: project
# image: <image>.jpg
# last-updated: <date>
status: inactive

---
INTRODUCTION 
We define the general three-dimensional component layout problem as:

Given a set of three dimensional objects of arbitrary geometry and an available space (possibly the space of a container), find a placement for the objects within the space that achieves the design objectives, such that none of the objects interfere (i.e., occupy the same space), while satisfying optional spatial and performance constraints on the objects.

Component layout plays an important role in the design and usability of many engineering artifacts. Engineering artifacts of today are becoming increasingly detailed, resulting in continuous competitive pressure to increase complexity, decrease size, and reduce the design cycle time. As the availability of user-configured designs is becoming more prevalent; the layout of these one-of-a-kind designs must be individually configured, requiring fast computational procedures. To date, computer support of such layout tasks has only focused on representation and manual manipulation of the shapes. We provide a technique that can solve general layout problems faster with greater consideration of alternatives.

ALGORITHMS 

The 3D layout space is nonlinear and combinatorial, making it difficult to find an algorithm that is both efficient and capable of finding the global, or at least good local, optimum. We have adapted simulated annealing algorithm and pattern direct search algorithm as the search methods.

---SIMULATED ANNEALING:

Simulated annealing algorithm is a stochastic optimization technique introduced by Kirkpatrick et al. In summary, within the algorithm an initial design state is chosen and the value of the objective function for the state is evaluated. A step is taken to a new state by applying a move, or operator, from an available move set. This new state is evaluated. If the step leads to an improvement in the objective function, the new state is accepted. If the step leads to an inferior state, the step may still be accepted with some probability. This probability is a function of a decreasing parameter called temperature. The temperature is controlled by an annealing schedule. We use adaptive annealing schedules and dynamically modified move selections to improve the efficiency of the algorithm.

---EXTENDED PATTERN DIRECT SEARCH:

Pattern direct search algorithms are a subset of direct search algorithms introduced by Hooke and Jeeves, and recently researched by Torczon et al. The search algorithms follow a series of exploratory moves defined by pattern matrices to walk through a design space to search for a stationary point. They rely exclusively on the direct comparison of function values during search. We introduced extensions to the algorithms to incorporate domain-specific knowledge and to give them a stochastic flavor. The results show a one-to-two orders of magnitude improvement in run time over simulated annealing algorithm with equivalent quality solutions.

FEATURES

Optimizes the location of objects in Euclidean space while optimizing the objectives and satisfying given constraints.
Handles objects of any geometry.
Handles perturbations in 6 dimensional space (3 translations & 3 rotations).
Provides visual feedback to the user as it is optimizing the placement.
Interfaces with commercial CAD packages like ProEngineer.
Conforms with standard OOD practices, coded in C++.

OBJECTIVES

Different layout problems have different goals, or objectives. We have formulated several objectives as options with our algorithm. Among them are:
maximization of packing density
minimization of routing costs
maximization of assemblability
minimization of configuration costs
minimization of center of gravity
optimization of performance measures
Multiple objectives can be considered concurrently; each goal is added to a weighted multi-objective function. Constraints that can be articulated are added to the objective function as penalty terms.

MULTIRESOURCE MODELLING 

Of the primary objective function terms considered, the single most computationally expensive one to evaluate is the interference detection and quantification between components. To minimize overall run time, we use hierarchical octree models to approximate geometry of components and obtain interference calculations in reasonable time.

An octree is an approximation of an object at various levels of resolution based on successive binary division along each coordinate direction. Each division in 3D space divides a cube into eight cubes. We classify each cube at each level of division as white, black and gray -- white cubes indicate that no part of the actual object sits inside that cube, black indicates that the entire cube rests inside the original object and gray indicates a partial intersection. Figure 1 illustrates three levels of decomposition of a model in 2D.

 

TEST CASES

8 CUBE PACKING: 
Packing 8 cubes of dimensions 20x20x20 into a container of 
dimensions 40x40x40
Each cube is unconstrained in all 6 degrees of freedom 
Average time taken: 9 seonds 

64 CUBE PACKING: 
Packing 64 cubes of dimensions 20x20x20 into a container of 
dimensions 80x80x80
Each cube has 6 degrees of freedom 
Average time taken : 20 minutes 

LUNAR ROVER PACKING:
Packing of the components of a lunar rover for a low center of 
gravity

18 COGWHEEL PACKING:
Packing of 18 cog wheels into a cubic container. Note that cogwheels 
are non-convex, and must mesh in order to pack properly. 
Average time taken: 2.5 minutes 

SATURN CAR ENGINE COMPARTMENT LAYOUT: 
11 components and 26 constraints 
Average time taken: 17 seconds 

HEAT PUMP LAYOUT AND ROUTING: 
Concurrent layout and routing (routes not shown except in the 
last snapshot)
7 components, 6 routes and 2 constraints
Average time taken: 3 seconds 

FUTURE WORK 

Current extensions include incorporation of various analysis/simulation into the layout algorithm, modification of the search strategy to best meet specific classes of problems, and investigation into new applications of the basic search mechanisms. 

The system was commercialized with design advance (www.designadvance.com).