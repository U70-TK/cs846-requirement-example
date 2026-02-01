# Week 4 Guideline Counterexamples: Requirements

**Authors:** [Neel Sanjaybhai Faganiya, Ibrahim Mohammed Sayem, Felix Wang]

## Example Problems

### Problem A_1: Requirement Validation, Risk, and Missing NFRs (privacy, compliance, and accessibility) check

**Task Description:** Summarize the key points from each stakeholder interview, and identify which requirements are ambiguous or inconsistent, and what targeted follow-up questions they should ask.

Find the related files in the `Exercise_A/docs/transcripts` folder.

**Starter Code:**

The question needs to be asked of each stakeholder:
- Clarify contradictions with the different actors, such as the customer, software engineer, etc.
- Explore what alternatives are available.
- Uncover the missing non-functional requirements, such as privacy, compliance, and accessibility.

---

### Problem B_1: Requirement Classification

**Task Description:**

To classify requirements as either F (Functional) or NF (Non-Functional) and produce only a 2-column table: ID | (F or N). No justifications, no explanation, no reflection.

**Starter Code:**

There is no starter code for this task. Related file in `artifacts/requirements_R1-R4.md` has requirements that have to be classified as either Functional or Non-Functional by producing a 2-column table in a file named "req_classification_ans.md" under the same artifacts folder.

---

### Problem C: Requirement Backlog Construction

**Github repository URL:** https://github.com/U70-TK/cs846-requirement-example

For consistency and comparison, please use the Copilot GPT-5 mini model for all parts of Problem C.

**Task Description:**

You are working as a requirements engineer on a mobile app, WikiLens, which utilizes a real-time AI computer vision engine to process camera frames. Once an object is identified, the app will automatically generate a brief introduction about the object and retrieve the most relevant Wiki page. Please read the requirement interview transcripts in the provided GitHub repository, and complete the tasks below.

**Student Tasks:**

1. **Customer Personas** - Based on the requirement interviews, please analyze who the targeted users of this app are, and create at least 3 detailed Customer Personas. For each persona, please include the Persona, Archetype, Core Needs, and Pain Points.

2. **Backlog Generation** - Use the same chat in Copilot, extract clear and actionable User Stories from the provided transcripts. Each one of the user stories should be in the form:
   - "As a [role/persona], I want to [interact with the app in a specific way] so that [a goal could be achieved]."
   - And interrelated stories should be in the same functional category.

3. **Minimum Viable Product (MVP)** - Use the same chat, apply the MoSCoW Prioritization method, and label each user story with a priority label:
   - Must Have (M)
   - Should Have (S)
   - Could Have (C)
   - Won't Have (W)

4. **Story Point** - Use a different chat, analyze the story points of each user story, and label each user story with a story point label from below:
   - 1: Everything is known about this user story. It has no other dependencies, and should be less than 2 hours' work.
   - 2: Almost everything is known. There are almost no dependencies, and it will be half a day's work.
   - 3: Something is known about this user story. It has some dependencies and will take up to 2 days.
   - 5: Almost nothing is known about this user story. It has a few dependencies and will take a few days.
   - 8: Nothing is known about this user story. It has more than a few dependencies, and will take around a week.
   - 13: Nothing is known about this user story. It has unknown dependencies and will take more than a week.

5. **Acceptance Criteria** - Use a different chat, define a sequence of step-by-step paths the user would navigate from the initial given state of the app to the desired outcome of each user story.

---


## References

[1] Min, Sewon, et al. "Rethinking the role of demonstrations: What makes in-context learning work?." arXiv preprint arXiv:2202.12837 (2022).

[2] Ralph, Paul. 'The Illusion of Requirements in Software Development'. Requirements Engineering, vol. 18, no. 3, Sept. 2013, pp. 293–296, https://doi.org/10.1007/s00766-012-0161-4.

[3] Ralph, Paul, and Paul Kelly. 'The Dimensions of Software Engineering Success'. Proceedings of the 36th International Conference on Software Engineering, Association for Computing Machinery, 2014, pp. 24–35, https://doi.org/10.1145/2568225.2568261. ICSE 2014.

[4] Kravchenko, Tatiana, Tatiana Bogdanova, and Timofey Shevgunov. "Ranking requirements using MoSCoW methodology in practice." Computer Science Online Conference. Cham: Springer International Publishing, 2022.

[5] Ronanki, K., Cabrero-Daniel, B., Horkoff, J., & Berger, C. (2024). Requirements engineering using generative ai: Prompts and prompting patterns. In Generative AI for effective software development (pp. 109-127). Cham: Springer Nature Switzerland.

[6] Santos, S., Breaux, T., Norton, T., Haghighi, S., & Ghanavati, S. (2024, June). Requirements satisfiability with in-context learning. In 2024 IEEE 32nd International Requirements Engineering Conference (RE) (pp. 168-179). IEEE.
