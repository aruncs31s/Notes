
## Old Generic Table  
Table: `staff_additional_detail`
```php
const TYPE_ACHIEVEMENT=1;
const TYPE_PUBLICATION=2;
const TYPE_EXPERIENCE=3;
const TYPE_PROJECT=4;
const TYPE_INTEREST=5;
const TYPE_POSITION=6;
const TYPE_COORDINATOR=7;
const TYPE_INTERCTION_OUTSIDE=8;
const TYPE_SEMINAR=9;
const TYPE_PROGRAM=10;
const TYPE_RESEARCH=11;
const TYPE_CONSULTANCY=12;
const TYPE_INT_SUBJECT=13;
const TYPE_ACTIVITY=14;
const TYPE_SUB_ENGAGED= 15;
const TYPE_QUALIFICATION = 16;
const TYPE_PATENT=17;
const TYPE_MOOC_COURSE=18;
const TYPE_PROFESSIONAL_BODY=19;
const TYPE_ADMIN_WORK=20;
const TYPE_APPOINTMENT_ORDER=21;
const TYPE_GUIDESHIP=22;
const TYPE_INTERESTED_SUBJECTS=23;
const TYPE_PROFILE_URL=24;
const TYPE_GOOGLE_SCHOLAR=25;
const TYPE_COURSE_OFFERED=26;
const TYPE_RESEARCH_STUDENT=27;
const TYPE_ORCID=28;
const TYPE_BIODATA=29;
```

