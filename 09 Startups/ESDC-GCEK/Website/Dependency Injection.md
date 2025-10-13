---
dg-publish: true
---

# Dependency Injection

>[!summary]+ Summary
>- Dependency Injection (DI) is a design pattern used to implement IoC, allowing for better separation of concerns and easier testing.
>- In a DDD context, DI helps manage dependencies between domain services, repositories, and use cases, promoting a clean architecture.
>- By using a DI container, we can inject the required dependencies into our classes, making them more modular and easier to maintain.

>[!explanation]- Explanation
>Imagine you're building a house. Instead of each room handling its own plumbing and electricity, you have a central system that provides water and power to wherever it's needed. That's kind of like Dependency Injection (DI) in software—it's a way to supply the tools and services a part of your code needs without that code having to create them itself.
>In Domain-Driven Design (DDD), we focus on modeling our software around the real-world business problems it solves. Dependency Injection (DI) helps us keep things loosely connected, which means it avoids tight coupling between different parts of the code, making it easier to test, maintain, and change. It's part of Inversion of Control (IoC), where instead of your code reaching out for dependencies, they're handed to it.

>[!note]- Container
>In a DDD app, a container (like a toolbox) manages these dependencies—repositories for data, services for business logic—and injects them into your use cases or entities. This reduces tight coupling, so if you swap out a database, the rest of your code doesn't break.

### Why Dependency Injection Matters is used
- **Separation of Concerns**: DI helps keep different parts of your application independent, making it easier to manage and understand.
- **Testability**: By injecting dependencies, you can easily replace them with mock versions during testing, allowing for isolated unit tests.
- **Flexibility**: DI allows you to change implementations without modifying the dependent code, making it easier to adapt to new requirements or technologies.
- **Maintainability**: With DI, your code is cleaner and more organized, making it easier to maintain and extend over time.

### Imports
```ts
import userRepository from '../infrastructure/repositories/UserRepository.js';
import projectRepository from '../infrastructure/repositories/ProjectRepository.js';
import eventRepository from '../infrastructure/repositories/EventRepository.js';
import chatbotRepository from '../infrastructure/repositories/ChatbotRepository.js';

import { UserRegistrationService } from '../domain/services/UserRegistrationService.js';
import { LeaderboardService } from '../domain/services/LeaderboardService.js';
import { ChatbotService } from '../domain/services/ChatbotService.js';

import { CreateUserUseCase } from '../application/use-cases/users/CreateUserUseCase.js';
import { UpdateUserUseCase } from '../application/use-cases/users/UpdateUserUseCase.js';
import { DeleteUserUseCase } from '../application/use-cases/users/DeleteUserUseCase.js';
import { GetAllUsersUseCase } from '../application/use-cases/users/GetAllUsersUseCase.js';

import { CreateProjectUseCase } from '../application/use-cases/projects/CreateProjectUseCase.js';
import { AskChatbotUseCase } from '../application/use-cases/AskChatbotUseCase.js';
```

**Repositories**: Think of these as friendly librarians who fetch and store data from databases or external sources, like UserRepository or ProjectRepository.

**Domain Services**: These are the smart helpers that handle complex business rules, free from UI or framework details—examples include UserRegistrationService or LeaderboardService.

**Use Cases**: These are the action heroes of your app, orchestrating everything to get things done, like CreateUserUseCase or AskChatbotUseCase, pulling in repositories and services as needed.