---
id: Modular_CSS_Layout_for_Obsidian
aliases: []
tags:
  - os
  - tools
  - obsidian
cssclasses: 
dg-publish: true
---
## Modular CSS Layout for Obsidian
[Source](https://github.com/efemkay/obsidian-modular-css-layout/tree/main?tab=readme-ov-file#installation--download-and-enable)
Provides the following features using the `cssclasses `
- `wide-page`
- `wide-dataview`
- `wide-table`
- `wide-callout`
- `wide-backlinks`
- and  vault-wide toggle for each of the above

#### Multi Column layout 
Use the `> [!multi-column]` for multi column layout and need to put a `>` before actual callouts.

1. using `> [!info|right-medium]`
#test
> [!info|right-medium]
> 
> test test test test

> [!multi-column]
>
>> [!note]+ Use Case
>> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
>> ##### User Case Background
>> Vitae nunc sed velit dignissim sodales. In cursus turpis massa tincidunt dui ut ornare lectus.
>
>> [!warning]+ Resources
>> #### Requirement
>> - Lorem ipsum dolor sit amet
>> - Vitae nunc sed velit dignissim sodales.
>> - In cursus turpis massa tincidunt dui ut ornare lectus.
>
>> [!todo]+
>> - [x] Define Use Case ✅ 2024-07-31
>> - [ ] Craft User Story
>> - [ ] Develop draft sketches

## List Grid Example - Goals and Objectives

- #### Core Work #mcl/list-grid
    - [[00 Home|Main Goal 1]]
    - [[00 Home|Main Goal 2]]
    - [[00 Home|Main Goal 3]]
        - Collaboration with Jane
    - [[00 Home|Main Goal 4]]
- #### Learning & System
    - [[00 Home|Learning Goal 1]]
    - [[00 Home|Initiative 1]]
    - [[00 Home|Initiative 2]]
- #### Personal
    - [[00 Home|Personal Goal 1]]
    - [[00 Home|Personal Goal 2]]

|Type|Using Tag|MD Attr plugin|Frontmatter|
|---|---|---|---|
|LCol|`#mcl/list-column`|`two-column-list-block`  <br>`three-column-list-block`  <br>`four-column-list-block`  <br>`multi-column-list-block`|`two-column-list`  <br>`three-column-list`  <br>`four-column-list`  <br>`multi-column-list`|
|LGrd|`#mcl/list-grid`  <br>`#mcl/list-grid-wide`|-|`two-column-grid-list`  <br>`three-column-grid-list`|
|LCrd|`#mcl/list-card`  <br>`#mcl/list-card-wide`|-|-|
## Gallery Cards
