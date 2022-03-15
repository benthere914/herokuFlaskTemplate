echo "user name:"
read userName
echo "Repo Name:"
read repoName
echo "initializing repository..."
git init
git add .
git branch -M main
git commit -m "init"
git remote add origin git@github.com:$userName/$repoName.git
git push -u origin main
echo "done"
