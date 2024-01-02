---
title: Quantifying Aesthetic Form Preference And Design Generation
description: 

people:
  - Seth

layout: project
image: img/projects/researchseth2_clip_image002.png
# last-updated: <date>
status: inactive

---
One of the greatest challenges in product development is creating a form that is aesthetically attractive to an intended market audience.  Market research tools such as consumer surveys are well established for functional product features, but aesthetic preferences are as varied as the people that respond to them.  Additionally, and possibly even more challenging, user feedback requires objective measurement, quantification of aesthetics and of aesthetic preference. The common methods for quantifying aesthetics present respondents with metric scales over dimensions with abstract semantic labels like “strong” and “sexy.”  Even if researchers choose the correct semantics to test, and even if respondents accurately record their responses on these semantic scales, the results on the semantic scales must be translated back into a product shape, where the designer must take the consumers’ numerical scores for a set of semantics and translate that into a form which consumers will find desirable.  This translation presents a potential gap in understanding between the supply and demand sides of the marketplace. This gap between designer and user can be closed through objective methods to understand and quantify aesthetic preferences, because the designer would have concrete directions to use as a foundation for development of the product form.  Additionally, the quantification of aesthetic preference could be used by the designer as evidence to support certain product forms when engineering and manufacturing decisions are made that might adversely affect the aesthetics of the product form.

This project demonstrates how the qualitative attribute, form, can not only be represented quantitatively but also how customer preferences can be estimated as utility functions over the aesthetic space, so that new higher utility product forms can be proposed and explored.  To do so, the form is summarized with underlying latent form characteristics, and these underlying characteristics are specified to be attributes in a utility function.  Consumer surveys, created using design of experiments, are then used to capture an individual’s preference for the indicated attributes and thus the form. 


Once preference is summarized in the utility function, the utility function can be used as the basis for form generation and modification or design verification.  In new product development, quickly generating many product form concepts that a potential consumer prefers is a challenge.  By using the utility function in conjunction with a shape grammar representation we are able to rapidly and effectively generate product designs preferred by the consumer.  To do so, a multi-agent shape grammar implementation (MASGI) automatically generates product form designs according to the utility function that represents designer or consumer design preference.  Additionally, the multi-agent system creates a flexible shape grammar implementation that enables modifications to the shape grammar as the form design space changes.  The method is composed of three sub-processes: a Shape Grammar Interpreter that implements the shape grammar, an Agent System that chooses which shape grammar rules to implement and the parametric design choices according to a preference function, and a Preference Investigator that determines the preference function which constraints the automated form design process.
