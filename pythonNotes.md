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
>>use ```reverse()``` to reverse the list permanently.
>>
>>use ```len(_listName)``` to show the length of a list.
>
>Avoid Index Errors ! ! !

### Working with Lists

>Looping
>
>>Basic Information is already known.**Pay attention : var in for loop is still global var!**
>>
>>```range(_start,_end,_stepLen)``` function to present the numbers from the start number and stop before the end number
>>
>>use ```list(range(_start,_end))``` to generate a list，also  you can create almost alny set of numbers using ```range()``` function.
>>
>>Remember ```min(),max(),sum()``` function. 
>
>List Comprehension, like this:
>
>```python
>target=[value for value in range(1,11)]
>```
>
>working with part of a List
>
>>Slicing a List: use square brackets,0(By omitting the 2 value, it copied the original list),1,2 or 3index is okay.(The third value represent the skip len.)
>>
>>Looping through a slice : ```for player in players[:-3]:```
>
>dont use equation as copying behavior!!!
>
>Tuples
>
>>immutable list(lol)
>>
>>You can only change tuple when reassign the whole tuple.
>
>

### If Statements

>Multiple conditions : Use key words ```and```&& ```or```
>
>Use ```in``` to check if a certain value exits in a list.
>
>Checking whether a value is not in a list , use ```not``` keywords.
>
>Be aware of  the conception of boolean expression.
>
>If-elif statement can omit the last else statement and use a more specific elif statement.
>
>You can check special items using if statement with a list.
>
>**We can use list name in a if statement like what we do in cxx.If the list is not empty,statement returns True,else return false.**
>
>Styling your if statement : Use a single space **around** comparison operators!

### Dictionaries

>Key-value pattern!!!
>
>Define a dictionary by using a pair of braces.
>
>Use square braces to add and modify key-value pairs.
>
>Use del to delete key-value pairs like this:
>
>```del alien_0['points']```
>
>It is a good habit to include a comma after the last key-value pair as well.
>
>> Using get ( ) to acess value
>>
>> if a key doesn't exist in a dictionary , we could use ```get()``` like this :
>>
>> ```python
>> alien_0 = ['color':'green','speed':'slow']
>> point_value = alien_0.get('points','No point value assigned')
>> # if 'points' exist, you'll get the correspoding value, if not,you get the default value. 
>> ```
>
>Looping Through a Dictionary
>
>>All key-value pairs: like this
>>
>>```python
>>for key,value in user_0.items():
>>```
>>
>>Looping through all the keys in a dictionary like this:
>>
>>```python
>>for name in favorite_language.keys():
>>```
>>
>>you can also omit the ```keys()``` method and just use the dic's name.
>>
>>Another usage is to test if a key exist in a dictionary like this:
>>
>>```python
>>if 'erin' not in favorite_languages:
>>    # do something
>>```
>>
>>Looping through a Dictionary's key in a particulat order
>>
>>We can wrap the ```sorted()``` method around the like this:
>>
>>```python
>>for name in sorted(favorite_language.keys()):
>>```
>>
>>Looping through all the values in a Dictionary
>>
>>Simply like this:
>>
>>```python
>>for language in set(favorite_language.values()):
>>```
>>
>>Set is a collection in which each iten must be unique.**Also wrapped in a pair of braces and dont mistake sets for dictionaries.** 
>>
>>Here is another kind of set called fronzen set which means immutable.
>>
>>delaration like below:
>>
>>```python
>>s = frozenset([1, 2, 3, 'a', 1])
>>```
>>
>>
>
>Nesting
>
>>**A  List of Dictionaries** 
>>
>>each item in a list is a dictionary,remember each dictionary must have identical structure so you could work with each dictionary in the same way.
>>
>>**A List in a Dictionary**
>>
>>When you wanna associate more than a value with a single key
>>
>>DO NOT NESTING TOO DEEPLY.
>
>

### User Input and While Loops

