# 😻 나이계산기 
- korean President Yoon unified the age calculation method to full age. Amid the resulting confusion, an age calculator was created. 

### DEV
```bash
$ pyenv global
3.10.12
# $ python -m venv venv
$ source venv/bin/activate
# pip install -r requirements.txt
$ uvicorn api.index:app --reload 
```

### Contributing
- scenario #1
```bash
# setting ssh
$ git clone <URL>
$ git branch <VER>/<NAME>
$ git checkout <VER>/<NAME>
$ git push
# make PR
# doing ...
# dogng ...
$ git add <FILE_NAME>
$ git commit -m "<MESSAGE>"
$ git push

# merge main -> deploy
# releases & tag
```
- scenario #2
```bash
$ git branch -r
$ git checkout -t origin/<VER>/<NAME>
# doing ...
# dogng ...
$ git add <FILE_NAME>
$ git commit -m "<MESSAGE>"
$ git push

# merge main -> deploy
# releases & tag
```

### USE
- https://ac.journeyjean.shop

### Ref
- https://docs.python.org/ko/3.10/library/datetime.html
