# Architecture Decision Records (ADR)

This document tracks important architectural decisions and the reasoning behind them.

---

## ADR-001: Adopt Domain-Driven Design

**Status**:  Accepted  
**Date**: October 2025  
**Deciders**: Development Team

### Context

The ESDC Frontend was growing in complexity with business logic scattered across components. We needed a clear architectural pattern to:

- Organize code better
- Make the codebase more maintainable
- Enable easier testing
- Support future growth
- Separate business logic from UI

### Decision

Adopt Domain-Driven Design (DDD) with strict layered architecture:

- **Domain Layer**: Business logic and domain model
- **Application Layer**: Use cases and orchestration
- **Infrastructure Layer**: External integrations and data access
- **Presentation Layer**: UI components

### Consequences

#### Positive

-  Clear separation of concerns
-  Business logic is testable in isolation
-  Easier to understand and maintain
-  Scalable architecture
-  Domain-focused development
-  Reusable business logic

#### Negative

-  Learning curve for team members
-  More files and structure
-  Initial setup overhead
-  Requires discipline to maintain

#### Neutral

-  Need comprehensive documentation
-  Requires code review enforcement
-  Team training needed

---

## ADR-002: ApplicationService Facade Pattern

**Status**:  Accepted  
**Date**: October 2025  
**Deciders**: Development Team

### Context

With DDD, UI components need a simple way to interact with the domain and infrastructure layers. Direct access to repositories and use cases from UI components would:

- Violate layer boundaries
- Create tight coupling
- Make refactoring difficult
- Lead to inconsistent patterns

### Decision

Create an `ApplicationService` class that acts as a facade for all UI operations:

- Single entry point for UI
- Hides complexity of use cases and repositories
- Consistent API across the application
- Easy to mock for testing

```typescript
import applicationService from '@/application/ApplicationService';

// Simple API
const result = await applicationService.getAllUsers();
const result = await applicationService.createUser(userData);
```

### Consequences

#### Positive

-  Simple API for UI developers
-  Consistent error handling
-  Easy to refactor internals
-  Clear layer boundaries
-  Single source of truth
-  Easy to document

#### Negative

-  Additional abstraction layer
-  Potential for god object if not managed

#### Mitigation

- Keep ApplicationService as thin coordinator
- Delegate to specific use cases
- Document all methods clearly

---

## ADR-003: Value Objects for Domain Concepts

**Status**:  Accepted  
**Date**: October 2025  
**Deciders**: Development Team

### Context

Using primitive types (string, number) for domain concepts leads to:

- No validation
- Type confusion (email as string)
- Duplicated validation logic
- Weak domain model
- No encapsulation

### Decision

Create Value Objects for domain concepts:

- `Email` instead of `string`
- `Points` instead of `number`
- `Difficulty` instead of `string`
- `DateRange` instead of separate dates

```typescript
//  Before
const email: string = 'user@example.com';
const points: number = 100;

//  After
const email = new Email('user@example.com'); // Validates automatically
const points = new Points(100); // Cannot be negative
```

### Consequences

#### Positive

-  Built-in validation
-  Type safety
-  Self-documenting code
-  Encapsulated business rules
-  Immutability
-  Easy to test

#### Negative

-  More classes to manage
-  Learning curve
-  Conversion overhead

#### Neutral

-  Need conversion methods (toString, getValue)
-  Require understanding of value objects

---

## ADR-004: Event-Driven Architecture

**Status**:  Accepted  
**Date**: October 2025  
**Deciders**: Development Team

### Context

Many operations have side effects:

- User creation → send welcome email
- Challenge completion → update leaderboard
- Points awarded → notify user

Coupling these side effects to main business logic leads to:

- Difficult to test
- Hard to modify
- Tight coupling
- Cannot disable side effects easily

### Decision

Implement event-driven architecture using domain events:

- Publish events for significant domain changes
- Subscribe to events for side effects
- Loose coupling between modules

```typescript
// Publish
eventBus.publish({
  eventType: 'UserCreated',
  userId: user.id,
  email: user.email.toString(),
});

// Subscribe
eventBus.subscribe('UserCreated', async (event) => {
  await emailService.sendWelcome(event.userId);
});
```

### Consequences

#### Positive

-  Loose coupling
-  Easy to add/remove side effects
-  Better scalability
-  Clear audit trail
-  Testable in isolation

#### Negative

-  Harder to debug (async flow)
-  Event ordering can be tricky
-  Need monitoring/logging

#### Mitigation

- Log all events
- Document event flow
- Add event tracing in dev mode

---

## ADR-005: Repository Pattern for Data Access

**Status**:  Accepted  
**Date**: October 2025  
**Deciders**: Development Team

### Context

Direct API calls from domain or application layer:

- Creates tight coupling
- Hard to test
- Cannot switch data sources
- Business logic depends on infrastructure

### Decision

Use Repository Pattern:

- Define interfaces in domain layer
- Implement in infrastructure layer
- Inject into use cases
- Abstract data source completely

```typescript
// Interface in domain
interface IUserRepository {
  findById(id: string): Promise<User | null>;
  save(user: User): Promise<void>;
}

// Implementation in infrastructure
class ApiUserRepository implements IUserRepository {
  // API-specific implementation
}
```

