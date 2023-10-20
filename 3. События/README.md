## 3. События

**1. В лотерее на карточке, содержащей 49 чисел, нужно отметить 6 чисел.
Затем эти числа сверяются с 6 числами, отобранными случайным образом.
Каковы вероятности угадать n чисел, n = 1, 2, 3, 4, 5, 6?**  

_Сколько вообще существует наборов по 6 различных карт:_
  
![формула](https://latex.codecogs.com/svg.image?&space;C_{49}^{6})
  

_Поймем, что случай, когда совпали все 6 карт - всего 1_  

![формула](https://latex.codecogs.com/svg.image?&space;C_{43}^{0})

_При этом также у нас есть различные варианты того, какие конкретно числа совпали:_

![формула](https://latex.codecogs.com/svg.image?&space;C_{6}^{6})

_Когда совпали 5 карт - мы выбираем одну карту из оставшихся 43 (5 уже выбрали, а 6я не должна совпасть):_   

![формула](https://latex.codecogs.com/svg.image?&space;C_{43}^{1})
![формула](https://latex.codecogs.com/svg.image?&space;C_{6}^{5})


_Для n = 4:_

![формула](https://latex.codecogs.com/svg.image?&space;C_{43}^{2})
![формула](https://latex.codecogs.com/svg.image?&space;C_{6}^{4})


_Для n = 3:_

![формула](https://latex.codecogs.com/svg.image?&space;C_{43}^{3})
![формула](https://latex.codecogs.com/svg.image?&space;C_{6}^{3})


_Для n = 2:_

![формула](https://latex.codecogs.com/svg.image?&space;C_{43}^{4})
![формула](https://latex.codecogs.com/svg.image?&space;C_{6}^{2})


_Для n = 1:_

![формула](https://latex.codecogs.com/svg.image?&space;C_{43}^{5})
![формула](https://latex.codecogs.com/svg.image?&space;C_{6}^{1})


_Соответственно вероятности - это_


_Для n = 6:_

![формула](https://latex.codecogs.com/svg.image?\inline&space;\frac{C_{0}^{43}C_{6}^{6}}{C_{49}^{6}})


_Для n = 5:_

![формула](https://latex.codecogs.com/svg.image?\inline&space;\frac{C_{1}^{43}C_{5}^{6}}{C_{49}^{6}})


_Для n = 4:_

![формула](https://latex.codecogs.com/svg.image?\inline&space;\frac{C_{2}^{43}C_{4}^{6}}{C_{49}^{6}})


_Для n = 3:_

![формула](https://latex.codecogs.com/svg.image?\inline&space;\frac{C_{3}^{43}C_{3}^{6}}{C_{49}^{6}})


_Для n = 2:_

![формула](https://latex.codecogs.com/svg.image?\inline&space;\frac{C_{4}^{43}C_{2}^{6}}{C_{49}^{6}})


_Для n = 1:_

![формула](https://latex.codecogs.com/svg.image?\inline&space;\frac{C_{5}^{43}C_{1}^{6}}{C_{49}^{6}})


_Ну или в общем виде:
если A - общее количество чисел (49)
B - количество чисел, которое выбираем (6)
n - количество совпадающих чисел (1-6)_

![формула](https://latex.codecogs.com/svg.image?\inline&space;\frac{C_{B-n}^{A-B}C_{n}^{B}}{C_{A}^{B}})


**2. На каждой грани правильного додекаэдра написаны числа от 1 до 12
(игральный додекаэдр). Бросаются 3 додекаэдра на плоскость и считается
сумма значений на гранях, лежащих на плоскости. Выписать 5 самых
вероятных сумм и их вероятности.**  
   [код](2.py)  
   ![img2_1.jpg](resources/img2_1.jpg) ![img2_2.jpg](resources/img2_2.jpg)  
   ![img2_3.jpg](resources/img2_3.jpg) ![img2_4.jpg](resources/img2_4.jpg)
   
**3. На грани правильного додекаэдра написали первые буквы названий
месяцев. Сколько раз нужно бросить додекаэдр, чтобы с вероятностью
0,99 выпала хотя бы 1 раз буква А?**  
   [код](3.py)  
 ![img3_1.jpg](resources/img3_1.jpg) ![img3_2.jpg](resources/img3_2.jpg) 
  
**4. В списке фамилий студентов вашей группы опечатка в одной букве. Найти
вероятность, что неверно написана гласная буква.**  
   [код](4.py)  
 ![img4.jpg](resources/img4.jpg)
  

**5. Предположим, что все забыли свои дни рождения. Найти вероятность
того, что дни рождения 12 человек придутся на разные месяцы?**  
   [код](5.py)  
 ![img5.jpg](resources/img5.jpg)
  
  
**6. В таблице выписаны простые числа от 1 до 1000. Событие A — сумма
цифр простого числа кратна 5. Событие B — простое число начинается с 1.
Событие C — простое число двухзначное. Найти вероятность события (A∆C) \ B.**  
   [код](6.py)  
   ![img6.jpg](resources/img6.jpg)
  
**7. На шахматную доску ставят наудачу k ладей. С какой вероятностью они
не будут бить друг друга?**  
   [код](7.py)  
   ![img7.jpg](resources/img7_1.jpg)  
   ![img7_2.jpg](resources/img7_2.jpg)
