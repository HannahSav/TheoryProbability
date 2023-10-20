**1. В первом ящике 3 белых шара и 8 черных, во втором — 6 белых и 5
черных. Из первого во второй наудачу переложили один шар. Какова
теперь вероятность вынуть из первого ящика черный шар?**   
  
_Для первого вытягивания есть два случая_  
_Вытянутый шар - белый. Вероятность_
![формула](https://latex.codecogs.com/svg.image?&space;P(H_{w})=\frac{3}{11})  
  

_Вытянутый шар - черный. Вероятность_
![формула](https://latex.codecogs.com/svg.image?&space;P(H_{b})=\frac{8}{11})  
   
 
_Теперь посмотрим в обоих случаях - какова вероятность во второй раз вытянуть черный шар_  

![формула](https://latex.codecogs.com/svg.image?&space;P(A_{b}|H_{w})=\frac{7}{10}\ast&space;\frac{8}{11}=0,5(09))  
![формула](https://latex.codecogs.com/svg.image?&space;P(A_{b}|H_{w})=\frac{8}{10}\ast&space;\frac{3}{11}=0,2(18))  
  
  
_Получим ответ:_  

![формула](https://latex.codecogs.com/svg.image?&space;P(A_{b})=P(A_{b}|H_{w})+P(A_{b}|H_{b})=0,(72))
 
**2. Есть 10 симметричных монет, 8 нормальных и 2 бракованных (с двух
сторон герб). Наудачу взятая монета подбрасывается 3 раза. Найти
вероятность того, что выпадут три герба.**  

_Посчитаем вероятности для выбора каждого из видов монет:_  

![формула](https://latex.codecogs.com/svg.image?&space;P(H_{norm})=\frac{8}{10})  
![формула](https://latex.codecogs.com/svg.image?&space;P(H_{fake})=\frac{2}{10})  
  
_Посчитаем выроятности выпадения трех гербов подряд_  
![формула](https://latex.codecogs.com/svg.image?&space;P(A_{3gerb}|H_{norm})=\frac{1}{2}\ast&space;\frac{1}{2}\ast&space;\frac{1}{2}\ast&space;\frac{8}{10}\ast&space=0,1)  

![формула](https://latex.codecogs.com/svg.image?&space;P(A_{3gerb}|H_{fake})=1\ast&space;1\ast&space;1\ast&space;\frac{2}{10}\ast&space=0,2)  
  
_Получим ответ:_  

![формула](https://latex.codecogs.com/svg.image?&space;P(A_{3gerb})=P(A_{3gerb}|H_{normal})+P(A_{3gerb}|H_{fake})=0,3)



**3. Из 12 билетов 5 выигрышных. Билеты вытягиваются по одному без
возвращения. Во второй раз был вытянут выигрышный билет. Какова
вероятность того, что и в первый раз был вытянут выигрышный билет?**
  
_Рассмотрим все случаи для первого вытягивания:_  
_- был вытянут выигрышный билет_  
![формула](https://latex.codecogs.com/svg.image?\inline&space;P(H_{1})=\frac{5}{12})

_- был вытянут проигрышный билет_  
![формула](https://latex.codecogs.com/svg.image?\inline&space;P(H_{2})=\frac{7}{12})  
  
  
_Вероятность вытянуть выигрышный билет в каждом из этих случаев:_  
![формула](https://latex.codecogs.com/svg.image?\inline&space;P(A|H_{1})=\frac{5}{12}\ast&space;\frac{4}{11}=\frac{20}{132})
![формула](https://latex.codecogs.com/svg.image?\inline&space;P(A|H_{2})=\frac{7}{12}\ast&space;\frac{4}{11}=\frac{28}{132})  
  
  
_Найдем ответ по формуле Байеса_

![формула](https://latex.codecogs.com/svg.image?\inline&space;P(H_{1}|A)=\frac{P(A|H_{1})\ast&space;P(H_{1})}{P(A|H_{1})\ast&space;P(H_{1})+P(A|H_{2})\ast&space;P(H_{2})}\ast&space;=\frac{\frac{5}{12}\ast&space;\frac{20}{132}}{\frac{5}{12}\ast&space;\frac{20}{132}+\frac{4}{12}\ast&space;\frac{28}{132}}=\frac{0,06(31)}{0,6(31)+0,(07)}=0,471698113)


**4. Три охотника одновременно и независимо стреляют в кабана. Известно,
что первый попадает с вероятностью 0.8, второй — 0.4, третий – 0.2. Кабан
убит и в нем две пули. Как делить кабана?** 
#### Какие вероятности, что попал первый, второй и третий?  

#### Считаем вероятность, что две пули попали, если попал 1й  

#### -//- 2й  

#### -//- 3й  
#### считаем по ф-ле Байесса