---
tags:
  - exclude
---

# Projects New Design
>[!Abstract]+ Formats 
>
>>[!Abstract]- **F 0.0.1**
>> Due to limited screen size from now[^1] on the format has been changed 
>> 
>>
>>### Rules
>>1. Project  Name should be **first letter caps**
>>**Eg**: **Kannur Solar Monitor** , where each letter which is the start of new word will start with capital letter
>>2.  The project_dir should be in the following format 
>> 
>>There question arises whether the project should be in its own `dir` or outside the dir , which makes easy to open a single file but , having its own directory makes packing easy like if some one want to get the hand on the note through git or some other platform , and if the not has its own `dir` then they dont have to clone the entire repo but just download the notes they want. But then again there still problem exists like , if i want to create independent directories for each and every project that would make the too much repo in the github account , it will be something like the following 
>>If i am doing an electronics project , then it will have a **schematic diagram** , **Microcontroller codes** if i've used any  , also there will be notes folder it will be something like 
>>```
>>...System
>>	...Schematics
>>	....Microcontroller_Codes
>>	...Website
>>	...Obsidian_Notes 
>>```
>>This is well organised in terms of structure and format. Because the codes are separated well .
>>```bash
>>git clone --recursive ...System 
>>``` 
>>will be able to clone the entire system 
>>```
>>├── Documents.md
  >>  ├── Kannur Solar Batter Monitor Sketch.md
  >>  ├── Kannur Solar Battery Meter Canvas.canvas
  >>  ├── Kannur Solar Battery Monitor System.md
  >>  ├── Ledger.md
  >>  ├── Reasearch And Development.md
  >>  ├── Version 3.md
  >>  ├── Version Control.md
  >>  ├── Versions
>> 		│   ├── Version 1 Without Relay.md
>> 		│   ├── Version 1.md
>> 		│   ├── Version 2 with MQTT.md
>> 		│   ├── Version 2.md
>> 		│   └── Version 3.excalidraw.md
>> 		├── Versions.md
  >>  ├── attachments
  >>  │   ├── Bottom View.excalidraw.md
  >>  │   ├── Relay Module bottom.excalidraw.md
  >>  │   ├── Relay Module top.excalidraw.md
  >>  │   ├── Top View.excalidraw.md
  >>  │   ├── Version 1.excalidraw.md
  >>  │   ├── case.md
  >>  │   ├── docs
  >>  │   │   ├── bust ticket 2.png
  >>  │   │   ├── bust ticket.png
  >>  │   │   ├── dc dc Connector.png
  >>  │   │   ├── electronics components bill 2.png
  >>  │   │   ├── electronics components bill.png
  >>  │   │   └── pvc box.png
  >>  │   ├── initial circuit diagram.png
  >>  │   ├── p1.png
  >>  │   ├── p2.png
  >>  │   ├── p3.png
  >>  │   ├── relay change.png
  >>  │   └── voltage Sensing.excalidraw.md
  >>  └── drawings
  >>      ├── Drawing 2025-02-08 23.35.22.excalidraw.md
  >>      └── Future Ideas
  >>          └── Drawing 2025-02-10 13.38.10.excalidraw.md
>>```



[^1]:2025-04-24 1:40 PM 