# User Profile Feature - Visual Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           USER PROFILE SYSTEM                                │
│                        (Click Team Member Flow)                              │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  STEP 1: User Interaction                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│    ┌──────────────────────────────────────────────────┐                     │
│    │         Team Component (/src/components)         │                     │
│    ├──────────────────────────────────────────────────┤                     │
│    │                                                   │                     │
│    │  ┌─────────┐  ┌─────────┐  ┌─────────┐         │                     │
│    │  │ Member  │  │ Member  │  │ Member  │         │                     │
│    │  │  Card   │  │  Card   │  │  Card   │  ◄───── User clicks here      │
│    │  │ [Click] │  │ [Click] │  │ [Click] │         │                     │
│    │  └─────────┘  └─────────┘  └─────────┘         │                     │
│    │       ↓                                          │                     │
│    │  handleMemberClick(member)                      │                     │
│    └──────────────────────────────────────────────────┘                     │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘

                                    ↓

┌─────────────────────────────────────────────────────────────────────────────┐
│  STEP 2: Quick Preview Modal Opens                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│    ╔═══════════════════════════════════════════════════════════╗            │
│    ║         UserQuickModal                                     ║            │
│    ║         (/src/components/modals/UserQuickModal.tsx)       ║            │
│    ╠═══════════════════════════════════════════════════════════╣            │
│    ║                                                            ║            │
│    ║   ┌────────────────────────────────────────────────────┐  ║            │
│    ║   │  ┌──────┐                                          │  ║            │
│    ║   │  │Avatar│   John Doe                              │  ║            │
│    ║   │  │    │   @johndoe                             │  ║            │
│    ║   │  └──────┘   [Admin Badge]                         │  ║            │
│    ║   └────────────────────────────────────────────────────┘  ║            │
│    ║                                                            ║            │
│    ║    Email: john@example.com                              ║            │
│    ║    Location: San Francisco, CA                         ║            │
│    ║    Company: Tech Corp                                  ║            │
│    ║    Website: johndoe.com                                ║            │
│    ║    GitHub: @johndoe                                    ║            │
│    ║    Joined: January 2024                                ║            │
│    ║                                                            ║            │
│    ║   ┌────────────────────────────────────────────────┐     ║            │
│    ║   │         [See Full Profile Button]  ◄────────────── Click here     │
│    ║   └────────────────────────────────────────────────┘     ║            │
│    ║                                                            ║            │
│    ╚═══════════════════════════════════════════════════════════╝            │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘

                                    ↓

