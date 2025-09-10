---
tags:
  - go
  - solid_principle
  - programming
  - design_pattern
---

# Forwarding methods (**delegation layer**)

**“Repository facade that delegates to reader and writer implementations.”**
> In architecture/DDD lingo
- `staffExperienceRepository` is the **aggregate repository**.
- `staffExperienceReader` / `staffExperienceWriter` are **specialized repositories**.
- These wrapper methods are just **forwarders**, ensuring the high-level interface is satisfied.

```go
func (r *staffExperienceRepository) FindByStaffID(staffID string) (*[]dto.StaffExperiencePresentation, error) {
    return r.reader.FindByStaffID(staffID)
}

```