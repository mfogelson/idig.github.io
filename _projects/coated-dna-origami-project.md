---
title: Generating Coated DNA Origami Designs
description: |
  Using an improved shape annealing algorithm, we can generate
  hollow DNA origami designs with porous walls.

people:
  - Tito

layout: project
image: img/coated-dna-origami-project.png
last-updated: 2023-05-16
---


In recent years, the field of structural DNA nanotechnology has advanced rapidly due to transformative design tools. Although these tools have been revolutionary, they still bear one overall limitation of requiring users to fully conceptualize their designs before designing. Recently, a simple computational casting technique was developed using generative optimization strategies to automate the design of DNA origami nanostructures. This approach employs a shape annealing algorithm, which creates a formal language of honeycomb DNA origami nanostructures with shape grammars and drives designs from the language towards a desired configuration using simulated annealing. This initial demonstration of the approach can generate novel scaffold routing schemes for creating solid or hollow structures constrained by boundaries of polyhedral meshes. The results from the initial approach, particularly from the hollow structures, reveal a challenging design space. This simple technique generates novel scaffold routing schemes that do not replicate the overall polyhedral mesh shape and is limited in its ability of controlling scaffold path exploration in the design space. This work demonstrates an approach for varying effective wall thickness and improving quality of polyhedral mesh coverage for hollow structures that can be tuned and optimized by introducing a more refined computational casting technique. We achieve these improvements through changes in the simulated annealing algorithm by adding a Hustin move set algorithm that dynamically adjusts the performance of the overall design and redefining how these hollow designs are articulated. The results in this work illustrate how the shape annealing algorithm can navigate a challenging design space to generate effective hollow designs.