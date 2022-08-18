# GIT GUIDLINE

[REF](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)

## Git Init

````bash
cd /src/Aznose/frontend/
git init
```bash
copy create a new repository on the command line

## Initializing a Repository in an Existing Directory

```bash
echo "# jwt-frontend" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/lamit2708/jwt-frontend.git
git push -u origin main
````

## Delete Repos

[REF](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository)
Repo>Settings>Danger Zone

## Git error rename failed

```bash
$ git branch -M main
error: refname refs/heads/master not found
fatal: Branch rename failed
```

I deleted the repo, and started all over again, and it come right. thanks
