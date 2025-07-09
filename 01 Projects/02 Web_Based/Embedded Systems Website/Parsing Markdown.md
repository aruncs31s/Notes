# Parsing MarkDown

```ts
glob({ pattern: '**/[^_]*.{md,mdx}', base: "./src/content/projects/en" }),
```

✅ Match: post.md, blog/post.md, nested/deep/post.mdx
❌ Exclude: _draft.md , _hidden/post.md, blog/_private.mdx


```ts
schema: ({ image }) => z.object({})
```
