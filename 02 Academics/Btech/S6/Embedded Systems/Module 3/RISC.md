---
id: RISC
aliases: []
tags:
  - academics
  - btech
  - s6
  - embedded_systems
  - module_3
dg-publish: true
---
# RISC
- A fixed (32-bit) instruction size with few formats; CISC processors typically had variable length instruction sets with many formats.
- A load-store architecture where instructions that process data operate only on registers and are separate from instructions that access memory; CISC processors typically allowed values in memory to be used as operands in data processing instructions.
- A large register bank of thirty-two 32-bit registers, all of which could be used for any purpose, to allow the load-store architecture to operate efficiently; CISC register sets were getting larger, but none was this large and most had different registers for different purposes (for example, the data and address registers on the Motorola MC68000)

### Organization
- Hard-wired instruction decode logic; CISC processors used large microcode ROMs to decode their instructions.
- Pipelined execution; CISC processors allowed little, if any, overlap between con secutive instructions (though they do now).
 - Single-cycle execution; CISC processors typically took many clock cycles to complete a single instruction
### Advantages
1. A smaller die size: A simple processor should require fewer transistors and less silicon area. Therefore a whole CPU will fit on a chip at an earlier stage in process technology development, and once the technology has developed beyond the point where either CPU will fit on a chip, a RISC CPU leaves more die area free for performance-enhancing features such as cache memory, memory management functions, floating-point hardware, and so on.
2. A shorter development time : A simple processor should take less design effort and therefore have a lower design cost and be better matched to the process technology when it is launched

3. Higher Performance 
- [ ] Invest more about higher performance and complete this