┌─────────────────────────────────────────────────────────────────────────────┐
│  STEP 3: Full Profile Modal Opens                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│    ╔═══════════════════════════════════════════════════════════════════╗    │
│    ║  UserProfileModal                                                  ║    │
│    ║  (/src/components/modals/UserProfileModal.tsx)                    ║    │
│    ╠═══════════════════════════════════════════════════════════════════╣    │
│    ║                                                                     ║    │
│    ║  ┌────────────────────────────────────────────────────────────┐   ║    │
│    ║  │          Gradient Cover Image                            │   ║    │
│    ║  └────────────────────────────────────────────────────────────┘   ║    │
│    ║         ┌──────┐                                                   ║    │
│    ║         │Avatar│   John Doe                                       ║    │
│    ║         │    │   @johndoe                                      ║    │
│    ║         └──────┘   [Admin] [Rank #5]  14                       ║    │
│    ║                                                                     ║    │
│    ║  Bio: Full-stack developer passionate about...                    ║    │
│    ║                                                                     ║    │
│    ║   john@example.com   SF   Tech Corp   Website   GitHub ║    │
│    ║                                                                     ║    │
│    ║  ┌────────────────────────────────────────────────────────────┐   ║    │
│    ║  │            STATISTICS GRID (8 Cards)                     │   ║    │
│    ║  ├──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┤   ║    │
│    ║  │ 12   │ 15   │  3   │  5   │ 24   │ 18   │ 342  │ 2450 │   ║    │
│    ║  │Proj. │Events│Prod. │Cours │Chall.│Award │Likes │Point │   ║    │
│    ║  └──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘   ║    │
│    ║                                                                     ║    │
│    ║  ┌────────────────────────────────────────────────────────────┐   ║    │
│    ║  │ [Overview] [Projects] [Events] [Products] [Courses] []  │   ║    │
│    ║  └────────────────────────────────────────────────────────────┘   ║    │
│    ║                                                                     ║    │
│    ║  ┌────────────────────────────────────────────────────────────┐   ║    │
│    ║  │          TAB CONTENT AREA                                  │   ║    │
│    ║  │                                                             │   ║    │
│    ║  │  • Overview: Recent Activity Timeline                      │   ║    │
│    ║  │  • Projects: All user projects with status                 │   ║    │
│    ║  │  • Events: Participated/organized events                   │   ║    │
│    ║  │  • Products: Created/sold products                         │   ║    │
│    ║  │  • Courses: Enrolled/completed courses                     │   ║    │
│    ║  │  • Achievements: Badges and awards                         │   ║    │
│    ║  │                                                             │   ║    │
│    ║  └────────────────────────────────────────────────────────────┘   ║    │
│    ║                                                                     ║    │
│    ╚═══════════════════════════════════════════════════════════════════╝    │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────────┐
│                        COMPONENT HIERARCHY                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│    Team.tsx                                                                  │
│    ├── State Management                                                      │
│    │   ├── selectedMember                                                    │
│    │   ├── showQuickModal                                                    │
│    │   ├── showFullProfileModal                                             │
│    │   └── selectedUserId                                                    │
│    │                                                                          │
│    ├── Event Handlers                                                        │
│    │   ├── handleMemberClick()                                               │
│    │   ├── handleViewFullProfile()                                          │
│    │   ├── handleCloseQuickModal()                                          │
│    │   └── handleCloseFullProfileModal()                                    │
│    │                                                                          │
│    └── Child Components                                                      │
│        ├── UserQuickModal                                                    │
│        │   ├── Props: isOpen, onClose, user, onViewFullProfile             │
│        │   └── Displays: Avatar, Bio, Contact, CTA Button                   │
│        │                                                                      │
│        └── UserProfileModal                                                  │
│            ├── Props: isOpen, onClose, userId, initialUserData             │
│            ├── Header: Avatar, Stats, Bio, Contact                          │
│            ├── Stats Grid: 8 statistical cards                              │
│            └── Tabs: Overview, Projects, Events, Products, etc.             │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────────┐
│                          DATA FLOW                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│    ┌──────────┐                                                             │
│    │  Click   │                                                             │
│    │  Event   │                                                             │
│    └────┬─────┘                                                             │
│         │                                                                     │
│         ↓                                                                     │
│    ┌─────────────────┐                                                      │
│    │ Convert to      │                                                      │
│    │ UserData format │                                                      │
│    └────┬────────────┘                                                      │
│         │                                                                     │
│         ↓                                                                     │
│    ┌─────────────────┐       ┌──────────────────┐                          │
│    │ setSelectedUser │──────▶│ UserQuickModal   │                          │
│    │ setShowQuickModal│       │ (Basic Info)     │                          │
│    └─────────────────┘       └──────┬───────────┘                          │
│                                      │                                        │
│                                      │ Click "See Full Profile"              │
│                                      │                                        │
│                                      ↓                                        │
│                              ┌───────────────────┐                          │
│                              │ setUserId         │                          │
│                              │ setShowFullModal  │                          │
│                              └───────┬───────────┘                          │
│                                      │                                        │
│                                      ↓                                        │
│                              ┌───────────────────┐                          │
│                              │ API Call:         │                          │
│                              │ getUserProfile()  │                          │
│                              └───────┬───────────┘                          │
│                                      │                                        │
│                                      ↓                                        │
│                              ┌───────────────────────────┐                  │
│                              │ UserProfileComplete       │                  │
│                              │ - UserData                │                  │
│                              │ - Stats                   │                  │
│                              │ - Projects[]              │                  │
│                              │ - Events[]                │                  │
│                              │ - Products[]              │                  │
│                              │ - Courses[]               │                  │
│                              │ - Achievements[]          │                  │
│                              │ - Activity[]              │                  │
│                              └───────┬───────────────────┘                  │
│                                      │                                        │
│                                      ↓                                        │
│                              ┌───────────────────┐                          │
│                              │ UserProfileModal  │                          │
│                              │ (Full History)    │                          │
│                              └───────────────────┘                          │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────────┐
│                         TYPE DEFINITIONS                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│    UserData (base from user.ts)                                             │
│    ├── id, email, username, role                                            │
│    ├── name, login, avatar                                                   │
│    └── bio, location, company, blog, github                                 │
│                                                                               │
│    UserProfileComplete (extends UserData)                                    │
│    ├── stats: UserStats                                                     │
│    │   ├── total_projects, completed_projects                               │
│    │   ├── total_events_attended                                            │
│    │   ├── total_products                                                    │
│    │   ├── total_courses_completed                                          │
│    │   ├── total_challenges_completed                                       │
│    │   ├── total_achievements                                               │
│    │   ├── total_likes_given, total_likes_received                          │
│    │   ├── total_points                                                      │
│    │   ├── rank                                                              │
│    │   └── streak_days                                                       │
│    │                                                                          │
│    ├── projects: UserProject[]                                              │
│    │   ├── id, title, description, status                                   │
│    │   ├── likes, views, tags, technologies                                 │
│    │   └── github_link, live_url, dates                                     │
│    │                                                                          │
│    ├── events: UserEvent[]                                                  │
│    │   ├── event_id, title, description                                     │
│    │   ├── participation_status, role                                       │
│    │   └── dates, certificate_url                                           │
│    │                                                                          │
│    ├── products: UserProduct[]                                              │
│    │   ├── id, name, description, price                                     │
│    │   ├── category, status, stock                                          │
│    │   └── sales_count, created_at                                          │
│    │                                                                          │
│    ├── courses: UserCourse[]                                                │
│    │   ├── course_id, title, description                                    │
│    │   ├── progress, status, instructor                                     │
│    │   └── dates, certificate_url                                           │
│    │                                                                          │
│    ├── challenges: UserChallenge[]                                          │
│    │   ├── challenge_id, title, difficulty                                  │
│    │   ├── status, points_earned                                            │
│    │   └── attempts, best_score, completion_date                            │
│    │                                                                          │
│    ├── achievements: UserAchievement[]                                      │
│    │   ├── id, title, description                                           │
│    │   ├── icon, category, rarity                                           │
│    │   └── earned_date                                                       │
│    │                                                                          │
│    ├── likes: UserLike[]                                                    │
│    │   ├── project_id, project_title                                        │
│    │   ├── product_id, product_name                                         │
│    │   └── liked_at                                                          │
│    │                                                                          │
│    └── recent_activity: UserActivity[]                                      │
│        ├── type, title, description                                         │
│        ├── timestamp                                                         │
│        └── metadata                                                          │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────────┐
│                         STYLING LAYERS                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│    UserQuickModal.css                                                        │
│    ├── .user-quick-modal-content                                            │
│    ├── .user-quick-header                                                   │
│    ├── .user-quick-avatar                                                   │
│    ├── .role-badge (admin/moderator/user)                                   │
│    ├── .user-quick-details                                                  │
│    ├── .details-grid                                                        │
│    ├── .detail-item (with hover effects)                                    │
│    └── .btn-view-full-profile                                               │
│                                                                               │
│    UserProfileModal.css                                                      │
│    ├── .user-profile-modal-overlay                                          │
│    ├── .user-profile-modal-container                                        │
│    ├── .user-profile-cover (animated gradient)                              │
│    ├── .user-profile-avatar                                                 │
│    ├── .streak-badge (pulse animation)                                      │
│    ├── .role-badge, .rank-badge                                             │
│    ├── .user-stats-grid (8 cards)                                           │
│    ├── .stat-card (hover effects)                                           │
│    ├── .user-profile-tabs                                                   │
│    ├── .tab-button (active states)                                          │
│    └── .tab-content-* (overview, projects, etc.)                            │
│                                                                               │
│    sections.css (Team section)                                              │
│    ├── .team-card-clickable                                                 │
│    │   └── hover: translateY(-8px)                                          │
│    └── .team-avatar                                                         │
│        └── hover: scale(1.1) rotate(5deg)                                   │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────────┐
│                    RESPONSIVE BEHAVIOR                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│    Desktop (> 768px)          Tablet (480-768px)       Mobile (< 480px)     │
│    ┌─────────────────┐        ┌──────────────┐        ┌─────────┐          │
│    │ ┌─┬─┬─┬─┐       │        │ ┌──┬──┐      │        │ ┌─────┐ │          │
│    │ │ │ │ │ │ Stats │        │ │  │  │Stats │        │ │     │ │          │
│    │ ├─┼─┼─┼─┤       │        │ ├──┼──┤      │        │ │Stats│ │          │
│    │ │ │ │ │ │ Grid  │        │ │  │  │Grid  │        │ │     │ │          │
│    │ └─┴─┴─┴─┘       │        │ └──┴──┘      │        │ │Grid │ │          │
│    │                  │        │              │        │ └─────┘ │          │
│    │ Multi-column     │        │ 2 columns    │        │ 1 column│          │
│    │ Large fonts      │        │ Medium fonts │        │ Small   │          │
│    │ Full width       │        │ Adjusted     │        │ Stacked │          │
│    └─────────────────┘        └──────────────┘        └─────────┘          │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘


Legend:
  ┌─┐  UI Container       →  Data Flow         ║  Modal Window
  ├─┤  Component          ↓  User Action       ╔═╗ Important
  └─┘  Element            ◄─ Click/Interact    ╚═╝ Section
```