### Consequences

#### Positive

-  Loose coupling
-  Easy to test (mock repositories)
-  Can switch data sources
-  Clear abstraction
-  Domain doesn't know about API

#### Negative

-  Additional abstraction
-  More interfaces to maintain
-  Need DTO transformations

#### Neutral

-  Need clear interface definitions
-  Repository methods should be domain-focused

---

## ADR-006: TypeScript Strict Mode

**Status**:  Accepted  
**Date**: October 2025  
**Deciders**: Development Team

### Context

JavaScript/loose TypeScript leads to:

- Runtime errors
- Type confusion
- Hard to refactor
- Poor IDE support

### Decision

Enable TypeScript strict mode:

- `strict: true` in tsconfig
- No implicit any
- Strict null checks
- All types explicit

### Consequences

#### Positive

-  Catch errors at compile time
-  Better IDE support
-  Self-documenting code
-  Easier refactoring
-  Confidence in changes

#### Negative

-  More typing overhead
-  Learning curve
-  Migration effort for existing code

#### Mitigation

- Gradual migration
- Team training
- Type utilities and helpers

---

## ADR-007: TanStack Query for Server State

**Status**:  Accepted  
**Date**: October 2025  
**Deciders**: Development Team

### Context

Managing server state with useState/useEffect:

- Boilerplate code
- No caching
- No background refetching
- Manual loading/error states
- Duplicated logic

### Decision

Use TanStack Query (React Query) for all server state:

- Automatic caching
- Background refetching
- Optimistic updates
- Unified API

```typescript
const { data: users, isLoading } = useQuery({
  queryKey: ['users'],
  queryFn: () => applicationService.getAllUsers(),
});
```

### Consequences

#### Positive

-  Less boilerplate
-  Automatic caching
-  Better UX (background refetching)
-  Unified patterns
-  DevTools for debugging

#### Negative

-  Additional dependency
-  Learning curve
-  Need to understand caching

#### Neutral

-  Need guidelines for cache keys
-  Document invalidation strategies

---

## ADR-008: Tailwind CSS for Styling

**Status**:  Accepted  
**Date**: October 2025  
**Deciders**: Development Team

### Context

CSS-in-JS and traditional CSS have trade-offs:

- CSS-in-JS: Runtime overhead, complex setup
- Traditional CSS: Class naming issues, no tree-shaking
- Need consistent design system
- Want utility-first approach

### Decision

Use Tailwind CSS:

- Utility-first classes
- Custom design system
- Tree-shaking built-in
- Fast development

### Consequences

#### Positive

-  Fast development
-  Consistent design
-  Small bundle size
-  No CSS naming issues
-  Easy to maintain

#### Negative

-  Long class names
-  Learning curve
-  Need custom configuration

#### Mitigation

- Use component abstractions
- Extract common patterns
- Document design system

---

## ADR-009: Monorepo Structure (Future)

**Status**:  Proposed  
**Date**: October 2025  
**Deciders**: TBD

### Context

As project grows, we might want to:

- Share code between frontend and backend
- Split into microservices
- Reuse domain logic
- Separate concerns better

### Decision

Consider migrating to monorepo structure:

- Separate packages for domain, API client, UI
- Shared domain logic
- Better code organization

### Consequences

#### Positive

-  Code sharing
-  Better organization
-  Reusable packages
-  Consistent types

#### Negative

-  Complex setup
-  Build complexity
-  Learning curve

**Status**: Proposed for future consideration

---

## ADR-010: Component Testing Strategy

**Status**:  Accepted  
**Date**: October 2025  
**Deciders**: Development Team

### Context

Need clear testing strategy:

- What to test
- How to test
- Testing library choice
- Coverage goals

### Decision

Adopt testing pyramid:

- **Many unit tests**: Domain entities, value objects, services
- **Some integration tests**: Use cases, repositories
- **Few E2E tests**: Critical user flows

Use Vitest + Testing Library:

- Fast execution
- Good DX
- Easy mocking
- Good IDE support

### Consequences

#### Positive

-  Fast feedback
-  High confidence
-  Good coverage
-  Easy to maintain

#### Negative

-  Time to write tests
-  Need to maintain tests

**Coverage Goal**: 80% for domain layer

---

## Template for New ADRs

When adding a new ADR, use this template:

```markdown
## ADR-XXX: [Title]

**Status**: [Proposed/Accepted/Deprecated/Superseded]
**Date**: [Date]
**Deciders**: [Who made the decision]

### Context

[What is the issue that we're seeing that is motivating this decision or change?]

### Decision

[What is the change that we're proposing and/or doing?]

### Consequences

#### Positive

[What becomes easier?]

#### Negative

[What becomes harder?]

#### Neutral

[What is neither positive nor negative?]
```

---

## Review Schedule

ADRs should be reviewed:

- Quarterly: Check if decisions still valid
- After major changes: Update relevant ADRs
- When onboarding: Share with new team members

---

**Last Updated**: October 2025  
**Maintained By**: ESDC Development Team
