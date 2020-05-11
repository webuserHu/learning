### 一. 快捷键

#### `command 0` 到 `command 4` : 普通文本、一级～四级标题

#### `command B` : **加粗**

#### `command I` : *斜体*

#### `command U` : <u>下划线</u>

#### ``ctrl shift ` `` : ~~删除线~~

#### `command K`: [超链接](https://github.com) , 同样支持锚点

#### `` ctrl ` `` : `代码块`

#### ` option command T ` : 表格, 支持拖拽及移动

| a1   | b1   | c1   |
| ---- | :--- | ---- |
| a2   | b2   | c2   |
| a3   | b3   | c3   |

#### ` option command Q ` : 引用

> 引用1
>
> > 引用2

#### ` ctrl command I` : 插入图片

<img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png" style="zoom:50%;" />

#### ` ``` ` : 代码块

```java
public staic void main(String[] args){
  System.out.println("hello");
}
```

#### ` + 或 - 或 *` : 无序列表

- 1
- 2
  - 21
    - 211

#### ` 空格-空格[空格]空格` : 复选框

- [ ] 

` --- ` : 分割线

---



### 二. typora 自带功能

#### ` [^数字]` : 参考链接[^1]

[^1]: test



#### ` 上标下标` : X^2^ , H~2~O

```
上: X^2^
下: H~2~0
```



#### ` ==文本==` : ==高亮==



#### ` <!-- 文本 -->` : <!-- 注释 -->



#### ` $内联公式$` :

​					 $e^{i\pi}+1$ 

​					 $e^2$



#### ` [toc]` :目录

[toc]

#### 流程图 : 

+ flowchart : 在代码块输入flow

```flow

```



+ mermaid :  在代码块输入mermaid

  ```mermaid
  graph TD
  		开始-->条件B;
  		条件A-->条件D;
  		条件B-->条件D;
  		开始-->条件A;
  		条件D-->结束;
  ```



