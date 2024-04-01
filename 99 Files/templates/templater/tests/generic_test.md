<%-*
let tester = await tp.system.suggester(["Ganga", "Drishya"], ["ganga", "drishya"], false, "Tester Name?");
let module = await tp.system.suggester(["Accounts"], ["accounts"], false, "Module?");
let sub_module = await tp.system.suggester(["Receipt", "Pending","Consolidated Fee Report","Fee Collection"], ["receipt", "pending","consolidated_fee","collection"], false, "Sub Module?");
let tab_name = await tp.system.suggester(["Default","Summary", "Detailed", "Breakdown", "Transaction", "Feeheadwise Summary", "Feeheadwise Detailed"], ["default","summary", "detailed", "breakdown", "transaction", "feeheadwise_summary", "feeheadwise_detailed"], false, "Tab Name?");
let status = await tp.system.suggester(["Open", "In Progress", "Resolved", "Closed"], ["open", "in_progress", "resolved", "closed"], false, "Status?");
let start_date = tp.date.now("YYYY-MM-DD");
_%>
---
tags:
  - bug
tester: <% tester %>
module: <% module %>
sub_module: <% sub_module %>
tab_name: <% tab_name %>
status: <% status %>
start_date: <% start_date %>
cssclasses:
  - wide-page
---

# Bug Report: <% sub_module %> - <% tab_name %>

## Description

## Steps to Reproduce

## Expected Result

## Actual Result

## Screenshots/Logs
