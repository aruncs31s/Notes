---
aliases: 
Date: 30-06-2025
tags:
  - es_website
  - frontend
---
# 03 Login
>[!blank|right]
>![[login.png|right|250x300]] 



- [[Backend]]
- [[auth]]

Button Located at `src/components/ui/buttons/LoginBtn.astro`
```js
---
const { title = "Log in" } = Astro.props;

interface Props {
  title?: string;
}

const baseClasses =
  "flex items-center gap-x-2 text-base md:text-sm font-medium text-neutral-600 ring-zinc-500 transition duration-300 focus-visible:ring-3 outline-hidden";
const hoverClasses = "hover:text-orange-400 dark:hover:text-orange-300";
const darkClasses =
  "dark:border-neutral-700 dark:text-neutral-400 dark:ring-zinc-200 dark:focus:outline-hidden";
const mdClasses = "md:my-6 md:border-s md:border-neutral-300 md:ps-6";
const txtSizeClasses = "2xl:text-base";
const userSVG = `<svg
      class="h-4 w-4 shrink-0"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
  >
    <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path>
    <circle cx="12" cy="7" r="4"></circle>
  </svg>`;
---

<button
  type="button"
  class={`${baseClasses} ${hoverClasses} ${darkClasses} ${mdClasses} ${txtSizeClasses}`}
  data-hs-overlay="#hs-toggle-between-modals-login-modal"
>
  <!-- About Fragment: https://docs.astro.build/en/basics/astro-syntax/#fragments -->

  <Fragment set:html={userSVG} />
  {title}
</button>

```

- code fence marked by triple dashes ---  -> component script" or "frontmatter" section
- This section contains JavaScript/TypeScript code that runs on the server during build time
1. Component Script
2. Scope Isolation
```js
---
---
```

```js
const { title = "Log in" } = Astro.props;
```
`= "Log in"` sets a default value of "Log in" if no title prop is provided
ie
```js
<LoginBtn title="Sign In" /> // Value Will BE "Sign In"
<LoginBtn /> // Value will be "Log in"
```

```ts
interface Props {
  title?: string;
}
```
1. `interface Props` - Declares a TypeScript interface named "Props" 
2. `title?: string` - Defines a property with:
- Name: `title`
- Type: `string`
- Optional: `?` makes this prop optional
Without this 
```ts
<LoginBtn 
  title={123}          
  wrongProp="test"      
/>
```

>[!Note]- `props`
>props (short for properties) are a way to pass data from a parent component to a child component, Similar to function parameters.

>[!Important]- `interface`
>`interface` keyword is a TypeScript feature that allows you to define a contract for an object's shape
>For example
>```ts
>interface Props {
>title?: string;
>}
>```
>
>- This will create a type definition named `Props`
>- Specifies that any object implementing this interface can have a `title` property
>- The `?` makes the property optional
>- The property must be of type `string` if provided

