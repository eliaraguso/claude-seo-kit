---
type: llm
focus: trace
---

Judge the rewrite of src/content/features/shift-scheduling.md (the Write or Edit tool calls on that file) and Claude's final reply. The project's SEO.md lists confirmed product facts (weekly schedule by role, availability and time-off, labour cost against a target, publishing to phones, payroll CSV export, POS import, EUR 3 per active employee per month, 30-day trial) and says there are no approved customer testimonials.

PASS if all of these hold:
- the new copy is built on those product facts and does not invent facts that are not in the repository: no made-up customer names, quotes, testimonials, percentages, time savings or customer counts;
- where first-hand material would help (a customer example, a real result, a screenshot) it leaves a visible placeholder of the form [TO COMPLETE: ...] instead of filling it in;
- it is not keyword-stuffed: the phrase "shift scheduling" is not repeated mechanically and the text reads naturally for a restaurant or café manager;
- the frontmatter has a specific title and a specific meta description for this page;
- internal links are added to the page or proposed in the reply (for example to the shift swaps, time clock or pricing pages).

FAIL if the page invents testimonials, customer names or numbers, if it keeps the stuffed or generic wording, if title or description is missing or generic, or if no internal link is added or suggested.
