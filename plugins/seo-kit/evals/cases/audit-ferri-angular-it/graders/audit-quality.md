---
type: llm
focus: trace
---

Judge the SEO audit report, which is the content of the Write tool call that creates a file under seo-reports/ ending in -audit.md, together with Claude's final reply.

PASS if all of these hold:
- the report and the final reply are written in Italian;
- the report opens with a short plain-language summary before any technical detail;
- it contains an action plan ordered by priority or time, with the most serious problems first;
- it points out the title of the /servizi/ page with "perchè" and gives the correct spelling "perché";
- it points out that the /chi-siamo/ page has a canonical (and a link) pointing to localhost;
- it gives no invented numeric scores or grades and does not promise rankings.

FAIL if no such report was written, if it is mainly in English, if the typo or the localhost canonical is missing, or if it contains an invented score or a ranking promise.
