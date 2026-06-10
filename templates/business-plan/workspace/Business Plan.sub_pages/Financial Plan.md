---
title: Financial Plan
icon: Wallet
---

# Financial Plan

This page is the honest part. Year one is an investment year: the projection's gross profit does not cover the operating budget, and that's expected. The plan is to spend deliberately against a clear runway while we prove the growth and churn assumptions are real.

## The operating budget

Each category below rolls up its line items automatically — the **monthly_cost** on every category row is a sum of its children, and **annual_cost** multiplies that monthly total by the `months_per_year` constant (12).

<!-- otion:database {"path":"databases/Budget.db.json","title":"Operating Budget","height":"560"} -->

## What it costs to run

<!-- otion:info {"color":"blue","icon":"Info","text":"At launch the budget runs about **33,000 USD/month**, roughly **399,000 USD/year**. Engineering is the largest line — the product is the company — followed by Operations (a lean founder draw) and Marketing."} -->

The budget is intentionally lean. The founder salary is below market to stretch runway, engineering is contractor-based so it can flex, and marketing is held to a level where blended CAC stays near our 40 USD target.

## Revenue versus burn

Here's the year-one reality, stated without spin:

- Month 1 gross profit is about **1,530 USD**; Month 12 is about **2,617 USD**.
- Monthly burn is about **33,000 USD**.

So gross profit covers a single-digit percentage of burn in year one. **That is the correct shape for a seed-stage plan.** The point of the first twelve months is not profitability — it's proving that 8% growth and 3% churn hold once real money is on the line. If they do, the same compounding that takes us from 150 to 257 customers in year one takes us much further in year two, when the customer base is large enough for gross profit to start closing the gap.

## Runway

<!-- otion:info {"color":"yellow","icon":"AlertTriangle","text":"At about **33,000 USD/month** of burn against modest early revenue, a **500,000 USD** seed raise funds roughly **15–16 months** of runway after accounting for the small but growing gross profit. That's enough to reach the year-two inflection where net growth compounds on a bigger base."} -->

### What we watch monthly

- **Net new customers** — the single number that validates or breaks the model.
- **Churn** — the most dangerous assumption; a drift from 3% to 5% reshapes everything.
- **Blended CAC** — if it climbs, we rebalance toward referrals before raising the growth target.
- **Burn multiple** — dollars burned per dollar of net new gross profit, trending down.

## Re-run the model anytime

Every figure on this page flows from the [Assumptions model](Business Plan.sub_pages/Pricing and Growth Model.md). Change an input, and the projection — and this whole story — moves with it. That's the discipline the workspace is built to enforce: no number without a model behind it.

<!-- otion:pageLink {"path":"Business Plan.sub_pages/Pricing and Growth Model.md","title":"Back to the model"} -->