>Use ```input()``` to accept user input and use ```int()```  casting str to int.
>
>Module operator (I've learned that.)
>
>Using a Flag to judge if or not to quit the while loop.
>
>Break and Continue , not too much to say.**Avoid Infinite Loops**
>
>Using a While Loops with Lists and Dictionaries
>
>> You cant modify (Here 'Modify' means change the size of a list or a dictionary.)
>>
>> Moving Items from One List to Another: use while loop to pop from and append to another.
>>
>> Removing All Instances of Specific Values from a List: if a value is still in a list, continue to remove it.
>>
>> Filling a Dictionary with User Input
>>
>> 

### Functions

> Use ```def``` keyword to definie a function.Idented code block is function body.
>
> Passing Arguments
>
> >Positional Arguments : Pass Arguments according to the parameters' positions.
> >
> >Keyword Arguments : explicitly match each argument with a specific parameter. like this
> >
> >```python
> >describe_pet(animal_type='hamster',pet_name='harry')
> >```
> >
> >Default Argument : Pay attention to the position.Default argument should be set at the end of a function's parameter list. Because Python still interprets it as a positional arguments.
> >
> >Avoid Arguments Errors
>
> Return Values
>
> >Use ```return``` keyword to return a value (I' ve already leraned it.)
> >
> >Making Argument Optional ,like this:
> >
> >```python
> >def get_formatted_name(first_name,last_name,middle_name='')#also like age=None
> >```
> >
> >Returning a Dictionary : define a dictionary in the function code block.
> >
> >Using a Function with a while Loop ：Remember include a quit condition.
>
> Passing a List : We can pass a list to a function like a normal argument.
>
> Modifying a List in a Function: Any changes made to the list inside the function body are permanent. ( But change on a single argument will not affect the original var outside the function.)
>
> Make each function to do a specific job,not too many different tasks.
>
> Prevent a Fuction from Modifying a List: ```function_name(list_name[:])``` (But it will need extra time and memory,**Attention here it is a function call not a function definition!!!**)
>
> **Passing an Arbitray Number of Arguments** (like this)
>
> ```python
> def make_pizza(*toppings):
> ```
>
> Remember to place arbitrary arguments at last of the parameter list.
>
> Double asterisk means create a dictionary and accept arbitray number of arguments.(like this)
>
> ```python
> def build_profiles(first,last,**user_info):
> ```
>
> **Storing Your Functions in Modules**
>
> Importing an Entire Module : Use import to import a module in your file.
>
> ```python
> import pizza
> 
> pizza.make_pizza(16,'mushrooms')
> ```
>
> Import Specific Functions
>
> ```python
> from pizza import make_pizza,<other_func_name>
> 
> make_pizza(16,'mushrooms')
> ```
>
> Using as to give a nickname
>
> ```python
> from module_name import function_name as fn
> ```
>
> We can also use as to  give module an alias
>
> ```python
> import module_name as mn
> ```
>
> Using asterisk to import all fuctions in a module
>
> ```python
> from module_name import *
> ```
>
> **Styling Your Function**
>
> No extra spaces on either side of the equal sign.
>
> If there are too many parameters ,press 'Enter' and 'tab' twice to distinguish from the function body.

### Classes

>By convention, class name is capitalized.And like functions, a docstring under definition is better.
>
>a ```__init()__``` function is a must. Every mrthod related to a class must have a self parameter.
>
>Use class name(like construt function in cpp) to make an instance from a class.
>
>Setting a default value for an attribute.
>
>When a number is too long ,we can add undersocres to make it looks more clearly,like
>
>```python
>mu_used_cars.update_odometers(23_500)
>```
>
>**Modify Attribute Values**
>
>>Direcly by dot notation with an instance.
>>
>>Through a method.
>
>**Inheritance** like```class ElectricCar(Car):```
>
>>__init()__ Method for a Child Class: parent class must be part of the current file and must appear before the child class. 
>>
>>```python
>>super().__init(...)__
>>```
>>
>>We can also define attribute and method for child class.
>>
>>Overrinding Methods from the Parent Class : define a method in the child class with the same name as the method you want to override in the parent class.
>>
>>Use Instances as Attributes
>
>Importing Classes
>
>>Remember add a module level docstring describing the contents of a module.
>>
>>storing multiple classes in one module and these classes are related somehow.
>>
>>When you want to spread your classes into several modules to avoid one file from growing too large.
>>
>>Using alias as we did the previous chapter.
>
>Some Styling Issues
>
>* Class name should wrote in CamelCase while instances and module names use underscores. 
>* Every class should have a docstring immediately following the class definition.
>* One blank line between methods and 2 blank lines between different classes
>* If you need to import a module from standard library and a module that you wrote. Import standard library module first, then add a blank line and import from your own module.

### Filles and Exceptions

>**Reading from a File**
>
>> Use  ```open()``` to open a file and return a a object represent this file.
>>
>> Ketowrd ```with``` closes the file once access to it is no longer needed.
>>
>> read(): An empty string is returned when EOF is encountered immediately.
>
>File path : No much to say , but remember to use forward slashes.(If you insist to use backslash ,remember to add escape to each backslash.```C:\\path\\to\\file.txt```)
>
>Reading line by line

### python memory related and assignment mechanism

* 这里主要还是提到了一个常量池的问题，但是对于较大的元素，这里经过测试，界限是256

```python
x = 256
y = 256
print(id(x))#140734570339360 id方法用于查看地址
print(id(y))#140734570339360
x = 257
y = 257
print(id(x))#2697754162832
print(id(y))#2697752528080
```

这里还有另外一个和list相关的问题，就是list中的元素是不可变的，但是创建list的时候，回创建元素的地址以及pyList的地址，例子如下

```python
x = [500,501,502]
y = x
y[1] = 600
y = [700,800]
```

比如说修改y[1]这个语句，他其实是另外再为600分配一个地址，然后在pyList中第二个位置修改为新分配的600的地址。

## Web Application

### Getting Started with Django

>Set up a Project
>
>>Before started, we need to write a spec to keep track of what we've done and development process focused.
>
>Virtual Environtment
>
>>Main effect: Isolate packages from all other Python packages.
>>
>>```bash
>>python -m venv -m ll_env #create a virtual environment in a given path
>>```
>>
>>Activate:
>>
>>```bash
>>source ll_env/bin/activate #macOS or Linux
>>./ll_env/Scripts/Activate.ps1 #Windows powershell
>>```
>>
>>stop using a virtual environment
>>
>>```bash
>>deactivate
>>```
>
>Install Django and Start a Project
>
>>```bash
>>pip install django
>>django-admin startproject learning_log . #remember a dot behind a space
>>```
>>
>>Create the Database 
>>
>>```bash
>>python manage.py migrate #Any time we modify databases,we issue this command.
>>```
>>
>>Start the Server
>>
>>```bash
>>python manage.py runserver
>>```
>
>Start a App
>
>>```bash
>>python manage.py startapp learning_logs
>>```
>
>Once you have created this app,modify settings.py ,add this app into your INSTALLED_APPS as an item.
>
>Inside the learning_logs directory ,the most important files are model.py
>
>About models
>
>>A model tells python how to work with the data that will be stored in the app.
>
>change the current directory to the app you've just created and define models in models.py, Once you've changed the file ,enter the following in the terminal:
>
>```bash
>python manage.py makemigrations <app_name>  #Here it is learning_logs
>python manage.py migrate # Applying this app on your project!!!
>```
>
>Set up a SuperUser
>
>>```bash
>>python manage.py createsuperuser
>>Username: ...
>>Email: ...
>>...
>>```
>
>You can add models at the admin site.
>
>Define the Entry Model
>
>>Like what we've done in creating the topic model.Modify models.py and enter those 2 commands in the terminal.(In fact ,there are more details like how to connect each Entry with a Topic using a ForeignKey method.)
>
>The Django Shell
>
>>```powershell
>>python manage.py shell #to open the django shell 
>>```
>>
>>Use this interactive mode to query your objects and troubleshoot your bugs.
>
>**Making Pages :The learning Log Home Page**
>
>> Consist of 3 stages: define URLS, weting views, and writing templates.
>
>**Mapping  a URL**
>
>> Inside thre original project folder,add an app's urls, and inside that app's folder create another urls.py file which put all urls that might be used inside a variable called urlpatterns.**Use path functino to connect path and view functions.**
>
>**Writing a View**
>
>> In the app's folder ,define the function you just mentioned ,usually return a render function.(The parameter includes the request and html file).
>
>**Writing a Template**
>
>> In the app's folder, create a file folder called templates and inside templates create and write files according to what  you've provided in render fuction.
>
>**Building Additional Pages**
>
>Something about Templates Inheritance
>
>* 



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

## 学校慕课的补充部分

### python基础

#### 列表推倒式

就是之前看到的那种语法，

```python
values = [10, 21, 4, 7, 12]
squares = [x**2 for x in values]
print (squares)
```

前面一个是列表中所要存储的值，后一个是x所属的范围，列表推倒时还可以进行筛选。

```python
values = [10, 21, 4, 7, 12]
squares = [x**2 for x in values if x <= 10]
print (squares)
```

当然也可以用列表推导生成set和dictionary，以及求出该形式下所有元素的和

```python
square_set = {x**2 for x in values if x <= 10}
print(square_set)
square_dict = {x: x**2 for x in values if x <= 10}
print(square_dict)
# 注意这里的方括号，实际上来说就是还是生成了一个临时列表然后用sum函数去计算它的和。
total = sum([x*x for x in values])
```

但是使用方括号实际上会产生一个临时的列表，造成不必要的内存分配，所以我们也可以去掉方括号，不直接生成这个列表，时间比较的话，后者稍短，但是根据具体情况的不同有时候会出现误差。

#### 异常

具体格式就是使用

```python
try:
    pass
except (Exception):
    pass
```

有一种情况就是并不是所有的异常都派生于Exception类，所以有时候更一般的写法是只写except。

* 自定义异常，这个就不多说，在不满足条件的地方就raise一个异常。
* finally关键字，如果try语句中有一场，finally语句块在抛出异常之前执行，如果没有出现异常，finally语句块在最后执行。

#### warning

大致意思就是说如果出现了一些错误但是又不想让程序停止运行。具体内容去看chapetr10中的代码文件

#### 文件读写

ipython中可以使用

```python
%%writefile test.txt
...
...
...
```

When you want to finish writing press \<tab\>+ \<Enter\>.

提一些之前没有注意到的点，在程序中关闭文件可以使改动发生在磁盘上，并且即使显式关闭文件，但是出现异常时不会讲改动写入磁盘，我们可以使用异常处理，但是更简便的做法是使用with语句来打开文件。

* tips:os.remove()用于移除文件，os.rmdir()用于移除目录。

### Advanced Topics

#### sys模块简介

简单来说呢就是与系统相关的一个模块。

```python
import sys
# 获得并打印命令行参数
print (sys.argv)
#打印异常消息
try:
    x = 1/0
except Exception:
    print (sys.exc_info())
```

除此之外，还有显式当前平台和版本以及模块路径的功能。

####  os模块简介

主要还是和路径相关，以及路径文件之类的功能，ipython的环境太好用了，我这里就不多说了。具体细节坑定是要查文档的。

#### 函数进阶

* python中的函数可以像变量一样存储在字典里，而且还可以作为返回值。
* python中的函数传参方式是引用传参，但是如果我们在函数中将参数赋予一个新的值，那么函数外边的变量不会受到影响。
* 默认参数是可变的，如果定义了默认参数，并且参数类型是可变类型，那么随着调用次数增加，默认参数会发生变化。一个比较好的做法就是定义None来保障呢个调用之间的状态维持。

```python
def f(x = None):
    if x is None:
        x = []
    x.append(1)
    return x

print (f())
print (f())
print (f())
print (f(x = [9,9,9]))
print (f())
print (f())
```

这里使用None相当于传递了一个信号，说明没有没有提供显示的参数，说明这里需要使用默认参数。

* 高阶函数：以函数作为参数或者将函数作为返回值，比如说map（f,sq)将函数f作用到sq中的每个值上面。

filter(f,sq)的作用相当于，对sq中的每个元素s，返回f(s)为true的元素。

* 还有一种就是有点类似于装饰器的用法

  ```pytho
  def make_logger(target):
      def logger(data):
          with open(target, 'a') as f:
              f.write(data + '\n')
      return logger
  
  foo_logger = make_logger('foo.txt')
  foo_logger('Hello')
  foo_logger('World')
  ```

* 匿名函数：就是lambda表达式，大概写法就是

> ```python
> lambda <variables>: <expression>
> ```

前面是参数列表，后面是表达式或者返回值，一些例子如下。

```pytho	
from functools import reduce
s1 = reduce(lambda x, y: x+y, map(lambda x: x**2, range(1,10)))
print(s1)
```

* 全局变量，函数中可以使用到全局变量的值，但是，如果要对全局变量进行修改的话，必须加上global修饰符，例子如下

```python
x = 15

def print_newx():
    global x
    x = 18
    print (x)
    
print_newx()

print (x)
```

* 递归，细节就不多说了，这里写一个斐波那契的例子

```python
def fib(n):
    if n <= 0:
        return 'Invalid input'
    elif n == 1 or n ==2:
        return 1
    else:
        return f(n-1) + f(n-2)
```

#### 迭代器，装饰器，生成器

* 迭代器：主要就是enumerate这个函数既可以返回下标，又可以返回值。

```python
x = [2,4,6]

for i,n in enumerate(x):
    print('pos',i,'is',n)
```

迭代对象必须实现__iter\_\_方法，获得初始迭代器，然后也可以调用reversed方法来获得反向迭代器。

* 生成器：为了避免占用过大内存，而采用的一边循环一边计算的元素的方式称作生成器(generator)。同理，generator也是通过2next来进行输出，也可以使用range based for来进行输出，另外一个使用生成器的方法是在函数中使用yield关键字，	这样每次运行到指定位置的时候就会返回一个值。
* with语句和上下文管理器，其实我觉得这个有点像RAII的思想，就是使用with获取资源，然后在语句块结束的地方调用析构函数释放资源，但是我还是对python内部的一些函数不太了解。比如说为什么在with语句中刚开始调用的是__enter\_\_，结束的时候调用的是\_\_exit\_\_，这里不是很懂。
* 有点函数式编程的思想，大概就是以函数为对象，像正常的变量或者对系那个一样去使用它。而装饰器就是接受函数作为参数，并且返回对象也是函数对象的函数。两层嵌套就是普通的迭代器，三层嵌套的迭代器还可以添加参数。