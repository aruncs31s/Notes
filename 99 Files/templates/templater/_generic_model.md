---
id: _generic_model
aliases: []
tags: []
---

# Common Table Type

```go
type StaffProjectGuided struct {
ID                uint       `gorm:"primaryKey" `
StaffID           uint       `gorm:"not null"`
Title             string     `gorm:"type:text"`
```

^f9b01e

```go
CreatedAt         time.Time  `gorm:"column:created_at;autoCreateTime:milli"`
UpdatedAt         time.Time  `gorm:"column:updated_at;autoUpdateTime:milli"`
CreatedBy         *uint      `gorm:"column:created_by;type:int(11)"`
UpdatedBy         *uint      `gorm:"column:updated_by;type:int(11)"`
Agent             *string    `gorm:"column:agent;type:varchar(255)"`
IPAddress         *string    `gorm:"column:ip_address;type:varchar(45)"`
```

^134522

## FKs

```go
AcademicYearID    uint       ``
PeriodID          uint       `json:"period_id"`
FundingAgencyID   uint       `json:"funding_agency_id"`
ScholarID         uint       `json:"scholar_id"`
```

## Relations

```go
Staff         *Staff         `gorm:"foreignKey:StaffID;references:id" json:"staff,omitempty"`
AcademicYear  *AcademicYear  `gorm:"foreignKey:AcademicYearID;references:id" json:"academic_year,omitempty"`
Period        *Period        `gorm:"foreignKey:PeriodID;references:id" json:"period,omitempty"`
FundingAgency *FundingAgency `gorm:"foreignKey:FundingAgencyID;references:id" json:"funding_agency,omitempty"`
Scholar       *ScholarData   `gorm:"foreignKey:ScholarID;references:id" json:"scholar,omitempty"`
```
