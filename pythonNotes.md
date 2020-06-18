[TOC]

### Variables and Simple Data Types

> Familiar with the basic rules, anyway, avoid using uppercase letter at the beginning.
>
> Regard variables as labels (each references a certain value)
>
> >String
> >
> >single quote and double quotes are both okay.(为了更好地套娃2333,反正一个包括，另一个用于内部套娃23333)
> >
> >use title() function could change the string's form like a title. Similar methods includes upper() ,lower().

* format string:use ```f"{var1}{var2}"``` to emplace the corresponding var to its value.
* format control symbol: you've already got it.
* strip strings : use ```strip()``` to remove extra white spaces.**There is one more thing to say that rstrip(),lstrip() and strip() all return a new value instead of change the string themselves!**

> Numbers

* The result of division is float defaultly.
* you can use underscores in numbers to make large numbers more readable which do not affect the result **!**
* multiple assignment : have learned once;```x,y,z=1,2,3```
* Python has no built-in constant and py programmers use all capital letters to indicate a variable.
* 

 ### Introducing Lists

>use square brackets toindicate lists
>
>acess elements:
>
>>Normal index approach  is already known,remeber -1 return the last element of a list.
>
>changing ,adding and removing elements
>
>>changing is similar to syntax of accessing an element.
>>
>>use ```append()``` to add a element at the end of  a list.
>>
>>Insert elements into a list:use ```insert(_pos,_ele)``` to insert element in the giving position.
>>
>>Removing a element from a list (accoring pos or value)
>>
>>if you know the position of  a element；use```del(_listName[_pos])``` to remove a element.
>>
>>```pop()``` remove the element and return it.also,```pop(_pos)``` del the ele at the giving position.
>>
>>use ```remove(_value)``` to remove the giving element firstly appearing in the list. 
>
>Organizing a List
>
>>use ```sort()``` to sort a list permanently,default is alphabrtically, and ```sort(reverse=True)``` sort in the reverse order.
>>
>>use ```sorted(_listName)``` to display a list in a particular order but dosen't affect the original one. And it also 
>>
>>

* ```if __name__ =="__main__"```：定义程序入口，只在本程序下运行代码块之中的内容，被其他文件引用时不执行代码块中的内容，避免不必要的程序运行
* 似乎多出来的b的问题可以用base64解决。
* python整数没有大限制，和静态语言好像不太一样
* 在bytes中，无法表示为ASCII字符的字节用\x##表示
* list：有序集合，可以添加和删除元素，在末尾添加元素append，在指定位置插入元素insert(index,element)，删除末尾元素pop(),也可以使用pop(i)用于删除指定位置的元素，i代表的索引位置，负数可以访问相应的倒数第i个位置的元素。
* list里面元素的类型可以不相同，并且list还可以嵌套list
* 另一种有序数组叫做tuple，tuple一旦初始化就不能够修改，也没有insert，pop,append之类的方法，然后就是tuple在定义的时候就初始化，用括号（）括起来，**并且在一个元素的时候加逗号用以区别整数**，在tuple中添加list也可以修改list元素的内容
* 条件分支：if else ,elif，冒号，缩进；条件表达式和C++差不多
* for in循环，和C++的for each差不多
* 利用range函数生成list用于循环，range函数默认从0开始，也可自己设定起点，规则还是左闭右开
* 第二种是while循环，也不用多说，注意结合break和continue
* python内置了字典，相当于map**!!!!**需要用大括号括起来，实现了一种key-value的存储方式，但是如果key不存在的话，dict就会报错，这一点就和map不太一样，map初始值是0。所以可以使用in运算符来检测是否在dict里面，返回一个布尔值，或者用get方法，如果key不存在就会返回none或者是自己指定的第二个参数的值。**作为dict的键值，key是不能改变的，如整数，字符串等等**
* set，用([...])初始化，add（key）添加元素，remove（key）删除元素
* 还有就是不可变对象的一个概念，感觉就和java的内存模型差不多，不能改变字符串，只是改变他的指向

### 函数

* 存在一些内置函数，参数个数和类型都要正确，不然那就会报typeerror错误.如sort函数，max函数以及abs()函数。
* 另外，函数名其实就是对一个函数对象的引用，所以可以给函数起别名。

```python
a=abs
print(a(-1))
```

* 定义函数使用def语句，在交互式环境下，定义函数完毕跳出函数体要两次回车，另外可以将函数定义到一个文件之中使用```from filename import funcname```来引入函数
* 空函数

```python
def nop():
	pass
```

所以这种函数有什么用吗...（pass用于没想，当做占位符，以后可以进行修改）

* 函数返回多个值，其实就是返回一个list或者tuple。默认参数：在此参数后面加等号再加上默认值。不按照参数顺序传默认参数时，应该提供参数名。
* **定义默认参数要注意：默认参数应该指向不可变的对象**，可变参数，在前面加*号即可，就相当于list和tuple一样，但是不限制个数，如果list和tuple要传入当做参数
* 关键字参数，前面两个*,自动拼接成为dict，传参时要加参数名，函数会自动把其当做key,对应的value也会添加上
* 命名关键字参数：就是在关键字参数的基础上限制了参数的名字，格式：

```python
def person(name, age, *, city, job):
    print(name, age, city, job)
```

如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符`*`了：

```python
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
```

