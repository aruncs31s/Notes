# Users Screen Documentation

## Overview
The Users Screen manages user profiles and interactions within the AI Voice Assistant application. It provides a comprehensive interface for viewing, searching, adding, and managing users who interact with the assistant.

## File Location
`lib/screens/users_screen.dart`

## Architecture

### Main Components

#### 1. **UsersScreen** (StatefulWidget)
The primary screen widget that displays the user management interface.

**State Management:**
- Uses `Provider` pattern with `AppStateProvider` for state management
- Maintains local state for search functionality
- Automatically refreshes user list on screen initialization

**Key Features:**
- Real-time user search by name or email
- Pull-to-refresh functionality
- User count badge display
- Floating action button for adding new users

#### 2. **_UsersScreenState**
Manages the screen's lifecycle and user interactions.

**Properties:**
- `_searchController`: TextEditingController for search input
- `_searchQuery`: String to store current search query

**Lifecycle Methods:**
- `initState()`: Fetches users when screen loads using post-frame callback
- `dispose()`: Cleans up search controller

**UI Structure:**
```
Scaffold
├── Body (Consumer<AppStateProvider>)
│   ├── Header Section
│   │   ├── Title with user count badge
│   │   ├── Refresh button
│   │   └── Search bar
│   ├── Error Message (conditional)
│   └── Users List
│       ├── Loading indicator
│       ├── Empty state
│       └── ListView of user tiles
└── FloatingActionButton (Add User)
```

#### 3. **_UserTile** (StatelessWidget)
Displays individual user information in a card format.

**Displayed Information:**
- Avatar (initials or image)
- User name
- Email address (if available)
- Total interactions count
- Last activity timestamp

**Features:**
- Clickable card that opens user details dialog
- Avatar with fallback to initials
- Relative timestamp formatting (e.g., "2h ago", "3d ago")

**Timestamp Formatting Logic:**
- < 1 minute: "Just now"
- < 60 minutes: "Xm ago"
- < 24 hours: "Xh ago"
- < 7 days: "Xd ago"
- ≥ 7 days: "DD/MM/YYYY"

#### 4. **_UserDetailDialog** (StatelessWidget)
Modal dialog showing comprehensive user information.

**Sections:**
- **Header**: User avatar and basic info (name, email)
- **Statistics Cards**:
  - Total conversations count
  - Days active since joining
- **Timestamps**:
  - Account creation date
  - Last interaction date
- **Actions**:
  - View Chats button (navigation placeholder)
  - Delete button with confirmation

**Delete Flow:**
1. User clicks Delete button
2. Confirmation dialog appears
3. On confirmation, calls `provider.deleteUser()`
4. Closes both dialogs

#### 5. **_AddUserDialog** (StatefulWidget)
Form dialog for creating new users.

**Form Fields:**
- **Name** (required): User's display name
- **Username** (required): Unique username
- **Email** (optional): Email address with validation

**Validation Rules:**
- Name: Cannot be empty
- Username: Cannot be empty
- Email: Must match email regex pattern if provided

**Submission Flow:**
1. Validates form inputs
2. Creates User object with current timestamp
3. Calls API service to create user on backend
4. Adds user to local state via `provider.addUser()`
5. Closes dialog on success
6. Shows error snackbar on API failure

## Data Flow

### User Loading
```
Screen Init → AppStateProvider.refreshUsers() → API/Database → Update UI
```

### User Search
```
User Input → Update _searchQuery → Filter users list → Rebuild UI
```

### User Creation
```
Form Submit → Validate → ApiService.createUser() → AppStateProvider.addUser() → Refresh UI
```

### User Deletion
```
Delete Click → Confirmation → AppStateProvider.deleteUser() → API/Database → Refresh UI
```

## State Management

### AppStateProvider Integration
The screen consumes the following from AppStateProvider:
- `users`: List of all users
- `isLoading`: Loading state indicator
- `error`: Error message string
- `refreshUsers()`: Refresh user list
- `addUser(User)`: Add new user
- `deleteUser(int)`: Delete user by ID
- `clearError()`: Clear error state

### Local State
- Search query and controller managed locally
- Form inputs in AddUserDialog managed locally

## UI/UX Features

### Search Functionality
- Real-time filtering as user types
- Searches both name and email fields
- Case-insensitive matching
- Clear button appears when query is active

### Empty States
Two variants:
1. **No users exist**: Shows "Add User" button
2. **No search results**: Shows "Try adjusting your search query"

### Error Handling
- Displays error banner at top of screen
- Red-themed alert with error icon
- Dismissible via close button
- API errors shown via snackbar

### Loading States
- Circular progress indicator with "Loading users..." text
- Only shown when loading AND no cached users exist
- Pull-to-refresh available when users are displayed

### Visual Design
- Catppuccin theme colors throughout
- Card-based layout for user tiles
- Rounded corners and consistent spacing
- Color-coded icons (pink for users, blue for stats, etc.)

## API Integration

### ApiService Usage
```dart
final apiService = ApiService();
apiService.createUser(
  name: name,
  username: username,
  email: email,
);
```

**Error Handling:**
- Try-catch block around API calls
- User-friendly error messages via SnackBar
- Prevents local state update on API failure

## Dependencies

### External Packages
- `flutter/material.dart`: UI framework
- `provider`: State management
- `ai_voice_assistant/services/api_service.dart`: Backend API calls

### Internal Dependencies
- `../providers/app_state_provider.dart`: Global state
- `../models/user.dart`: User data model
- `../themes/catppuccin_theme.dart`: Theme colors

## User Model Requirements

The screen expects User model with:
- `id`: Unique identifier (nullable)
- `name`: Display name
- `username`: Unique username
- `email`: Email address (nullable)
- `avatarPath`: Avatar image path (nullable)
- `totalInteractions`: Conversation count
- `lastInteractionAt`: Last activity timestamp
- `createdAt`: Account creation timestamp (nullable)

## Future Enhancements

### Placeholder Functionality
- "View Chats" button currently has no implementation
- Could navigate to filtered conversation screen

### Potential Improvements
- Avatar upload functionality
- User profile editing
- Bulk user operations
- Export user data
- Advanced filtering options
- Sorting capabilities

## Best Practices Demonstrated

1. **Separation of Concerns**: UI components split into focused widgets
2. **State Management**: Proper use of Provider pattern
3. **Form Validation**: Comprehensive input validation
4. **Error Handling**: User-friendly error messages
5. **Responsive Design**: Adapts to different screen sizes
6. **Accessibility**: Semantic icons and labels
7. **Code Reusability**: Extracted widgets for common patterns
8. **Clean Code**: Clear naming and organization
