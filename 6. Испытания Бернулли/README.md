**1. Вы встретились с шахматистом равной с Вами силы (ничейные
результаты исключены). Что более вероятно: выиграть более одного раза
в 4 партиях или более двух раз в 6 партиях?**  
  
_Воспользуемся формулой для подсчета вероятности в схеме испытаний Бернулли_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_m^k=C_m^k\ast&space;p^k\ast&space;q^{m-k})_

_**Для 4 партий:**_
_Вероятность выиграть 0 раз_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{4}^{0}=C_{4}^{0}\ast&space;{\frac{1}{2}}^0\ast&space;{\frac{1}{2}}^{4-0}=1\ast&space;1\ast&space;\frac{1}{16}=\frac{1}{16}=0,0625)_
  
  
  
_Вероятность выиграть 1 раз_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{4}^{1}=C_{4}^{1}\ast&space;{\frac{1}{2}}^1\ast&space;{\frac{1}{2}}^{4-1}=4\ast&space;\frac{1}{2}\ast&space;\frac{1}{8}=0,25)_
  
_Тогда вероятность выиграть больше одного раза_
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;1-P_4^1-P_4^0=1-0,25-0,0625=0,6875)_  
  

_**Для 6 партий:**_  
  
  
_Вероятность выиграть 0 раз_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{6}^{0}=C_{6}^{0}\ast&space;{\frac{1}{2}}^0\ast&space;{\frac{1}{2}}^{6-0}=1\ast&space;1\ast&space;\frac{1}{64}=\frac{1}{64}=0,015625)_
  

_Вероятность выиграть 1 раз_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_6^1=C_6^1\ast&space;{\frac{1}{2}}^1\ast&space;{\frac{1}{2}}^{6-1}=6\ast&space;\frac{1}{2}\ast&space;\frac{1}{32}=0,09375)_
   
  
_Вероятность выиграть 2 раза_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_6^2=C_6^2\ast&space;{\frac{1}{2}}^2\ast&space;{\frac{1}{2}}^{6-2}=15\ast&space;\frac{1}{4}\ast&space;\frac{1}{16}=0,234375)_
  

_Тогда вероятность выиграть больше двух раз_

_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;1-P_6^1-P_6^2-P_6^0=1-0,09375-0,234375-0,015625=0,65625)

  
**2. В кошельке лежат 8 монет достоинством 5 копеек и 2 монеты
достоинством 3 копейки. Наудачу выбирается монета и бросается 5 раз.
Какова вероятность того, что в сумме будет 15 очков, если герб
принимается за 0 очков?**  
  
_Воспользуемся формулой для подсчета вероятности в схеме испытаний Бернулли_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_m^k=C_m^k\ast&space;p^k\ast&space;q^{m-k})_  

_Посчитаем верояность получить 15 очков, если выбрали 3 копейки_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_5^5=C_5^5\ast&space;\frac{1}{2}^5\ast&space;\frac{1}{2}^{5-5}=1\ast&space;\frac{1}{32}\ast&space;1=\frac{1}{32}=0,03125)_
  
  
_Посчитаем верояность получить 15 очков, если выбрали 5 копеек_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_5^3=C_5^3\ast&space;\frac{1}{2}^3\ast&space;\frac{1}{2}^{5-3}=10\ast&space;\frac{1}{8}\ast&space;\frac{1}{4}=\frac{10}{32}=0,3125)_
    

_А теперь вспомним, что монеты в 3 и в 5 копеек выпадают с разной вероятностью. Посчитаем полную:_
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{full}=P_{3}\ast&space;P_{5}^{5}+P_{5}\ast&space;P^3_5=\frac{2}{10}\ast&space;\frac{1}{32}+\frac{8}{10}\ast&space;\frac{10}{32}=0,25625)_


  
  
**3. Два баскетболиста делают по три броска в корзину. Вероятность
попадания у первого 0.6, у второго 0.7. Найти вероятность того, что у
обоих будет равное количество попаданий.**  
  
_Воспользуемся формулой для подсчета вероятности в схеме испытаний Бернулли_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_m^k=C_m^k\ast&space;p^k\ast&space;q^{m-k})_  
  
_Вероятность того, что первый забьет 0 раз_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{first3}^0=C_3^0\ast&space;0,6^0\ast&space;0,4^{3-0}=1*1*0,064=0,064)_
_Вероятность того, что первый забьет 0 раз_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{second3}^0=C_3^0\ast&space;0,7^0\ast&space;0,3^{3-0}=1*1*0,027=0,027)_ 
  
  
_Соответственно вероятность того, что оба ни разу не забьют_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{both0shot}=P_{first3}^0\ast&space;P_{second3}^0=0,064\ast&space;0,027=0,001728)_
  

_Вероятность того, что первый забьет 1 раз_  
  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{first3}^1=C_3^1\ast&space;0,6^1\ast&space;0,4^{3-1}=3*0,6*0,16=0,288)_
  
_Вероятность того, что первый забьет 1 раз_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{second3}^1=C_3^1\ast&space;0,7^1\ast&space;0,3^{3-1}=3*0,7*0,09=0,189)_
  
_Соответственно вероятность того, что оба забьют по 1 разу_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{both1shot}=P_{first3}^1\ast&space;P_{second3}^1=0,288\ast&space;0,189=0,054432)_  
  
  

_Вероятность того, что первый забьет 2 раза_  
  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{first3}^2=C_3^2\ast&space;0,6^2\ast&space;0,4^{3-2}=3*0,36*0,4=0,432)_
  
_Вероятность того, что первый забьет 2 раза_  
 
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{second3}^2=C_3^2\ast&space;0,7^2\ast&space;0,3^{3-2}=3*0,49*0,3=0,441)_
  
_Соответственно вероятность того, что оба забьют по 2 раза_  
  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{both2shot}=P_{first3}^2\ast&space;P_{second3}^2=0,432\ast&space;0,441=0,190512)_  
  


_Вероятность того, что первый забьет 3 раза_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{first3}^3=C_3^3\ast&space;0,6^3\ast&space;0,4^{3-3}=1*0,216*1=0,216)_
_Вероятность того, что первый забьет 3 раза_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{second3}^3=C_3^3\ast&space;0,7^3\ast&space;0,3^{3-3}=1*0,343*1=0,343)_
_Соответственно вероятность того, что оба забьют по 3 раза_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{both3shot}=P_{first3}^3\ast&space;P_{second3}^2=0,216\ast&space;0,343=0,074088)_  
  
  
  
_Итоговая вероятность_
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{sameNumberOfShot}=P_{both3shot}+P_{both2shot}+P_{both1shot}+{P_both0shot}=0,074088+0,190512+0,054432+0,001728=0,32076)_
  
  
**4. Партия изделий содержит 1% брака. Каков должен быть объем
контрольной выборки, чтобы вероятность обнаружить в ней хотя бы одно
бракованное изедлие была не меньше 0.95?**  
  
_Воспользуемся формулой для подсчета вероятности в схеме испытаний Бернулли_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_m^k=C_m^k\ast&space;p^k\ast&space;q^{m-k})_  
  
  
_Эта вероятность должна быть не меньше 0.95. То есть мы ищем m при котором_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;0,95\leq&space;\sum_{i=1}^{m}P_m^i=C_m^i\ast&space;p^i\ast&space;q^{m-i})_   
  
[код с перебором](4.py)

![img6_1](resources/img6_1.jpg)
![img6_2](resources/img6_2.jpg)
