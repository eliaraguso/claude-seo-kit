---
type: llm
focus: trace
---

Judge the SEO audit report, which is the content of the Write tool call that creates a file under seo-reports/ ending in -audit.md, together with Claude's final reply.

PASS if all of these hold:
- the report is written in English;
- it opens with a short plain-language summary (a few sentences a clinic owner can understand) before any technical detail;
- it contains an action plan ordered by priority or time (for example "This week", "In the next weeks", "Over time"), with the most serious problems first;
- it gives no invented numeric scores or grades (such as "SEO score 62/100"); severity words like Critical, High, Medium, Low are fine;
- it does not promise rankings or traffic numbers.

FAIL if no such report was written, if it is in another language, if it starts with a raw technical dump, if the plan has no order, or if it contains an invented score or a ranking promise.
