---
id: API_Designing
aliases: []
tags:
  - coding
  - web
  - apis
dg-publish: true
---
# API Designing 

```

2025/08/01 17:33:36 /home/aruncs/Work/etlab-backend-go/modules/staff/handler/register_staff_details.go:67 sql: Scan error on column index 2, name "dob": unsupported Scan, storing driver.Value type []uint8 into type *time.Time
[0.389ms] [rows:1] SELECT * FROM `s

```

This error occurs because the MySQL driver is returning the date as a byte slice (`[]uint8`) instead of a `time.Time` that GORM expects. This is a common issue with MySQL date/datetime handling in Go.

Here are several solutions:

#### Solution 1: Add `parseTime=true` to your database connection string

This is the most common fix. Update your database connection string to include `parseTime=true`:

```go
// Example connection string
dsn := "username:password@tcp(localhost:3306)/database_name?charset=utf8mb4&parseTime=true&loc=Local"
db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})

```

```go
package models

import (
	"database/sql/driver"
	"fmt"
	"time"
)

// CustomDate handles MySQL date scanning issues
type CustomDate struct {
	time.Time
}

// Scan implements the Scanner interface
func (cd *CustomDate) Scan(value interface{}) error {
	if value == nil {
		cd.Time = time.Time{}
		return nil
	}
	
	switch v := value.(type) {
	case time.Time:
		cd.Time = v
		return nil
	case []byte:
		return cd.parseFromString(string(v))
	case string:
		return cd.parseFromString(v)
	default:
		return fmt.Errorf("cannot scan %T into CustomDate", value)
	}
}

// Value implements the Valuer interface
func (cd CustomDate) Value() (driver.Value, error) {
	if cd.Time.IsZero() {
		return nil, nil
	}
	return cd.Time, nil
}

// parseFromString parses date string in various formats
func (cd *CustomDate) parseFromString(s string) error {
	if s == "" {
		cd.Time = time.Time{}
		return nil
	}
	
	// Try different date formats
	formats := []string{
		"2006-01-02",
		"2006-01-02 15:04:05",
		time.RFC3339,
	}
	
	for _, format := range formats {
		if t, err := time.Parse(format, s); err == nil {
			cd.Time = t
			return nil
		}
	}
	
	return fmt.Errorf("cannot parse date: %s", s)
}

