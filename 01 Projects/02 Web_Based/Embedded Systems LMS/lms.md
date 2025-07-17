---
id: lms
aliases: 
tags:
  - project
  - es_website
  - lms
---

## Features Needed

* User Accounts: Who is taking the course?
* Progress Tracking: Which lessons has അവര്‍ completed?
* Assessments: Quizzes, assignments, and grades.
* Enrollment: Which courses is a user signed up for?
* Dashboards: A personal page for users to see their progress.


1. Showcasing old projects
2. Showcase currently Working Projects

- Broken 

```js
export async function getStaticPaths() {
  const coursePosts = await getCollection("course");
  const paths = coursePosts
    .filter((post) => post.slug)
    .map((post) => {
      return {
        params: { id: post.slug },
        props: { post },
      };
    });
  console.log("Generated paths:", paths);
  return paths;
}
```
- The one `/project` uses
```js
export async function getStaticPaths() {
  const productEntries = await getCollection("projects");
  return productEntries.map((product) => {
    return {
      params: { id: product.id },
      props: { product },
    };
  });
}
```

- Fixed
```js
// Update getStaticPaths for English posts
export async function getStaticPaths() {
  const coursePosts = await getCollection("course");
  return coursePosts.map((post) => {
    return {
      params: { id: post.id },
      props: { post },
    };
  });
}

// Get the current post's data
const { post } = Astro.props;

```

 