---
tags:
  - es_website
  - backend
  - idea_1
---
# YAML Conversion
So the initial idea is to conver a standard readme into a YAML frontmatter format that can be used in a static site component in our [[Embedded Systems Website]] 

## Required Format
```yaml
title: "SF-TB T845"
description: "Machine Screws"
main:
  id: 1
  content: |
    Introducing the SF-TB T845 – your go-to solution for precision fastening in machinery and equipment. This comprehensive set of machine screws is meticulously crafted to meet the stringent demands of industrial applications, ensuring secure and reliable fastening.
  imgCard: "@/images/product-image-1.avif"
  imgMain: "@/images/product-image-main-1.avif"
  imgAlt: "Mockup boxes of machine screws set"
tabs:
  - id: "tabs-with-card-item-1"
    dataTab: "#tabs-with-card-1"
    title: "Description"
  - id: "tabs-with-card-item-2"
    dataTab: "#tabs-with-card-2"
    title: "Specifications"
  - id: "tabs-with-card-item-3"
    dataTab: "#tabs-with-card-3"
    title: "Blueprints"
longDescription:
  title: "Precision Fastening Solutions"
  subTitle: |
    The SF-TB T845 Machine Screws offer unparalleled precision and reliability for industrial applications, ensuring seamless operation and longevity for your machinery and equipment.
  btnTitle: "Contact sales to learn more"
  btnURL: "#"
descriptionList:
  - title: "Durability"
    subTitle: "Crafted from high-quality materials, these machine screws are built to withstand the rigors of industrial environments."
  - title: "Precision Engineering"
    subTitle: "Engineered with precision-cut threads and exact specifications, ensuring a tight and secure fit for every application."
  - title: "Versatility"
    subTitle: "Suitable for a wide range of machinery and equipment, providing versatile fastening solutions for various industrial needs."
specificationsLeft:
  - title: "Material Composition"
    subTitle: "Constructed from premium-grade steel or alloy for exceptional strength and durability."
  - title: "Surface Finish"
    subTitle: "Finished with a protective coating to enhance corrosion resistance and extend service life."
  - title: "Quantity Per Set"
    subTitle: "Each set contains a comprehensive assortment of machine screws to meet diverse industrial requirements."
  - title: "Size Range"
    subTitle: "Available in various sizes and lengths to accommodate different machinery and equipment specifications."
specificationsRight:
  - title: "Thread Specifications"
    subTitle: "Precision-engineered threads ensure optimal grip and reliability, even in high-vibration environments."
  - title: "Load Capacity"
    subTitle: "Designed to meet or exceed industry standards for load-bearing capacity, ensuring safe and reliable operation."
  - title: "Certifications"
    subTitle: "Compliant with relevant industry standards and certifications, guaranteeing quality and reliability."
  - title: "Applications"
    subTitle: "Ideal for use in a wide range of industrial machinery, equipment, and assemblies that demand precise and secure fastening."
blueprints:
  first: "@/images/blueprint-1.avif"
  second: "@/images/blueprint-2.avif"   
```

![[Recording 20250710223947.m4a]]

## The README.md Format 
<iframe src="https://raw.githubusercontent.com/aruncs31s/es_gcek_electronics_projects_template/refs/heads/main/README.md" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>



Core Idea:

Read the README.md file content.

Parse the Markdown to extract headings, paragraphs, lists, and images.

Map these extracted components to the specific keys in your desired YAML frontmatter structure (e.g., title, description, main.content, longDescription.subTitle, specificationsLeft, tableData, etc.).

Generate the YAML frontmatter string.

Combine the YAML frontmatter with any remaining Markdown content (if any, though your example suggests all content is in frontmatter).