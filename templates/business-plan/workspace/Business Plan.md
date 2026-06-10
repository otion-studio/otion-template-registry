---
title: Business Plan
icon: Rocket
---

# NestRoute — Business Plan

NestRoute is a meal-planning subscription app for busy households. You tell it who you're feeding and what's in the fridge, and it builds the week's dinners, a single shopping list, and a Sunday-night prep plan. This workspace is the working business plan for NestRoute's first year: a set of editable assumptions, a twelve-month revenue projection that recomputes from them, and an operating budget.

<!-- otion:info {"color":"blue","icon":"Lightbulb","text":"**The whole model lives in three databases.** *Assumptions* holds the inputs (price, growth, churn, CAC, margin). *Projections* turns them into a live 12-month forecast. *Budget* tracks what it costs to run. Change one number in Assumptions and every projection cell recomputes."} -->

## Core assumptions at a glance

<!-- otion:info {"color":"green","icon":"Target","text":"Launch price **12 USD/mo** · starting base **150 customers** · **8%** monthly growth · **3%** monthly churn · CAC **40 USD** · gross margin **85%**. Edit any of these on the Assumptions page and watch the projection move."} -->

## The 12-month projection

This is the heart of the plan. Every cell below is a formula reading from the Assumptions database — there are no hard-coded numbers in this table.

<!-- otion:database {"path":"databases/Projections.db.json","title":"12-Month Projection","height":"460"} -->

## The operating budget

<!-- otion:database {"path":"databases/Budget.db.json","title":"Operating Budget","height":"460"} -->

## Read the plan

<!-- otion:pageLink {"path":"Business Plan.sub_pages/Executive Summary.md","title":"Executive Summary"} -->

<!-- otion:pageLink {"path":"Business Plan.sub_pages/Product.md","title":"Product"} -->

<!-- otion:pageLink {"path":"Business Plan.sub_pages/Market and Customers.md","title":"Market and Customers"} -->

<!-- otion:pageLink {"path":"Business Plan.sub_pages/Pricing and Growth Model.md","title":"Pricing and Growth Model"} -->

<!-- otion:pageLink {"path":"Business Plan.sub_pages/Go-to-Market.md","title":"Go-to-Market"} -->

<!-- otion:pageLink {"path":"Business Plan.sub_pages/Financial Plan.md","title":"Financial Plan"} -->

## Before the next review

<!-- otion:todo {"text":"Validate the 8% monthly growth assumption against the first 60 days of post-launch data","id":"todo-bp-0001","created":"2026-06-01T09:00:00.000Z"} -->

<!-- otion:todo {"text":"Pressure-test churn — re-run the model at 5% to see the downside case","id":"todo-bp-0002","created":"2026-06-01T09:00:00.000Z"} -->

<!-- otion:todo {"text":"Confirm CAC of 40 USD holds once paid social spend scales past 2,500 USD/mo","id":"todo-bp-0003","created":"2026-06-01T09:00:00.000Z"} -->
