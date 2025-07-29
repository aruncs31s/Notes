# Bitbucket 
How to clone Private

1. Generate an SSH key pair if you haven't already:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

2. Add the public key to your Bitbucket account:
   - Copy the contents of ~/. Ssh/id_ed 25519. Pub
   - Go to Bitbucket settings > SSH keys > Add key
   - Paste the key and save

3. Clone the repository using SSH:

```bash
git clone git@bitbucket.org:username/repo.git
```

Replace username and repo with your Bitbucket username and repository name.