// Updated StaffDetail struct using CustomDate
type StaffDetail struct {
	ID                       int        `gorm:"column:id;primaryKey;autoIncrement" json:"id"`
	StaffID                  int        `gorm:"column:staff_id;not null" json:"staff_id"`
	DOB                      CustomDate `gorm:"column:dob;type:date;not null" json:"dob"`
	Qualifications           *string    `gorm:"column:qualifications;size:250" json:"qualifications,omitempty"`
	Experience               *string    `gorm:"column:experience;size:700" json:"experience,omitempty"`
	MaritalStatus            *string    `gorm:"column:marital_status;size:25" json:"marital_status,omitempty"`
	FatherName               *string    `gorm:"column:father_name;size:60" json:"father_name,omitempty"`
	MotherName               *string    `gorm:"column:mother_name;size:60" json:"mother_name,omitempty"`
	SpouseName               *string    `gorm:"column:spouse_name;size:60" json:"spouse_name,omitempty"`
	BloodGroup               *string    `gorm:"column:blood_group;size:8" json:"blood_group,omitempty"`
	Nationality              *string    `gorm:"column:nationality;size:50" json:"nationality,omitempty"`
	PresentAddress           *string    `gorm:"column:present_address;size:500" json:"present_address,omitempty"`
	PermanentAddress         *string    `gorm:"column:permanent_address;size:500" json:"permanent_address,omitempty"`
	CVFile                   *string    `gorm:"column:cv_file;size:100" json:"cv_file,omitempty"`
	LastInstitution          *string    `gorm:"column:last_institution;size:200" json:"last_institution,omitempty"`
	PhoneHome                *string    `gorm:"column:phone_home;size:15" json:"phone_home,omitempty"`
	PhoneOffice              *string    `gorm:"column:phone_office;size:25" json:"phone_office,omitempty"`
	CreateTime               *time.Time `gorm:"column:create_time;type:datetime" json:"create_time,omitempty"`
	UpdateTime               *time.Time `gorm:"column:update_time;type:datetime" json:"update_time,omitempty"`
	CreatedBy                *int       `gorm:"column:created_by" json:"created_by,omitempty"`
	UpdatedBy                *int       `gorm:"column:updated_by" json:"updated_by,omitempty"`
	OfficeAddress            *string    `gorm:"column:office_address;type:mediumtext" json:"office_address,omitempty"`
	PanNo                    *string    `gorm:"column:pan_no;size:25" json:"pan_no,omitempty"`
	AadharNo                 *string    `gorm:"column:aadhar_no;size:25" json:"aadhar_no,omitempty"`
	PanImage                 *string    `gorm:"column:pan_image;size:100" json:"pan_image,omitempty"`
	AadharImage              *string    `gorm:"column:aadhar_image;size:100" json:"aadhar_image,omitempty"`
	InterestedSubjects       *string    `gorm:"column:interested_subjects;size:1000" json:"interested_subjects,omitempty"`
	PenNo                    *string    `gorm:"column:pen_no;size:1000" json:"pen_no,omitempty"`
	ReligionID               *int       `gorm:"column:religion_id" json:"religion_id,omitempty"`
	CasteID                  *int       `gorm:"column:caste_id" json:"caste_id,omitempty"`
	PresAddress1             *string    `gorm:"column:pres_address_1;type:mediumtext" json:"pres_address_1,omitempty"`
	PresAddress2             *string    `gorm:"column:pres_address_2;type:mediumtext" json:"pres_address_2,omitempty"`
	PresAddress3             *string    `gorm:"column:pres_address_3;type:mediumtext" json:"pres_address_3,omitempty"`
	PresAddressPin           *string    `gorm:"column:pres_address_pin;type:mediumtext" json:"pres_address_pin,omitempty"`
	PresAddressDistrict      *string    `gorm:"column:pres_address_district;type:mediumtext" json:"pres_address_district,omitempty"`
	PresAddressState         *string    `gorm:"column:pres_address_state;type:mediumtext" json:"pres_address_state,omitempty"`
	State                    *string    `gorm:"column:state;type:mediumtext" json:"state,omitempty"`
	Address1                 *string    `gorm:"column:address1;size:500" json:"address1,omitempty"`
	Address2                 *string    `gorm:"column:address2;size:500" json:"address2,omitempty"`
	Address3                 *string    `gorm:"column:address3;size:500" json:"address3,omitempty"`
	District                 *string    `gorm:"column:district;size:500" json:"district,omitempty"`
	Pin                      *string    `gorm:"column:pin;size:500" json:"pin,omitempty"`
	AltEmail                 *string    `gorm:"column:alt_email;type:mediumtext" json:"alt_email,omitempty"`
	AltPhone                 *int       `gorm:"column:alt_phone" json:"alt_phone,omitempty"`
	Expertise                *string    `gorm:"column:expertise;type:mediumtext" json:"expertise,omitempty"`
	ServiceBreak             *bool      `gorm:"column:service_break;type:tinyint(1)" json:"service_break,omitempty"`
	ServiceStartDate         *CustomDate `gorm:"column:service_start_date;type:date" json:"service_start_date,omitempty"`
	ServiceProof             *string    `gorm:"column:service_proof;type:mediumtext" json:"service_proof,omitempty"`
	ResearchArea             *string    `gorm:"column:research_area;type:mediumtext" json:"research_area,omitempty"`
	Form16PartA              *string    `gorm:"column:form_16_part_a;type:mediumtext" json:"form_16_part_a,omitempty"`
	Form16PartB              *string    `gorm:"column:form_16_part_b;type:mediumtext" json:"form_16_part_b,omitempty"`
	BankName                 *string    `gorm:"column:bank_name;type:mediumtext" json:"bank_name,omitempty"`
	BankAccNo                *string    `gorm:"column:bank_accno;type:mediumtext" json:"bank_accno,omitempty"`
	BankBranch               *string    `gorm:"column:bank_branch;type:mediumtext" json:"bank_branch,omitempty"`
	BankIFSCCode             *string    `gorm:"column:bank_ifsc_code;type:mediumtext" json:"bank_ifsc_code,omitempty"`
	PassportNo               *string    `gorm:"column:passport_no;type:mediumtext" json:"passport_no,omitempty"`
	PassportIssuedBy         *string    `gorm:"column:passport_issued_by;type:mediumtext" json:"passport_issued_by,omitempty"`
	PassportExpDate          *CustomDate `gorm:"column:passport_exp_date;type:date" json:"passport_exp_date,omitempty"`
	StaffroomNo              *string    `gorm:"column:staffroom_no;size:15" json:"staffroom_no,omitempty"`
	LicenseNo                *string    `gorm:"column:license_no;size:30" json:"license_no,omitempty"`
	LicenseExpire            CustomDate `gorm:"column:license_expire;type:date;not null" json:"license_expire"`
	BadgeNo                  *string    `gorm:"column:badge_no;size:30" json:"badge_no,omitempty"`
	BaggeExpire              CustomDate `gorm:"column:bagge_expire;type:date;not null" json:"bagge_expire"`
	VidwanID                 *string    `gorm:"column:vidwan_id;size:15" json:"vidwan_id,omitempty"`
	AICTEID                  *string    `gorm:"column:aicte_id;size:15" json:"aicte_id,omitempty"`
	HighQualifications       *string    `gorm:"column:high_qualifications;size:250" json:"high_qualifications,omitempty"`
	PursingPhD               *string    `gorm:"column:pursing_phd;size:250" json:"pursing_phd,omitempty"`
	SpecialisationArea       *string    `gorm:"column:specialisation_area;size:250" json:"specialisation_area,omitempty"`
	PhDResearchArea          *string    `gorm:"column:phd_research_area;type:mediumtext" json:"phd_research_area,omitempty"`
	PhDInstitution           *string    `gorm:"column:phd_institution;type:mediumtext" json:"phd_institution,omitempty"`
	PhDResearchProgress      *string    `gorm:"column:phd_research_progress;type:mediumtext" json:"phd_research_progress,omitempty"`
	PhDYearOfEnrollment      *string    `gorm:"column:phd_year_of_enrollment;type:mediumtext" json:"phd_year_of_enrollment,omitempty"`
	PhDDateOnDesignated      CustomDate `gorm:"column:phd_date_on_designated;type:date;not null" json:"phd_date_on_designated"`
	PhDGuidance              *string    `gorm:"column:phd_guidance;type:mediumtext" json:"phd_guidance,omitempty"`
	NoOfExperience           int        `gorm:"column:no_of_experience;not null" json:"no_of_experience"`
	Link                     *string    `gorm:"column:link;type:mediumtext" json:"link,omitempty"`
	OrcidID                  *string    `gorm:"column:orcid_id;type:text" json:"orcid_id,omitempty"`
	ScopusProfileID          *string    `gorm:"column:scopus_profile_id;type:text" json:"scopus_profile_id,omitempty"`
	WebOfScienceAccount      *string    `gorm:"column:web_of_science_account;type:text" json:"web_of_science_account,omitempty"`
	HIndex                   int        `gorm:"column:h_index;not null" json:"h_index"`
}

func (StaffDetail) TableName() string {
	return "staffdetail"
}

```

```go
## Solution 3: Use string fields and convert manually

The simplest approach if you want to avoid custom types:

```

```go
// Use string for date fields and convert when needed
DOB string `gorm:"column:dob;type:date;not null" json:"dob"`

// Convert when needed:
dobTime, err := time.Parse("2006-01-02", staffDetail.DOB)

```

#### Types 

```go
// Option 1: Simple (relies on existing DB schema)
Image *string `gorm:"column:image" json:"image,omitempty"`

// Option 2: Explicit type specification
Image *string `gorm:"column:image;type:varchar(100)" json:"image,omitempty"`

// Option 3: With additional constraints
Image *string `gorm:"column:image;type:varchar(100);default:null" json:"image,omitempty"`

```

