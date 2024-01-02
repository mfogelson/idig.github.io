---
title: The Role of Social Choice Theory and Arrow's Theorem in Engineering Design
# description: | 
#     description

people:
  - Kosa
  - Chris

layout: project
image: img/choice2.gif
last-updated: 2020-01-01
status: inactive

---
Much of the design process is accomplished by teams rather than individuals. During design, there often arise situations in which members of a team have different opinions, yet a group decision must still be made. Unfortunately, Arrow's Impossibility Theorem indicates that there is no method for aggregating group preferences that will always satisfy a small number of "fair" conditions.

A broad debate within the engineering design literature has attempted to assess whether or not Arrow's theorem applies to engineering design. Some researchers have proposed that it applies to all problem with multiple criteria or multiple decision-makers. Others have adopted the stance that engineering design is primarily concerned with the aggregation of multiple criteria, and thus Arrow's theorem need not apply. This project took the point of view that Arrow's theorem only applies to early stages of design (when criteria for comparing solutions are not well-defined).


With this in mind, we studied which voting rules were more likely to lead to outcomes that satisfied Arrow's conditions during the early stages of design. To do this, we first used experiential conjoint methodology to query real preferences for a set of 3D printed mugs (see above). We then used those preferences to construct, simulate, and analyze thousands of voting scenarios with different numbers of alternatives and voters, and several different voting rules.


Results indicated that the Copeland voting rule (shown above) offered the highest probability of satisfying all of Arrow's conditions. In addition, the Copeland rule was the most strategyproof (most resistant to manipulation by a dishonest individual). A comparison of the results for different voting rules is shown below.


Future work will extend this analysis to a larger set of aggregation functions, and explore the use of the Copeland function in more complex and longitudinal design contexts.

