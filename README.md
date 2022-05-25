# hitfilter
敏感词过滤器

## 安装

```shell script
$ pip install hitfilter
```

## 示例

### 一般操作

```python
import hitfilter

gfw = hitfilter.DFAFilter()
gfw.parse()

print(gfw.filter("售假人民币 习近平", "*"))
结果：售假 ** 币 ** *
```

或:

```python
import hitfilter

gfw = hitfilter.DFAFilter()
gfw.add("1989年")
print(gfw.filter("1989年5月8日", "*"))
结果： ** ** 年5月8 *
```

### 自定义keywords

```python
import hitfilter

gfw = hitfilter.DFAFilter()
gfw.parse("keyword")
print(gfw.filter("啊55呸啊呸", "*"))
结果：***呸啊呸
```
