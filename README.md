This is a pelican site

The content directory contains the content of oages and articles
The output directory contains the generated html

Generate output locally:  
`pelican content -s pelicanconf.py`


Generate output for remote:  
`pelican content -s publishconf.py`


```
cd output
touch .nojekyll

git init

git add .

git commit -m "new content"

git remote add origin https://github.com/rogerbrinkmann/vtp

git push --force origin master:gh-pages