"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
points=0
riddles=['What kind of band never plays music?','what has many eyes but can not see?','what can travel all around the world without leaveing its corner?']
answers=['a rubber band','a potatoe','a stamp']
dic={}
for i in range(len(riddles)):
  dic[riddles[i]]=answers[i]
print(dic) 
for i in dic:
  print(i)
  ans=input('answer ?')
  if ans==dic[i]:
    points+=1
    print('right!')
  else:
        print('wrong!')
if points==3:
  print('you win!')
else:
  print('you lost!')    


      



