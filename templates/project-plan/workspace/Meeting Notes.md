---
title: Meeting Notes
icon: NotebookPen
---

# Meeting Notes

Decisions and action items from the Aurora launch meetings, newest first. Decisions are in **bold** so they're easy to scan; every meeting ends with owned action items.

<!-- otion:info {"color":"gray","icon":"Info","text":"Format: context, then **decisions in bold**, then a checklist of action items with owners. If it isn't written here, it wasn't decided."} -->

## 2026-06-16 — Build kickoff

Attendees: Priya Raman, Mei-Ling Chen, Aleksandr Volkov, Carlos Mendes, Hannah Bergström.

We reviewed the Discovery outputs and aligned on how the two hardware and firmware workstreams run in parallel.

- **Decision: we will run hardware design and firmware development concurrently, not sequentially, to protect the October launch date.**
- **Decision: enclosure tooling is the critical path — Operations will start it the moment the PCB layout is frozen.**
- **Decision: we book the certification lab slot now rather than waiting for a finished board, and run pre-certification in-house first.**

Action items:

- [ ] Aleksandr: freeze the PCB layout by July 3
- [ ] Carlos: get tooling quotes from both contract manufacturers
- [ ] Mei-Ling: confirm the certification lab booking
- [ ] Hannah: refresh the spend forecast with tooling costs

## 2026-06-10 — Discovery review

Attendees: Marcus Feld, Priya Raman, Daniel Okafor, Mei-Ling Chen, Hannah Bergström.

Discovery is essentially complete. We walked the sponsor through the research, the architecture spike, and the business case.

- **Decision: Discovery gate is approved — we proceed to Build.**
- **Decision: Matter is the primary radio stack; Zigbee support is kept as a compatibility layer only.**
- **Decision: launch-price tiers are approved at the proposed margins.**

Action items:

- [x] Daniel: finalize the positioning brief
- [ ] Hannah: lock the unit-economics model for the charter
- [ ] Priya: schedule the Build kickoff

## 2026-05-22 — Kickoff & charter

Attendees: Priya Raman, Daniel Okafor, Mei-Ling Chen, James Whitfield, Carlos Mendes, Olivia Grant.

First full-team meeting. We agreed the scope, the five-phase structure, and the target launch date.

- **Decision: the public launch date is October 9, 2026.**
- **Decision: voice assistant, a developer SDK, and subscriptions are out of scope for this release.**
- **Decision: each phase ends in a formal gate that the Accountable lead must sign off.**

Action items:

- [x] Priya: write the project charter
- [x] Daniel: run customer discovery interviews
- [ ] James: build the retail-partner target list

## Standing actions

<!-- otion:todo {"text":"Circulate notes within 24 hours of every meeting","id":"todo-mtg-0001","created":"2026-05-22T09:00:00.000Z"} -->

<!-- otion:pageLink {"path":"Project Charter.md","title":"Back to the Project Charter"} -->
