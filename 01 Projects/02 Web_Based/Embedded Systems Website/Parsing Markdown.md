# Parsing MarkDown

```ts
glob({ pattern: '**/[^_]*.{md,mdx}', base: "./src/content/projects/en" }),
```

✅ Match: post.md, blog/post.md, nested/deep/post.mdx
❌ Exclude: _draft.md , _hidden/post.md, blog/_private.mdx


```ts
schema: ({ image }) => z.object({})
```

`z` -> `zod` : TypeScript-first schema validation with static type inference
this is used to provide the following 
- ✅ Valid content
```ts
title: "Hello"
avatar: "./images/pic.jpg"
age: 25
```
- ❌ Invalid content
```ts
title: 123          # Error: must be string
avatar: "nonexistent.jpg"  # Error: image not found
age: "25"          # Error: must be number
```

>[!important]
>The schema acts as a contract that your content must follow to be valid

```ts
title: z.string(),
description: z.string(),
```
