---
tags:
  - etlab
  - table
cssclasses:
  - wide-page
status:
---
<%*
let tableName = await tp.system.prompt("Enter the table name (e.g., staff_qualifications):");
%>
#  SQL Table: <% tableName %>


<%*
// Ask for Go struct name (optional, can be derived from table name)
let structName = await tp.system.prompt("Enter Go struct name (optional, press Enter to auto-generate):");
if (!structName) {
    // Auto-generate struct name from table name (snake_case to PascalCase)
    structName = tableName.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join('');
}

// Ask whether this table is new, being updated, or is a reference/old table.
const options = ["New Table", "Updating Existing", "Reference/Old"];
const icons = ["✅ New", "🛠️ Update", "♻️ Reference"];
let state = await tp.system.suggester(options, icons, false, "Is this a new table, an update, or a reference/old table?");

// Print a small badge line and inject a starter heading for each choice
tR += `\n> **Table state:** ${state}\n\n`;
if (state === "New Table") {
    tR += "## New Table\n- Purpose: \n- Initial columns: \n- Migration (yes/no): \n\n";
} else if (state === "Updating Existing") {
    tR += "## Updated Table\n- Changes summary: \n- Migration steps: \n- Backward compatibility: \n\n";
} else {
    tR += "## Reference / Old Table\n- Reason for reference: \n- Will it be migrated? (yes/no): \n- Notes: \n\n";
}
%>



## Overview
- **Purpose**: Description of what this table stores
- **Related Tables**: List of related tables
- **Status**: Draft/In Development/Production





## Core Columns
| Column     | Type         | Constraint                 | Comment              |
| ---------- | ------------ | -------------------------- | -------------------- |
| `id`       | INT UNSIGNED | PRIMARY KEY AUTO_INCREMENT | Unique identifier    |
| `staff_id` | INT UNSIGNED | NOT NULL                   | FK to staff table    |
| `type`     | INT          | DEFAULT 12                 | Type identifier      |
| `status`   | TINYINT(1)   | DEFAULT 1                  | 1=Active, 0=Inactive |
| `year_id`  | INT UNSIGNED |                            | FK to academic_year  |
| `file`     | VARCHAR(255) |                            | File path/upload     |
| `sort`     | INT          | DEFAULT 0                  | Sort order           |
|            |              |                            |                      |

## Metadata Columns
| Column | Type | Default | Comment |
|--------|------|---------|---------|
| `created_at` | TIMESTAMP | CURRENT_TIMESTAMP | Record creation |
| `updated_at` | TIMESTAMP | CURRENT_TIMESTAMP ON UPDATE | Last modification |
| `created_by` | INT(11) | NULL | FK to users |
| `updated_by` | INT(11) | NULL | FK to users |
| `agent` | VARCHAR(255) | NULL | Last updater agent |
| `ip` | VARCHAR(45) | NULL | Last updater IP |

## Foreign Keys
```sql
FOREIGN KEY (staff_id) REFERENCES staff(id) ON DELETE CASCADE
FOREIGN KEY (year_id) REFERENCES academic_year(id)
FOREIGN KEY (created_by) REFERENCES users(id)
FOREIGN KEY (updated_by) REFERENCES users(id)
```

## Indexes
```sql
INDEX idx_staff (staff_id)
INDEX idx_status (status)
INDEX idx_year (year_id)
```

## SQL Create Statement
```sql
CREATE TABLE <% tableName %> (
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    staff_id INT UNSIGNED NOT NULL,
    -- Add columns here
 
        `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Creation timestamp',
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Update timestamp',
    `created_by` INT(11) NULL COMMENT 'Created by user ID (FK to users table)',
    `updated_by` INT(11) NULL COMMENT 'Updated by user ID (FK to users table)',
    agent VARCHAR(255) DEFAULT NULL COMMENT 'Agent of the last updater',
    ip VARCHAR(45) DEFAULT NULL COMMENT 'IP address of the last updater',
    FOREIGN KEY (staff_id) REFERENCES staff(id) ON DELETE CASCADE,
    INDEX idx_staff (staff_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='Table for <% tableName %>';
```

> **Note**: Table name will be automatically filled from your input

