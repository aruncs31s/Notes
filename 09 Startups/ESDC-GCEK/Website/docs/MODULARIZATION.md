# Project Modularization Architecture

## Overview

The project has been reorganized into a modular architecture to improve scalability, maintainability, and code organization. This document outlines the new structure.

## New Project Structure

```
src/
├── modules/                          # Core feature modules
│   ├── courses/                      # LMS & Course Module
│   │   ├── components/               # Course-specific components
│   │   │   ├── VideoPlayer.tsx
│   │   │   ├── ChapterCard.tsx
│   │   │   ├── ModuleSection.tsx
│   │   │   └── index.ts
│   │   ├── pages/                    # Course pages
│   │   │   └── CourseDetail.tsx
│   │   ├── services/                 # Business logic
│   │   │   └── courseService.ts
│   │   ├── hooks/                    # Custom React hooks
│   │   │   └── useCourseProgress.ts
│   │   ├── types/                    # TypeScript types
│   │   │   └── index.ts
│   │   ├── styles/                   # Module-scoped styles
│   │   │   └── courseDetail.css
│   │   └── index.ts                  # Module barrel export
│   │
│   ├── auth/                         # Authentication Module
│   │   ├── components/               # Auth components
│   │   │   ├── Login.tsx
│   │   │   ├── Register.tsx
│   │   │   └── index.ts
│   │   ├── services/                 # Auth services
│   │   │   └── authService.ts
│   │   ├── hooks/                    # Auth hooks
│   │   │   └── useAuth.ts
│   │   ├── types/                    # Auth types
│   │   │   └── auth.ts
│   │   └── index.ts
│   │
│   ├── user/                         # User Module
│   │   ├── components/               # User components
│   │   │   ├── UserProfile.tsx
│   │   │   ├── ProfileCard.tsx
│   │   │   └── index.ts
│   │   ├── pages/                    # User pages
│   │   │   ├── ProfilePage.tsx
│   │   │   └── UserProjectsPage.tsx
│   │   ├── services/                 # User services
│   │   │   └── userService.ts
│   │   ├── hooks/                    # User hooks
│   │   │   └── useUserProfile.ts
│   │   └── index.ts
│   │
│   └── shared/                       # Shared Module
│       ├── components/               # Global components
│       │   ├── Navbar.tsx
│       │   ├── Footer.tsx
│       │   ├── DockSidebar.tsx
│       │   └── index.ts
│       ├── hooks/                    # Shared hooks
│       │   ├── useTheme.ts
│       │   ├── useSettings.ts
│       │   └── index.ts
│       ├── utils/                    # Utility functions
│       │   ├── helpers.ts
│       │   ├── constants.ts
│       │   └── index.ts
│       └── index.ts
│
├── contexts/                         # Global context providers (unchanged)
├── pages/                            # Legacy pages (being migrated)
├── components/                       # Legacy components (being migrated)
├── styles/                           # Global styles
├── App.tsx                           # Main app routing
└── main.tsx                          # Entry point
```

## Module Architecture Benefits

### 1. **Encapsulation**
Each module is self-contained with its own:
- Components
- Services (business logic)
- Hooks
- Types
- Styles

### 2. **Scalability**
New features can be added as complete modules without affecting existing code:
```
modules/
├── courses/
├── auth/
├── user/
├── shared/
├── marketplace/  (NEW)
├── notifications/ (NEW)
└── admin/       (NEW)
```

### 3. **Reusability**
Modules export barrel files (`index.ts`) for clean imports:
```typescript
// Instead of:
import { CourseService } from '../../../services/courseService';
import { useCourseProgress } from '../../../hooks/useCourseProgress';
import { VideoPlayer } from '../../../components';

// Use:
import { CourseService, useCourseProgress, VideoPlayer } from '@/modules/courses';
```

### 4. **Maintainability**
Related code is colocated:
- Types are defined in the module
- Services handle business logic
- Components are display logic
- Hooks manage state and effects

## Migration Path

