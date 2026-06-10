---
title: Go-to-Market
icon: Megaphone
---

# Go-to-Market

Our acquisition target is a **40 USD CAC** with payback inside four months at the 12 USD price. We hit it by blending cheap organic channels with disciplined paid spend, and by making referral the default growth engine as the base scales.

## Channels

### Content and recipe SEO
A weekly stream of searchable, genuinely useful recipe and meal-planning posts. This is the slow-but-durable channel: it compounds, it lowers blended CAC over time, and it brings in households already in a planning mindset.

### Paid social
Instagram and TikTok campaigns aimed squarely at the home-cooking niche. We hold spend to a level where the blended CAC stays near 40 USD, and we treat the [Budget](Business Plan.sub_pages/Financial Plan.md) paid-social line as a dial, not a fixed cost.

### Referrals
<!-- otion:info {"color":"pink","icon":"Gift","text":"The strongest channel for a household utility is word of mouth. A give-a-month, get-a-month referral keeps CAC down precisely as the customer base — and therefore the number of potential referrers — grows month over month."} -->

### Partnerships
Bundles with grocery-delivery services and CSA boxes. NestRoute plans the week; the partner fulfills the groceries. It's distribution we don't pay for per-click, and it reinforces the product instead of competing with it.

## Funnel and activation

- **Signup** is free to start: set up the household, see one real weekly plan before paying.
- **Activation** is accepting and shopping the first plan — the moment the value lands.
- **Habit** is the third consecutive week, after which churn drops sharply because the app has learned the household.

## How spend tracks the model

Because `cac_spend` in the projection is `new_customers × CAC`, the model already ties acquisition cost to growth. If we push the growth assumption up, the projection automatically shows the higher acquisition spend it implies — so we never plan growth without also planning what it costs.

<!-- otion:info {"color":"blue","icon":"Info","text":"Discipline rule: if blended CAC drifts above the payback line, we shift budget from paid social toward referrals and content before we touch the growth target."} -->

<!-- otion:pageLink {"path":"Business Plan.sub_pages/Financial Plan.md","title":"The budget and the runway"} -->