* 参数组合：这个理解即可，，有一个优先级顺序
* 函数递归，这个也不多说了，注意层数多了会栈溢出这时候就要采用尾递归优化。尾递归就是指调用自身并且return语句不包含表达式，如：

```python
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
```

但是python并没有对尾递归进行优化...

* 汉诺塔原理：参数不断换位置即可，就是先假设移动n-1个到B，然后再移动最后一个到C，最后再将剩下的从B移动到C

### 高级特性

* 切片，简而言之就是字符串，数组，列表之类的分段

* 只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：

  ```python
  >>> d = {'a': 1, 'b': 2, 'c': 3}
  >>> for key in d:
  ...     print(key)
  ...
  a
  c
  b
  ```

  因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

  默认情况下，dict迭代的是key。如果要迭代value，可以用`for value in d.values()`，如果要同时迭代key和value，可以用`for k, v in d.items()`。

  由于字符串也是可迭代对象，因此，也可以作用于`for`循环：

  ```python
  >>> for ch in 'ABC':
  ...     print(ch)
  ...
  A
  B
  C
  ```

  通过collections模块的Iterable判断：

  ```python
  >>> from collections import Iterable
  >>> isinstance('abc', Iterable) # str是否可迭代
  True
  >>> isinstance([1,2,3], Iterable) # list是否可迭代
  True
  >>> isinstance(123, Iterable) # 整数是否可迭代
  False
  ```

  Python内置的`enumerate`函数可以把一个list变成索引-元素对，这样就可以在`for`循环中同时迭代索引和元素本身：

  ```python
  >>> for i, value in enumerate(['A', 'B', 'C']):
  ...     print(i, value)
  ...
  0 A
  1 B
  2 C
  ```

**记住python一行定义多个变量的形式：变量全都放左边，值全部在右边**

* 列表生成式：Python内置的非常简单却强大的可以用来创建list的生成式。

  举个例子，要生成list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`可以用`list(range(1, 11))`：

  ```python
  >>> list(range(1, 11))
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  ```

可以使用两层循环，可以生成全排列：

```python
>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```

在一个列表生成式中，`for`前面的`if ... else`是表达式，而`for`后面的`if`是过滤条件，不能带`else`。 

这里可以再去看一下相对应的章节

* 生成器：

**我对generator的理解就是，list会保存所有的值，但是generator只会保存next的值，并且通过表达式不断计算下一个值**

*注意*，赋值语句：

```python
a, b = b, a + b
```

相当于：

```python
t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]
```

函数中添加yield就变成generator了。要得到返回值，就要处理异常。

总而言之，generator像一个惰性的list，并且从课后习题中可以发现，list是可以直接相加的，但是str和int相加时不能像java那样直接进行类型转换。

* 迭代器

可以被`next()`函数调用并不断返回下一个值的对象称为迭代器：`Iterator` ，这里可以对比理解C++的迭代器

可以使用`isinstance()`判断一个对象是否是`Iterator`对象：

```python
>>> from collections.abc import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('abc', Iterator)
False
```

把`list`、`dict`、`str`等`Iterable`变成`Iterator`可以使用`iter()`函数： 

```python
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True
```

### 函数式编程

就我自己理解，就是把函数也当做变量一样，传函数名字也可以进行相同的函数

* map和reduce函数

第一个参数是函数名，第二个参数是可迭代对象，map就是作用到每个元素之上，而reduce是第一个第二个元素做运算，之后不断迭代。**注意使用reduce要加from functools import reduce**

* 作业一：TypeError: ‘str’ object does not support item assignment  因为字符串是不能改变的，所以我们不能去试图改变字符串
* 作业二：直接使用lamda表达式，

```python
from functools import reduce
def prod(L):
    return reduce(lambda x, y:x*y,L)
```

* 作业三，使用find函数，并且使用[:5:-1]反向切片，左开右闭，并且开始元素为最后一个元素，这样就可以使用x/10+y操作。

```python
from functools import reduce
DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def char2int(s):
    return DIGITS[s]

def str2float(a):
    i=a.find('.')
    s=reduce(lambda x,y: x*10+y,map(char2int,a[:i]))
    s+=reduce(lambda x,y: x/10+y,map(char2int,a[:i:-1]))/10
    return s

L=[0,1,2,3,4,5,6,7,8,9]
print(L[:5:-1])
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
```

* filter用于过滤，和map一样，也返回的是iterator,转换为list要添加强制转换符

### 异步IO

概念和操作系统类似就是一个线程因为IO操作阻塞，不能其他线程也一起等待，现在要结局的问题就是CPU的高速运行和IO设备速度慢的读写如何匹配：当代码需要执行一个耗时的IO操作时，它只发出IO指令，并不等待IO结果，然后就去执行其他代码了。一段时间后，当IO返回结果时，再通知CPU进行处理。 

**异步IO的意思就是，我先发出IO指令，但是不去等待结果，等IO结束时在处理结果，发出IO指令之后就继续去执行下一条指令**

#### 协程

携程看上去也像子程序，但是在运行一个子程序的过程中可能中断去执行另外一个子程序，特点在于一个线程执行，也不是函数调用发生的子程序切换。所以说协程没有线程切换的开销，因此效率比较高。

python中协程可以通过generator来实现。

**yield的作用其实是调用者和被调用者之间的通信，迭代器可以调用close函数，这样再次调用next(\<Iterator \>)就会报StopIteration的错误**