| Field                       | Type          | Null | Key | Default | Extra          |
| --------------------------- | ------------- | ---- | --- | ------- | -------------- |
| id                          | int(11)       | NO   | PRI |         | auto_increment |
| staff_id                    | int(11)       | NO   | MUL |         |                |
| description                 | longtext      | YES  |     |         |                |
| sort                        | int(11)       | NO   |     |         |                |
| type                        | int(11)       | NO   |     |         |                |
| category                    | int(11)       | YES  |     |         |                |
| status                      | int(11)       | NO   |     |         |                |
| create_time                 | datetime      | YES  |     |         |                |
| update_time                 | datetime      | YES  |     |         |                |
| created_by                  | int(11)       | YES  |     |         |                |
| updated_by                  | int(11)       | YES  |     |         |                |
| year_id                     | int(11)       | YES  |     |         |                |
| from_date                   | date          | YES  |     |         |                |
| to_date                     | date          | YES  |     |         |                |
| period                      | int(11)       | YES  |     |         |                |
| attr_desc_1                 | longtext      | YES  |     |         |                |
| attr_desc_2                 | longtext      | YES  |     |         |                |
| attr_desc_3                 | longtext      | YES  |     |         |                |
| attr_int_1                  | varchar(250)  | YES  |     |         |                |
| attr_int_2                  | int(11)       | YES  |     |         |                |
| attr_int_3                  | int(11)       | YES  |     |         |                |
| level                       | int(11)       | YES  |     | 1       |                |
| title                       | mediumtext    | YES  |     |         |                |
| journal_name                | mediumtext    | YES  |     |         |                |
| index                       | mediumtext    | YES  |     |         |                |
| collaboration               | mediumtext    | YES  |     |         |                |
| with_whom                   | mediumtext    | YES  |     |         |                |
| patent_no                   | mediumtext    | YES  |     |         |                |
| patent_status               | int(11)       | YES  |     |         |                |
| file                        | mediumtext    | YES  |     |         |                |
| attr_desc_4                 | mediumtext    | YES  |     |         |                |
| designation                 | mediumtext    | YES  |     |         |                |
| duration                    | mediumtext    | YES  |     |         |                |
| attended_institute          | mediumtext    | YES  |     |         |                |
| oraganised_by               | mediumtext    | YES  |     |         |                |
| file_2                      | mediumtext    | YES  |     |         |                |
| cost                        | mediumtext    | YES  |     |         |                |
| awarded_by                  | int(11)       | YES  |     |         |                |
| month                       | int(11)       | YES  |     |         |                |
| academic_year               | int(11)       | YES  |     |         |                |
| agency                      | mediumtext    | YES  |     |         |                |
| confr_name                  | mediumtext    | YES  |     |         |                |
| confr_place                 | mediumtext    | YES  |     |         |                |
| presentation_mode           | mediumtext    | YES  |     |         |                |
| publisher                   | mediumtext    | YES  |     |         |                |
| book_title                  | mediumtext    | YES  |     |         |                |
| auth_name                   | mediumtext    | YES  |     |         |                |
| is_first_auth               | int(11)       | YES  |     |         |                |
| first_auth                  | mediumtext    | YES  |     |         |                |
| affil_first_auth            | mediumtext    | YES  |     |         |                |
| link_google_scholar         | mediumtext    | YES  |     |         |                |
| volume                      | mediumtext    | YES  |     |         |                |
| page_no                     | int(11)       | YES  |     |         |                |
| year                        | int(11)       | YES  |     |         |                |
| place                       | mediumtext    | YES  |     |         |                |
| phone                       | varchar(20)   | YES  |     |         |                |
| current_status              | mediumtext    | YES  |     |         |                |
| email                       | mediumtext    | YES  |     |         |                |
| provider                    | mediumtext    | YES  |     |         |                |
| annual_year                 | int(11)       | YES  |     |         |                |
| research_project            | mediumtext    | YES  |     |         |                |
| name_investigator           | mediumtext    | YES  |     |         |                |
| department_investigator     | mediumtext    | YES  |     |         |                |
| year_of_award               | int(11)       | YES  |     |         |                |
| link_ugc                    | mediumtext    | YES  |     |         |                |
| amount_sanctioned           | decimal(10,2) | NO   |     |         |                |
| duration_project            | mediumtext    | YES  |     |         |                |
| name_funding_agency         | mediumtext    | YES  |     |         |                |
| type_government             | int(11)       | NO   |     |         |                |
| patent_title                | mediumtext    | YES  |     |         |                |
| patent_assignee_name        | mediumtext    | YES  |     |         |                |
| patent_date_granted         | date          | YES  |     |         |                |
| patent_field_date           | date          | YES  |     |         |                |
| patent_link_url             | mediumtext    | YES  |     |         |                |
| publication_author_name     | mediumtext    | YES  |     |         |                |
| publication_co_author_name  | mediumtext    | YES  |     |         |                |
| publication_journal_name    | mediumtext    | YES  |     |         |                |
| year_of_publication         | int(11)       | YES  |     |         |                |
| link_journal                | mediumtext    | YES  |     |         |                |
| link_article                | mediumtext    | YES  |     |         |                |
| publication_issn_number     | varchar(200)  | YES  |     |         |                |
| mooc_achievements           | mediumtext    | YES  |     |         |                |
| mooc_course_title           | mediumtext    | YES  |     |         |                |
| title_experience            | mediumtext    | YES  |     |         |                |
| publication_book_title      | mediumtext    | YES  |     |         |                |
| publication_isbn_number     | varchar(200)  | YES  |     |         |                |
| publication_book_chapter    | mediumtext    | YES  |     |         |                |
| publication_chapter_ugc     | mediumtext    | YES  |     |         |                |
| published_paper_conference  | mediumtext    | YES  |     |         |                |
| publication_isbn_conference | varchar(200)  | YES  |     |         |                |
| link_website_journal        | mediumtext    | YES  |     |         |                |
| name_of_client              | mediumtext    | YES  |     |         |                |
| title_proceeding_conference | mediumtext    | YES  |     |         |                |
| no_of_experience            | int(11)       | NO   |     |         |                |
| patent_applicant_name       | mediumtext    | YES  |     |         |                |
| remarks                     | varchar(3000) | YES  |     |         |                |
| attr_int_4                  | int(11)       | YES  |     |         |                |
| profile_url                 | text          | YES  |     |         |                |
| award_name                  | varchar(100)  | YES  |     |         |                |
| field_of_contribution       | varchar(100)  | YES  |     |         |                |
| doi                         | varchar(20)   | YES  |     |         |                |
| orcid                       | varchar(20)   | YES  |     |         |                |
| biodata                     | text          | YES  |     |         |                |



### New Table Schema
```sql
<% await tp.system.prompt("Paste the Create Table SQL ") %>
```


## Mapping

<% await tp.system.prompt("Paste the Create Table SQL ") %>