### Phase 1: Core Modules (COMPLETED)
- ✅ Courses Module - LMS functionality with chapter-based learning

### Phase 2: In Progress
- ⏳ Auth Module - Login, Register, authentication
- ⏳ User Module - Profile, projects
- ⏳ Shared Module - Common components

### Phase 3: Future
- Marketplace Module
- Notifications Module
- Admin Module
- Settings Module

## Usage Examples

### Importing from Modules

```typescript
// Courses Module
import {
  CourseDetailPage,
  CourseService,
  useCourseProgress,
  VideoPlayer,
  type Course,
  type Chapter,
} from '@/modules/courses';

// Auth Module
import {
  LoginComponent,
  AuthService,
  useAuth,
  type AuthUser,
} from '@/modules/auth';

// User Module
import {
  UserProfileComponent,
  UserService,
  useUserProfile,
  type UserProfile,
} from '@/modules/user';

// Shared Module
import {
  Navbar,
  Footer,
  useTheme,
  type Theme,
} from '@/modules/shared';
```

### Service Usage

```typescript
// In a component
import { useCourseProgress } from '@/modules/courses';

export function CourseView() {
  const {
    progress,
    markVideoWatched,
    getProgressPercentage,
  } = useCourseProgress(courseId);

  return (
    <div>
      <ProgressBar percentage={getProgressPercentage()} />
    </div>
  );
}
```

## Module Development Guidelines

### 1. **File Organization**
```
module/
├── components/     # Reusable UI components
├── pages/          # Page-level components
├── services/       # Business logic & API calls
├── hooks/          # Custom React hooks
├── types/          # TypeScript interfaces
├── styles/         # CSS files
└── index.ts        # Public API
```

### 2. **Type Definitions**
Keep types in `types/index.ts`:
```typescript
// modules/courses/types/index.ts
export interface Course { ... }
export interface Chapter { ... }
export type CourseProgress = { ... }
```

### 3. **Services**
Put business logic in services:
```typescript
// modules/courses/services/courseService.ts
export class CourseService {
  static getCourseById(id: number): Course | undefined { ... }
  static saveCourseProgress(progress: CourseProgress): void { ... }
}
```

### 4. **Hooks**
Create custom hooks for state management:
```typescript
// modules/courses/hooks/useCourseProgress.ts
export function useCourseProgress(courseId: number) {
  const [progress, setProgress] = useState<CourseProgress | null>(null);
  // ... hook logic
  return { progress, markVideoWatched, ... };
}
```

### 5. **Barrel Exports**
Always export public API from `index.ts`:
```typescript
// modules/courses/index.ts
export { default as CourseDetailPage } from './pages/CourseDetail';
export { CourseService } from './services/courseService';
export { useCourseProgress } from './hooks/useCourseProgress';
export type { Course, Chapter, CourseProgress } from './types';
```

## Routing Migration

### Old Structure (App.tsx)
```typescript
import CourseDetail from './pages/CourseDetail';
```

### New Structure (App.tsx)
```typescript
import { CourseDetailPage } from '@/modules/courses';

<Route path="/course/:id" element={<CourseDetailPage />} />
```

## Alias Configuration

To use `@/` imports, configure `tsconfig.json`:

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  }
}
```

## Best Practices

1. **Keep modules independent** - Avoid circular dependencies
2. **Use barrel exports** - All public APIs through `index.ts`
3. **Type everything** - Use TypeScript for better DX
4. **Colocate related code** - Put related files in same module
5. **Separate concerns** - Services for logic, components for UI
6. **Document modules** - Add README.md in each module
7. **Use hooks for state** - Avoid prop drilling with custom hooks
8. **Test modules independently** - Each module can be tested in isolation

## Migration Checklist

- [x] Courses Module created
- [ ] Auth Module migration
- [ ] User Module migration
- [ ] Shared Module creation
- [ ] Update App.tsx routing
- [ ] Update all imports
- [ ] Remove duplicate code
- [ ] Update tests
- [ ] Update documentation
