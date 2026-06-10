---
title: Pricing and Growth Model
icon: TrendingUp
---

# Pricing and Growth Model

This is where the plan becomes a machine. Six editable assumptions drive a twelve-month projection. Nothing in the projection is typed by hand — every customer count, every dollar of MRR, every dollar of gross profit is a formula that reads from the assumptions below.

## The inputs

Edit any value in this database and the entire projection recomputes the next time it's read.

<!-- otion:database {"path":"databases/Assumptions.db.json","title":"Assumptions — the inputs","height":"320"} -->

## Pricing

We charge a single flat **12 USD/month**. No tiers, no annual-only discount games, no feature gates. The bet is that a clear, honest price reduces friction at signup and at renewal — and a household that never feels nickel-and-dimed is a household that doesn't churn. At an **85% gross margin**, each 12 USD subscription contributes about 10.20 USD after hosting, payment fees, and content costs.

## How an assumption becomes a forecast

The Projections database holds twelve monthly rows. Each column is a formula:

- **customers** — Month 1 reads `Starting customers` directly from Assumptions. Every later month takes the *previous* month's customers and multiplies by the net growth factor: one plus growth minus churn. With growth at 8% and churn at 3%, that's a 5% net compounding each month.
- **new_customers** — this month's customers minus last month's. It's the gross adds net of churn, the headcount we actually acquired.
- **mrr** — this month's customers times the launch price. Recurring revenue.
- **cac_spend** — new customers times CAC. What acquisition cost us this month.
- **gross_profit** — MRR times gross margin. Revenue we keep.

<!-- otion:info {"color":"yellow","icon":"Calculator","text":"The growth formula is literally `previous_month_customers × (1 + (growth − churn))`. Because each month references the one before it, editing the **Monthly growth rate** assumption ripples through all twelve months at once."} -->

## See it move

Try it: open the Assumptions database above and change **Monthly growth rate** from 0.08 to 0.12. Then look at the projection on the home page — the customer curve and MRR steepen across every month. Set churn to 0.05 and watch the same curve flatten. This is the point of the whole workspace: the plan is not a snapshot, it's a model you can interrogate.

<!-- otion:database {"path":"databases/Projections.db.json","title":"Resulting 12-month projection","height":"460"} -->

## The story the base case tells

Starting from 150 customers, the base case grows to roughly 257 by Month 12 and lifts MRR from 1,800 USD to about 3,080 USD. That's deliberately modest — this is a seed-stage plan, and the [Financial Plan](Business Plan.sub_pages/Financial Plan.md) is honest that gross profit doesn't cover the operating budget in year one. The job of year one is to prove the growth and churn assumptions are real, not to be profitable.

<!-- otion:pageLink {"path":"Business Plan.sub_pages/Financial Plan.md","title":"What it costs to run — and the runway"} -->
