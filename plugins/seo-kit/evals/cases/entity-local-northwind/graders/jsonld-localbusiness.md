---
# The identity file (content of the Write call that creates seo-reports/...-identity.md) contains a LocalBusiness-family type (LocalBusiness or a subtype such as Physiotherapy / MedicalBusiness / MedicalClinic).
type: regex
target: trace
pattern: '-identity\.md\\*"\s*,\s*\\*"content\\*"\s*:\s*\\*"(?:[^"\\]|\\.)*?(?:LocalBusiness|Physiotherapy|MedicalBusiness|MedicalClinic)'
---
