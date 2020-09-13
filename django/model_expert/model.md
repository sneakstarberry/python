https://wayhome25.github.io/django/2017/04/01/django-ep9-crud/

https://django-orm-cookbook-ko.readthedocs.io/en/latest/or_query.html 장고 ORM 쿡북

[https://hyunvinci.tistory.com/entry/53-%EC%9E%A5%EA%B3%A0-%ED%86%A0%ED%81%B0-%EC%9D%B8%EC%A6%9D-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-%EC%98%81%EC%96%B4%EC%8C%A4%EC%9D%B4-%EB%A7%8C%EB%93%9C%EB%8A%94-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85-%EC%9D%B8%EC%A6%9DCRUD-%EB%A7%8C%EB%93%A4%EC%96%B4%EC%9A%A4-%EB%A6%AC%EC%95%A1%ED%8A%B8%EC%99%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0?category=789453](https://hyunvinci.tistory.com/entry/53-장고-토큰-인증-로그인-구현하기-영어쌤이-만드는-회원가입-인증CRUD-만들어욤-리액트와-파이썬-장고?category=789453)

# MODEL

### 모델 사용하기
모델을 정의하고 난 후에는 Django 모델을 사용하도록 해야합니다.
`settings.py`에 가서 `INSTALLED_APPS`설정에 models.py가 포함된 모듈(앱)의 이름을 추가합니다.

예를 들어 `models.py`가 포함된 모듈(앱)의 이름이 `myapp`이라면 `INSTALLED_APPS`는 다음과 같습니다.
```python
INSTALLED_APPS = [
    #...
    'myapp',
    #...
]
```

`INSTALLED_APPS`에 새 앱을 추가하고 `python manage.py migrate`를 실행하고 경우에 따라서 `python manage.py makemigrations`를 사용하여 먼저 `migrations`를 생성해 줍니다.

### FIELDS
모델의 가장 중요한 부분과 모델과 모델에서 필요한 부분은 데이터 베이스 필드 목록을 정의하는 것 입니다. 필드는 클래스 속성으로 지정됩니다. `clean`, `save`또는 `delete` 같은 모델의 API와 충돌하는 필드 이름을 선택하지 않도록 주의해야 합니다.

 예:
```python
from django.db import models

class Musician (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album (models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
```

---

#### FIELD TYPES
모델의 각 필드는 적절한 `Field`클래스의 인스턴스 여야합니다. Django는 필드 클래스 유형을 사용하여 몇 가지 사함을 결정합니다.

- 열 유형으로, 데이터베이스에 저장할 데이터의 종류 (예: `INTEGER`, `VARCHAR`, `TEXT`)를 알려줍니다.
- Form field를 렌더링 할 때 사용할 기본 HTML 위젯 (예: `<input type="text>`, `<select>`).
- Django 관리자 및 자동 생성 폼에 사용되는 최소한의 유효성 검사 요구 사항입니다.

Django는 수십 개의 내장 필드 유형을 제공합니다. [참조 모델필드](https://docs.djangoproject.com/en/3.0/ref/models/fields/)에서 전체 목록을 찾을 수 있습니다. Django의 내장 필드 중 원하는 것이 없다면 커스텀 필드를 쉽게 작성 할 수 있습니다. [사용자 정의 모델 필드 작성](https://translate.google.com/translate?hl=ko&sl=en&u=https://www.djangoproject.com/start/&prev=search)을 참조하십시오.

---

#### FIELD OPTIONS

각 필드는 하나의 특정 인수의 세트를 취합니다.([참조 모델필드](https://docs.djangoproject.com/en/3.0/ref/models/fields/)에 문서화 됨).예를 들어 `CharField`(및 해당 하위 클래스)에는 데이터를 저장하는 데 사용되는 `VARCHAR`데이터베이스 필드의 크기를 지정하는 `max_length`인수가 필요합니다.

모든 필드 유형에 사용할 수 있는 공통 인수 세트도 있습니다. 이러한 것들은 모두 선택 사항입니다. 공통 인수 세트는 [참조](https://docs.djangoproject.com/en/3.0/ref/models/fields/)에 자세히 설명되어 있지만 가장 자주 사용되는 것들에 대한 요약은 다음과 같습니다.

- **`null`**
`True` 이면 Django는 데이터베이스에 빈 값을 `NULL`로 저장합니다. 기본 값은 `False`입니다.

- **`blank`**
`True` 인 경우 필드를 비워 둘 수 있습니다. 기본값은 `False`입니다.

이것은 `null`과는 다릅니다. `null`은 순전히 데이터베이스 관련이지만 `blank`는 유효성 검사 관련입니다. 필드가 `blank=True`인 경우 양식 유효성 검증은 빈 값을 입력 할 수 있게 합니다. 필드에 `blank=False`가 있으면 필드가 필요합니다.

- **`choices`**
이 필드를 위한 선택사항들로서 사용하기 위한 2개로 짝지어진 튜플들의 나열(A sequence of 2-tuples to use as choices for this field.). 이 옵션이 제공되면 기본 양식 위젯은 표준 텍스트 필드 대신 선택 목록이 되고 선택지는 주어진 선택지로 제한 됩니다.

choices는 다음과 같습니다.
```python
YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
)
```

각 튜플의 첫 번째 요소는 데이터베이스에 저장되는 값이며, 두 번째 요소는 기본 양식 이나 위젯에 표시되는 값 입니다.
모델 인스턴스에서 표시되는 값을 액세스하기 위해서는 get_FOO_display()함수를 사용합니다. 예제는 다음과 같습니다.:

```python
from django.db import models
class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES
```

```cmd
>>> p = Person(name="Fred Flintstone", shirt_size="L")
>>> p.save()
>>> p.shirt_size
'L'
>>> p.get_shirt_size_display()
'Large'
```

- **`default`**
필드에 기본값으로 설정 됩니다.

- **`help_text`**
폼 위젯에서 추가적으로 보여줄 도움말 텍스트입니다. 폼을 사용하지 않아요, 문서화에 많은 도움이 됩니다.

- **`primary_key`**
True일 경우, 해당 필드는 모델의 primary key로 사용됩니다.

어떤 필드에도 `primary_key=True`를 설정하지 않으면 장고는 자동으로 `IntegerField`를 생성해 `primary key`로 사용합니다. 그러므로 반드시 `primary_key=True`를 어떤 필드에 추가할 필요는 없습니다. 자세한 정보는 [Automatic primary key fiels](https://docs.djangoproject.com/en/3.0/topics/db/models/#automatic-primary-key-fields).

`primary key`필드는 읽기 전용입니다. 기존 객체의 기본 키 값을 변경한 다음 저장하면 기존 객체와 함께 새 객체가 생성됩니다. 예를 들면 다음과 같습니다.

<pre><code>from django.db import models
class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)</code></pre>

```cmd
>>> fruit = Fruit.objects.create(name='Apple')
>>> fruit.name = 'Pear'
>>> fruit.save()
>>> Fruit.objects.values_list('name', flat = True)
<QuerySet ['Apple', 'Pear']>
```

- **`unique`**
True인 경우 이 필드는 테이블 전체에서 고유해야 합니다.

---

#### 자동 **`Primary_key`** 필드

Django는 기본적으로 각 모델에 다음 필드를 제공합니다.

```
id = models.AutoField(primary_key = True)
```

이것은 `auto-incrementing primary key`입니다.



사용자 정의 기본 키를 지어하려면 필드 중 하나에 `primary_key=True`를 지정하시오. Django가 `Field.primary_key`가 설정된 것을 본다면 장고는 자동적으로 `id`열을 추가하지 않습니다.



각 모델에는 정확히 하나의 필드에 `primary_key=True`(선언되었거나 자동으로 추가됨.)가 있어야합니다.

---

#### 자세한 필드 이름

`ForeignKey` 제외한 각 필드 유형 (`ManyToManyField` 및 `OneToOneField`)은 선택적인 첫번째 위치 인자를 Verbose name로 사용합니다. Verbose name을 지정하지 않으면 Django는 필드의 속성 이름을 사용하여 자동으로 이름을 만들어 밑줄을 공백으로 변환 합니다.



이 예에서 Verbose name은 "person's first name"

```
first_name = models.CharField("person's first name", max_length = 30)
```

이 예에서 Verbose name은 "first name"

```
first_name = models.CharField(max_length = 30)
```

`ForeignKey`, `ManyToManyField` 및 `OneToOneField`는 첫 번째 인수가 모델 클래스 여야하므로 `verbose_name`키워드 인수를 사용해야 합니다.

```
poll = models . ForeignKey (
    Poll ,
    on_delete = models . CASCADE ,
    verbose_name = "the related poll" ,
)
sites = models . ManyToManyField ( Site , verbose_name = "list of sites" )
place = models . OneToOneField (
    Place ,
    on_delete = models . CASCADE ,
    verbose_name = "related place" ,
)
```

---

### 관계

관계형 데이터베이스의 힘은 테이블을 서로 관계시키는 데 있습니다. Django는 다 대일, 다 대다 및 일 대일의 세 가지 가장 일반적인 데이터베이스 관계 유형을 정의하는 방법을 제공합니다.



#### 다 대일 관계

다 대일 관계를 정의하기 위해 `django.db.models.ForeignKey`를 사용합니다. 모델의 클래스 속성으로 포함하여 다른 `Field`유형과 마찬가지로 사용합니다.



`ForeignKey`에는 위치 인수가 필요합니다. 모델과 관련된 클래스입니다.



예를 들어 **Car** 모델에 __Manufacturer__ 가 있는 경우 (즉, **Manufacturer**는 여러 의 자동차를 만들지만 각 **Car**에는 하나의 **Manufacturer**만 있음) 다음 과 같이 정의하십시오.

```python
from django.db import models

class Manufacturer(models.Model):
    #...
    pass
class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete = models.CASCADE)
    #...
```

재귀 관계(자체와 다 대일 관계가 있는 객체)와 아직 정의되지 않은 모델 과의 관계를 만들 수 도 있습니다. 자세한 내용은 [참조 모델필드](https://docs.djangoproject.com/en/3.0/ref/models/fields/)를 참조하십시오.

`ForeignKey`필드의 이름(위 예제의 `manufacturer`)은 모델의 이름 소문자로 제안하지만 필수는 아닙니다. 물론 원하는 대로 필드에 이름 붙일 수 있습니다. 예를 들면 다음과 같습니다.

```python
class Car(models.Model):
    company_that_makes_it = models.ForeignKey(
    	Manufacturer,
    	on_delete = models.CASCADE,
    )
    #...
```

> 참고 하세요.
>
> `ForeignKey`필드는 [참조 모델필드](https://docs.djangoproject.com/en/3.0/ref/models/fields/)에 설명된 많은 추가 인수를 허용합니다. 이 옵션은 관계 작동 방식을 정의하는 데 도움이 됩니다. 모두 선택사항입니다.
>
> 역방향 관련 개체에 액세스하는 방법에 대한 자세한 내용은 [다음 관계 역방향 예를](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/topics/db/queries/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhisnYa1yxUqHy7w7AxLW5fwKTxTYA#backwards-related-objects) 참조하십시오.

---

#### 다 대다 관계

다 대다 관계를 정의하려면 `ManyToManyField`를 사용하십시오. 모델의 클래스 속성으로서 다른 `Field`유형과 마찬가지로 사용합니다.



`ManyToManyField`에는 위치 인수가 필요합니다. 모델과 관련된 클래스입니다.



예를 들어 `Pizza`에 여러 개의 `Topping`개체가 있는 경우(즉, `Topping`은 여러 피자에 있을 수 있고 각 `Pizza`에는 여러 개의 토핑이 있는 경우) 다음과 같이 표현합니다.

``` python
from django.db import models

class Topping(models.Model):
    #...
    pass
class Pizza(models.Model):
    #...
    toppings = models.ManyToManyField(Topping)
```

[`ForeignKey`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.ForeignKey) 와 마찬가지로 [재귀 관계](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#recursive-relationships) (자체와 다 대다 관계를 가진 객체) 및 [아직 정의되지 않은 모델](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#lazy-relationships) 과의 [관계를](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#lazy-relationships) 만들 수도 있습니다.

[`ManyToManyField`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.ManyToManyField) 의 이름 (위의 예에서 `toppings` )은 관련 모델 객체 세트를 설명하는 복수형이어야합니다.

[`ManyToManyField`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.ManyToManyField) 가있는 모델은 중요하지 않지만 둘 중 하나가 아닌 모델 중 하나에 만 배치해야합니다.

일반적으로 [`ManyToManyField`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.ManyToManyField) 인스턴스는 양식에서 편집 할 객체로 이동해야합니다. 위의 예에서, `toppings` 은 `Pizza` ( `pizzas` [`ManyToManyField`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.ManyToManyField) 가있는 `Topping` 대신)는 피자가 여러 피자에있는 토핑보다 토핑이있는 피자에 대해 생각하는 것이 더 자연 [`ManyToManyField`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.ManyToManyField) 때문입니다. 위에 설정된 방식으로 `Pizza` 양식을 사용하면 토핑을 선택할 수 있습니다.

> 참조 하십시오.
>
> 전체 예는 다 [대다 관계 모델 예](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_many/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhj0KnoqcFf-JIsGdqN__LybnXCWcQ) 를 참조하십시오.

`ManyToManyField필드는 [모델 필드 참조](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#manytomany-arguments)에 설명 된 여러 가지 추가 인수도 허용합니다. 이 옵션은 관계 작동 방식을 정의하는 데 도움이됩니다. 이것은 모두 선택 사항입니다.

---

##### 다 대다 관계에 대한 추가필드

피자와 토핑 믹싱 및 매칭과 같은 다 대다 관계 만 다룰 때는 표준 [`ManyToManyField`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.ManyToManyField) 만 있으면됩니다. 그러나 때로는 두 모델 간의 관계와 데이터를 연결해야 할 수도 있습니다.

예를 들어, 음악가가 속한 음악 그룹을 추적하는 응용 프로그램의 경우를 고려하십시오. 개인과 구성원 인 그룹간에 다 대다 관계가 있으므로 [`ManyToManyField`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.ManyToManyField) 를 사용하여이 관계를 나타낼 수 있습니다. 그러나 개인이 그룹에 가입 한 날짜와 같이 수집하려는 멤버십에 대한 세부 사항이 많이 있습니다.

이러한 상황에서 Django를 사용하면 다 대다 관계를 관리하는 데 사용될 모델을 지정할 수 있습니다. 그런 다음 중간 모델에 추가 필드를 넣을 수 있습니다. 중간 모델은 매개 변수로 작동 할 모델을 가리 키기 위해 [`through`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.ManyToManyField.through) 인수를 사용하여 [`ManyToManyField`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.ManyToManyField) 와 연관됩니다. 음악가 예제의 경우 코드는 다음과 같습니다.

```python
from django.db import models

class Person ( models . Model ):
    name = models . CharField ( max_length = 128 )

    def __str__ ( self ):
        return self . name

class Group ( models . Model ):
    name = models . CharField ( max_length = 128 )
    members = models . ManyToManyField ( Person , through = 'Membership' )

    def __str__ ( self ):
        return self . name

class Membership ( models . Model ):
    person = models . ForeignKey ( Person , on_delete = models . CASCADE )
    group = models . ForeignKey ( Group , on_delete = models . CASCADE )
    date_joined = models . DateField ()
    invite_reason = models . CharField ( max_length = 64 )
```

중개 모델을 설정할 때 다 대다 관계에 관련된 모델에 외래 키를 명시 적으로 지정합니다. 이 명시 적 선언은 두 모델의 관계를 정의합니다.

중간 모델에는 몇 가지 제한 사항이 있습니다.

- 중간 모델은 소스 모델에 대한 *단* 하나의 외래 키를 포함해야하며 (이 예제에서는 `Group` 이 됨) Django가 [`ManyToManyField.through_fields`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.ManyToManyField.through_fields) 사용하여 관계에 사용해야하는 외래 키를 명시 적으로 지정해야합니다. 외래 키가 둘 이상 있고 `through_fields` 를 지정하지 않으면 유효성 검사 오류가 발생합니다. 대상 모델에 대한 외래 키에도 유사한 제한이 적용됩니다 (이 예에서는 `Person` 임).
- 중개 모델을 통해 자체와 다 대 다 관계를 갖는 모델의 경우 동일한 모델에 대한 두 개의 외래 키가 허용되지만 다 대 다 관계의 두 (다른) 측면으로 취급됩니다. 그래도 외래 키가 두 *개* 이상인 경우 위와 같이 `through_fields` 도 지정해야합니다. 그렇지 않으면 유효성 검사 오류가 발생합니다.
- 중개 모델을 사용하여 모델에서 자체로 다 대다 관계를 정의 할 때 [`symmetrical=False`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.ManyToManyField.symmetrical) 를 *사용해야합니다* ( [모델 필드 참조 참조](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#manytomany-arguments) ).

중개 모델 (이 경우 `Membership` 을 사용하도록 [`ManyToManyField`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.ManyToManyField) 를 설정 [`ManyToManyField`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.ManyToManyField) 대다 관계를 작성할 준비가되었습니다. 중간 모델의 인스턴스를 작성하여이를 수행하십시오.

```cmd
>>>  ringo = Person . objects . create ( name = "Ringo Starr" )
>>>  paul = Person . objects . create ( name = "Paul McCartney" )
>>>  beatles = Group . objects . create ( name = "The Beatles" )
>>>  m1 = Membership ( person = ringo , group = beatles ,
...     date_joined = date ( 1962 , 8 , 16 ),
...     invite_reason = "Needed a new drummer." )
>>>  m1 . save ()
>>>  beatles . members . all ()
<QuerySet [<Person: Ringo Starr>]>
>>>  ringo . group_set . all ()
<QuerySet [<Group: The Beatles>]>
>>>  m2 = Membership . objects . create ( person = paul , group = beatles ,
...     date_joined = date ( 1960 , 8 , 1 ),
...     invite_reason = "Wanted to form a band." )
>>>  beatles . members . all ()
<QuerySet [<Person: Ringo Starr>, <Person: Paul McCartney>]>
```

필요한 필드에 대해 `through_defaults` 를 지정하는 한 `add()` , `create()` 또는 `set()` 을 사용하여 관계를 만들 수도 있습니다.

```cmd
>>>  beatles . members . add ( john , through_defaults = { 'date_joined' : date ( 1960 , 8 , 1 )})
>>>  beatles . members . create ( name = "George Harrison" , through_defaults = { 'date_joined' : date ( 1960 , 8 , 1 )})
>>>  beatles . members . set ([ john , paul , ringo , george ], through_defaults = { 'date_joined' : date ( 1960 , 8 , 1 )})
```

중간 모델의 인스턴스를 직접 작성하는 것이 좋습니다.

중간 모델에 의해 정의 된 사용자 정의 통과 테이블이 `(model1, model2)` 쌍에 고유성을 적용하지 않고 여러 값을 허용하는 경우 [`remove()`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/relations/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhhZzNP8UkRd4q51y5cg2kF7UBUpAg#django.db.models.fields.related.RelatedManager.remove) 호출은 모든 중간 모델 인스턴스를 제거합니다.

```cmd
>>>  Membership . objects . create ( person = ringo , group = beatles ,
...     date_joined = date ( 1968 , 9 , 4 ),
...     invite_reason = "You've been gone for a month and we miss you." )
>>>  beatles . members . all ()
<QuerySet [<Person: Ringo Starr>, <Person: Paul McCartney>, <Person: Ringo Starr>]>
>>>  # This deletes both of the intermediate model instances for Ringo Starr
>>>  beatles . members . remove ( ringo )
>>>  beatles . members . all ()
<QuerySet [<Person: Paul McCartney>]>
```

[`clear()`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/relations/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhhZzNP8UkRd4q51y5cg2kF7UBUpAg#django.db.models.fields.related.RelatedManager.clear) 메소드를 사용하여 인스턴스에 대한 다 대다 관계를 모두 제거 할 수 있습니다.

```cmd
>>>  # Beatles have broken up
>>>  beatles . members . clear ()
>>>  # Note that this deletes the intermediate model instances
>>>  Membership . objects . all ()
<QuerySet []>
```

다 대 다 관계를 설정하면 쿼리를 발행 할 수 있습니다. 일반적인 다 대 다 관계와 마찬가지로 다 대 다 관련 모델의 속성을 사용하여 쿼리 할 수 있습니다.

```cmd
 # Find all the groups with a member whose name starts with 'Paul'
>>> Group . objects . filter ( members__name__startswith = 'Paul' )
< QuerySet [ < Group : The Beatles > ] >
```

중간 모델을 사용하면서 해당 속성을 쿼리 할 수도 있습니다.

```cmd
>>>  ringos_membership = Membership . objects . get ( group = beatles , person = ringo )
>>>  ringos_membership . date_joined
datetime.date(1962, 8, 16)
>>>  ringos_membership . invite_reason
'Needed a new drummer.'
```

동일한 정보에 액세스하는 다른 방법은 `Person` 객체에서 다 [대 다 역 관계를](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/topics/db/queries/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhisnYa1yxUqHy7w7AxLW5fwKTxTYA#m2m-reverse-relationships) 쿼리하는 것입니다.

```cmd
>>>  ringos_membership = ringo . membership_set . get ( group = beatles )
>>>  ringos_membership . date_joined
datetime.date(1962, 8, 16)
>>>  ringos_membership . invite_reason
'Needed a new drummer.'
```

---

#### 일대일 관계 [¶](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/topics/db/models/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhgluAftv6BsrnLiSWOPdWK1TkdBnA#one-to-one-relationships)

일대일 관계를 정의하려면 [`OneToOneField`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.OneToOneField) 사용 [`OneToOneField`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.OneToOneField) . 모델의 클래스 속성으로 포함하여 다른 `Field` 유형과 마찬가지로 사용합니다.

이것은 객체가 어떤 방식으로 다른 객체를 "확장"할 때 객체의 기본 키에서 가장 유용합니다.

[`OneToOneField`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.OneToOneField) 에는 위치 인수가 필요합니다. 모델과 관련된 클래스입니다.

예를 들어,“장소”데이터베이스를 구축하는 경우 데이터베이스에 주소, 전화 번호 등과 같은 매우 표준적인 자료를 구축 할 수 있습니다. 그런 다음 자신을 반복하고 `Restaurant` 모델에서 해당 필드를 복제하는 대신 장소 위에 식당 데이터베이스를 구축하려는 경우 식당에 [`OneToOneField`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.OneToOneField) to `Place` 만들 수 `Place` (레스토랑은 "식당"이기 때문에; 사실, 이것을 처리하기 위해 일반적으로 암시 적 일대일 관계를 포함하는 [상속을](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/topics/db/models/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhgluAftv6BsrnLiSWOPdWK1TkdBnA#model-inheritance) 사용합니다).

[`ForeignKey`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.ForeignKey) 와 마찬가지로 [재귀 관계](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#recursive-relationships) 를 정의하고 [아직 정의되지 않은 모델에 대한 참조를](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#lazy-relationships) 작성할 수 있습니다.

> 참고 하십시오.
>
> 전체 예는 [일대일 관계 모델 예](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/topics/db/examples/one_to_one/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhgXytUf1VKJ0KNZqjN4d76Z2re-JQ) 를 참조하십시오.

[`OneToOneField`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.OneToOneField) 필드는 선택적 [`parent_link`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.OneToOneField.parent_link) 인수도 허용합니다.

모델의 기본 키가 자동으로되는 데 사용되는 [`OneToOneField`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.OneToOneField) 클래스. 더 이상 사실이 아닙니다 (원하는 경우 [`primary_key`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.Field.primary_key) 인수를 수동으로 전달할 수 있음). 따라서 단일 모델에 [`OneToOneField`](https://translate.googleusercontent.com/translate_c?depth=1&hl=ko&prev=search&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.djangoproject.com/en/3.0/ref/models/fields/&xid=17259,15700023,15700186,15700190,15700256,15700259,15700262,15700265,15700271&usg=ALkJrhizkOeG8FsoW467hxjohmHLy3Vb1Q#django.db.models.OneToOneField) 유형의 여러 필드를 가질 수 있습니다.

























