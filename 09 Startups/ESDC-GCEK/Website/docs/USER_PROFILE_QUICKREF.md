# User Profile Feature - Quick Reference

##  Quick Start

### What Was Implemented?

A complete user profile system that allows users to click on team members and view their:

- **Basic Info**: Name, role, contact details, bio
- **Complete History**: Projects, events, products, courses, challenges, achievements, likes
- **Statistics**: Total counts for all activities
- **Activity Timeline**: Recent user activities

---

##  Files Created

1. **Types**: `/src/types/userProfile.ts`
   - Extended user profile type definitions
   - Interfaces for projects, events, products, courses, etc.

2. **Components**:
   - `/src/components/modals/UserQuickModal.tsx` - Quick preview modal
   - `/src/components/modals/UserProfileModal.tsx` - Full profile with tabs

3. **Styles**:
   - `/src/styles/UserQuickModal.css`
   - `/src/styles/UserProfileModal.css`

4. **Documentation**:
   - `/docs/USER_PROFILE_FEATURE.md` - Complete implementation guide

##  Files Modified

1. `/src/components/Team.tsx`
   - Added click handlers for team members
   - Integrated modals
   - State management for modal visibility

2. `/src/styles/sections.css`
   - Added `.team-card-clickable` styles
   - Hover effects and animations

---

##  How It Works

### User Flow:

```
User clicks team member card
    ↓
UserQuickModal opens (basic info)
    ↓
User clicks "See Full Profile"
    ↓
UserProfileModal opens (complete history with tabs)
```

### Component Structure:

```
Team Component
├── UserQuickModal
│   ├── Basic Info Section
│   ├── Contact Details
│   └── "See Full Profile" Button
│
└── UserProfileModal
    ├── Header (Avatar, Stats, Bio)
    ├── Tabs Navigation
    └── Tab Content
        ├── Overview (Activity)
        ├── Projects
        ├── Events
        ├── Products
        ├── Courses
        └── Achievements
```

---

##  Usage Example

```typescript
import { useState } from 'react';
import UserQuickModal from './modals/UserQuickModal';
import UserProfileModal from './modals/UserProfileModal';

const YourComponent = () => {
  const [selectedUser, setSelectedUser] = useState<UserData | null>(null);
  const [showQuickModal, setShowQuickModal] = useState(false);
  const [showFullModal, setShowFullModal] = useState(false);
  const [userId, setUserId] = useState<string | null>(null);

  const handleUserClick = (user: UserData) => {
    setSelectedUser(user);
    setShowQuickModal(true);
  };

  const handleViewFullProfile = (userId: string) => {
    setUserId(userId);
    setShowFullModal(true);
  };

  return (
    <>
      <div onClick={() => handleUserClick(userData)}>
        {/* User card */}
      </div>

      {selectedUser && (
        <UserQuickModal
          isOpen={showQuickModal}
          onClose={() => setShowQuickModal(false)}
          user={selectedUser}
          onViewFullProfile={handleViewFullProfile}
        />
      )}

      {userId && (
        <UserProfileModal
          isOpen={showFullModal}
          onClose={() => setShowFullModal(false)}
          userId={userId}
          initialUserData={selectedUser}
        />
      )}
    </>
  );
};
```

---

##  UI Features

### UserQuickModal

-  Clean, minimalist design
-  Avatar with role badge
-  Contact information grid
-  Responsive layout
-  Call-to-action button

### UserProfileModal

-  Gradient cover image
-  Large profile avatar with streak badge
-  8 statistical cards
-  Tab-based navigation (6 tabs)
-  Smooth animations
-  Fully responsive design
-  Keyboard accessible (Escape to close)

---

##  Backend Integration (TODO)

### Required API Endpoints:

```typescript
// Get complete user profile
GET /api/users/:userId/profile

// Response:
{
  "success": true,
  "data": {
    "id": "123",
    "username": "johndoe",
    "email": "john@example.com",
    "stats": { /* UserStats */ },
    "projects": [ /* UserProject[] */ ],
    "events": [ /* UserEvent[] */ ],
    "products": [ /* UserProduct[] */ ],
    "courses": [ /* UserCourse[] */ ],
    "achievements": [ /* UserAchievement[] */ ],
    "recent_activity": [ /* UserActivity[] */ ]
  }
}
```

### Update ApplicationService:

```typescript
// In src/application/ApplicationService.ts

async getUserProfile(userId: string): Promise<UserProfileComplete> {
  const response = await this.api.get(`/api/users/${userId}/profile`);
  return response.data.data;
}
```

### Update UserProfileModal:

Replace mock data with:

```typescript
const profile = await applicationService.getUserProfile(userId);
setUserProfile(profile);
```

---

##  Stats Displayed

1. **Projects**: Total and completed projects
2. **Events**: Events attended/organized
3. **Products**: Products created/sold
4. **Courses**: Courses completed
5. **Challenges**: Coding challenges solved
6. **Achievements**: Badges and awards
7. **Likes**: Likes given and received
8. **Points**: Total points earned
9. **Rank**: Leaderboard position
10. **Streak**: Consecutive active days

---

##  Responsive Design

### Breakpoints:

- **Mobile** (< 480px): Single column, stacked layout
- **Tablet** (480px - 768px): 2-column grid
- **Desktop** (> 768px): Full multi-column layout

---

##  Current Status

###  Completed:

- All type definitions
- Both modal components
- Team integration
- Complete styling
- Documentation

###  Pending (Backend):

- API integration
- Real data for all tabs
- Activity timeline
- Stats calculation

###  Future Features:

- Follow/unfollow users
- Direct messaging
- Share profile
- Export data
- Privacy settings

---

##  Common Issues & Solutions

### Modal not opening?

- Check `isOpen` prop is `true`
- Verify state management
- Check console for errors

### Data not showing?

- Verify UserData format
- Check userId is passed correctly
- Review API response structure

### Styling broken?

- Import CSS files
- Check CSS variables defined
- Verify z-index values

---

##  Key Props

### UserQuickModal:

```typescript
{
  isOpen: boolean;          // Modal visibility
  onClose: () => void;      // Close handler
  user: UserData;           // User data
  onViewFullProfile: (userId: string) => void; // Full profile handler
}
```

### UserProfileModal:

```typescript
{
  isOpen: boolean;          // Modal visibility
  onClose: () => void;      // Close handler
  userId: string;           // User ID to fetch
  initialUserData?: UserData; // Optional prefetch data
}
```

---

##  Related Components

Can be integrated with:

- Contributors lists
- Leaderboards
- Search results
- User mentions
- Comments sections
- Project teams
- Event participants

---

##  Additional Resources

- Full Documentation: `/docs/USER_PROFILE_FEATURE.md`
- Type Definitions: `/src/types/userProfile.ts`
- Base User Types: `/src/types/user.ts`
- Example Implementation: `/src/components/Team.tsx`

---

**Need Help?**

1. Check the full documentation
2. Review code comments
3. Test with mock data first
4. Verify API when backend is ready

---

_Last Updated: October 15, 2025_
