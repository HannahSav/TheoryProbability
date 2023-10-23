**1. Вы встретились с шахматистом равной с Вами силы (ничейные
результаты исключены). Что более вероятно: выиграть более одного раза
в 4 партиях или более двух раз в 6 партиях?**  
  
_Воспользуемся формулой для подсчета вероятности в схеме испытаний Бернулли_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_m^k=C_m^k\ast&space;p^k\ast&space;q^{m-k})_

_**Для 4 партий:**_
_Вероятность выиграть 1 раз_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{4}^{1}=C_{4}^{1}\ast&space;{\frac{1}{2}}^1\ast&space;{\frac{1}{2}}^{4-1}=4\ast&space;\frac{1}{2}\ast&space;\frac{1}{8}=0,25)_
  
_Тогда вероятность выиграть больше одного раза_

_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;1-P_4^1=1-0,25=0,75)_  
  

_**Для 6 партий:**_
_Вероятность выиграть 1 раз_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_6^1=C_6^1\ast&space;{\frac{1}{2}}^1\ast&space;{\frac{1}{2}}^{6-1}=6\ast&space;\frac{1}{2}\ast&space;\frac{1}{32}=0.09375)_
   
  
_Вероятность выиграть 2 раза_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_6^2=C_6^2\ast&space;{\frac{1}{2}}^2\ast&space;{\frac{1}{2}}^{6-2}=15\ast&space;\frac{1}{2}\ast&space;\frac{1}{16}=0.5)_
  

_Тогда вероятность выиграть больше двух раз_

_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;1-P_6^1-P_6^2=1-0,09375-0,5=0,40625)

  
**2. В кошельке лежат 8 монет достоинством 5 копеек и 2 монеты
достоинством 3 копейки. Наудачу выбирается монета и бросается 5 раз.
Какова вероятность того, что в сумме будет 15 очков, если герб
принимается за 0 очков?**  
  
_Воспользуемся формулой для подсчета вероятности в схеме испытаний Бернулли_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_m^k=C_m^k\ast&space;p^k\ast&space;q^{m-k})_  

_Посчитаем верояность получить 15 очков, если выбрали 3 копейки_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_5^5=C_5^5\ast&space;\frac{1}{2}^5\ast&space;\frac{1}{2}^{5-5}=1\ast&space;\frac{1}{32}\ast&space;1=\frac{1}{32}=0,03125)_
  
  
_Посчитаем верояность получить 15 очков, если выбрали 5 копеек_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_3^5=C_3^5\ast&space;\frac{1}{2}^3\ast&space;\frac{1}{2}^{5-3}=10\ast&space;\frac{1}{8}\ast&space;\frac{1}{4}=\frac{10}{32}0,3125)_
    

_А теперь вспомним, что монеты в 3 и в 5 копеек выпадают с разной вероятностью. Посчитаем полную:_
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_{full}=P_{3}\ast&space;P_{5}^{5}+P_{5}\ast&space;P^3_5=\frac{2}{10}\ast&space;\frac{1}{32}+\frac{8}{10}\ast&space;\frac{10}{32}=0,25625)_


  
  
**3. Два баскетболиста делают по три броска в корзину. Вероятность
попадания у первого 0.6, у второго 0.7. Найти вероятность того, что у
обоих будет равное количество попаданий.**  
  
_Воспользуемся формулой для подсчета вероятности в схеме испытаний Бернулли_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_m^k=C_m^k\ast&space;p^k\ast&space;q^{m-k})_
  
  
**4. Партия изделий содержит 1% брака. Каков должен быть объем
контрольной выборки, чтобы вероятность обнаружить в ней хотя бы одно
бракованное изедлие была не меньше 0.95?**  
  
_Воспользуемся формулой для подсчета вероятности в схеме испытаний Бернулли_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;P_m^k=C_m^k\ast&space;p^k\ast&space;q^{m-k})_  
  
  
_Эта вероятность должна быть не меньше 0.95. То есть мы ищем m при котором_  
_![формула](https://latex.codecogs.com/svg.image?\inline&space;&space;0,95\leq&space;\sum_{i=1}^{m}P_m^i=C_m^i\ast&space;p^i\ast&space;q^{m-i})_   
  
[код с перебором](4.py)
