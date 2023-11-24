# Практическая работа №1

## Определение расхода припоя при пайке печатных плат

## Дано
- $P=25$ - количество плат (шт)
- $q=352$ - количество точек пайки на одну плату (шт)
- $d=1.2$ = диаметр прутка припоя (мм)
- $\rho = 0.0085$ - плотность припоя ($г/мм^3$)
- $R_1 = 0.3$ - радиус вершины конуса (мм\)
- $R_2 = 1.5$ - радиус основания конуса (мм)
- $H = 1.3$ - высота конуса (мм)

## Найти
- $V$ - обьем усеченного конуса
- $w$ - вес одной точки пайки
- $W$ - общий вес на плату
- $W_{30}$ - вес с запасом
- $L$ - длина прутка припоя на одну плату
- $L_{общая}$ - всего нужно на пайку


1. Найдем объем усеченного цилиндра:

$V_{конус}=\frac{1}{3}\pi H(R_1^2+R_2^2+R_1\cdot R_2)= \frac{1}{3}\cdot 3.1416 \cdot 1.3 \cdot (0.3^2+1.5^2+0.3\cdot 1.5) \approx 3.798мм^3$

2. Вес одной точки:

$w = V_{конус} \cdot \rho = 3.798\cdot 0.0085\approx 0.0322г$

3. Вес всех точек на плате:

$W = q\cdot w = 352 \cdot 0.0322 \approx 11.364г$

4. Вес с 30% запасом для одной платы

$W_{30\%} = W+0.3W \approx 14.7734г$

5. Количество грамм припоя в одном мм прутка диаметром 1.2 мм

$Q=\frac{\pi d^2}{4}\cdot \rho = \frac{3.1416 \cdot 1.2^2}{4}\cdot 0.0085 \approx 0.0096 г$

6. Длина проволки (прутка) припоя для одной платы
$L = W_{30\%} / Q \approx 14.7734 / 0.0096 \approx 1536.77мм$ 

Итого, для одной платы с 352 точками пайки необходим пруток припоя более полутора метров.

Цифра кажется огромной по сравнению с 16 мм в задаче из примера. 

Но, при грубом подсчете 16 мм - никак не может быть даже на плату с 81 точкой!

## Доказательство

У нас есть конус, у которого верхний диаметр 0.6, а нижний 3 мм. Возьмем среднее арифметическое двух оснований и получим 1,8мм, что является диаметром большим чем диаметр прутка припоя 1.2. Предположим, очень грубо, что мы имеем дело не с конусом а с цилиндром диаметр которого 1.2, следовательно его высота H из условия равна 1.3мм. Умножив 1.3 на 352 получим 458мм, т.е. почти пол метра прутка припоя нам нужно только по самым грубым подсчетам. Более того, сократили в меньшую сторону  показатели цилиндра с 1.8 до 1.2. Но, все равно откуда взялись полтора метра, рассмотрим далее. 

Можно подтвердить правильность полуторометрового вычисления  с помощью формулы цилиндра, ведь пруток у нас цилиндрической формы, то:

7. Найдем объем цилиндра длиной 1мм для диаметра 1.2 (радиус 0.6):

$V_{цилиндр}=\pi r^2H = 3.1416 * 0.6^2*1 \approx 1.13мм^3$

8. Теперь найдем вес этого цилиндра (миллиметрового куска прутка)

$w_{цилиндр} = V_{цилиндр} * \rho = 1.13 \cdot 0.0085 \approx 0.0096г$

Результат совпадает с Q из пункта №5.

Отсюда, така же найдем длину прутка для всей платы. Мы знаем массу с 30% запасом, поделим ее на вес одного мм прутка и мы получим то количество мм, которое входит в эту массу:

9. $L = W_{30\%} / Q \approx 14.7734 / 0.0096 \approx 1536.77$

Дело в том, что мы считали 30% как запас, это одна треть (очень много), более того мы не учитывали ножку которая, тоже имеет объем

10. Посчитаем сколько будет занимать объем ножки:

$V_{ножка}=\pi r^2H = 3.14 \cdot 0.3^2 \cdot 1.3 \approx 0.36мм^3$

11. Вычтем объем ножки из объема конуса, получим объем конуса с отверстием

$V_{hole} =  V_{конус} - V_{ножка} = 3.798 - 0.36 \approx 3.43мм^3$

12. Найдем вес конуса с отверстием:

$w_{hole} = V_{hole} \cdot \rho = 3.43 \cdot 0.0085 \approx 0.029г$

13. Найдем вес всех точек пайки на одной плате

$W_{hole} = w_{hole} \cdot q = 0.029 \cdot 352 = 10.26 грамм$

14. Переведем в длину:

$L_{hole} = W_{hole} / w_{hole} = 10.26/0.029 \approx 1067.73мм$


Следовательно 1 метр припоя весит около 10 грамм. [Интернет подтверждает!](https://www.vseinstrumenti.ru/product/pripoj-s-kanifolyu-pos-61-1-mm-spiral-1-metr-rexant-09-3110-766176/)

15. Расчет метража припоя для всех 25 плат, содержащих по 352 точки:

$L_{25} = L_{hole} \cdot 25 = 1067.73 \cdot 25 \approx 27353.33мм \approx 27,5метра$