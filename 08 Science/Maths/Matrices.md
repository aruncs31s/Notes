---
id: Matrices
aliases: []
tags: []
---

# Matrices

Created : 2024-05-14 15:10
#todo Arange

## Contents

- [[#Matrix Multiplication]]
- [[Gauss–Jordan elimination]]
- [[#Determinant]]
- [[#Properties]]
- [[#References]]
-

### Matrix Multiplication

### Matrix Product

The product AB between matrices

$$
A \in R_m\times_l\  and B \in R_l \times _n
then \ C \in R_m \times _n
$$

$$
c_ij = \sum_{k=1}^l a_ik \ b_kj
$$

#rules

> [!NOTE] Rows and Columns
> The this notation
> $$ R_m \times \_l $$
> The `m` represents the rows and `l` represents the columns
> To perform **multiplication of two matrices**, we should make sure that the ==number of columns in the 1st matrix is equal to the rows in the 2nd matrix==. 
> And if you multiply an $m\times n$ matrix with $n\times 1$ matrix then the result will be $n\times 1$ matrix 

#### Inverse of a Matrix 
Consider a Vector 
$$
\overrightarrow v = \begin{bmatrix} 1 & 2 & 3  \\  4& 5& 6  \\ 7& 8& 9 \end{bmatrix}
$$
Then $\overrightarrow v^{-1}$
$$
\overrightarrow v = \begin{bmatrix} 1 & 4 & 7  \\  2& 5& 8  \\ 3& 6& ==9== \end{bmatrix}
$$


#### Dot Product
$$
\begin{bmatrix}
a  \\ b   \\  c  \\  d 
\end{bmatrix}
\cdot 
\begin{bmatrix}
e \\ f   \\  g  \\  h 
\end{bmatrix} = 
a \cdot e  + b \cdot f  +   c \cdot g  +  d \cdot h 

$$

![[dot product.excalidraw]]

![](https://www.mathsisfun.com/algebra/images/matrix-multiply-a.svg)
##### Poroperties
1. If the vectors are pointing in the same direction then the dot product is positive



```js
const a = [1,3,4] 
const b = [3,4,5]
dotProduct = (a,b) => {
	let result = 0;
		for ( let i = 0; i < a.length;i++){
		result = a[i] * b[i];
		
		}
		return result ;
}
console.log( "Input vector 1 = "+ a + "\nInput Vector 2 = " +b + "\nDot Product = " + dotProduct(a ,b))
```

> [!NOTE] Order of Projection
> In dot product calculation the order of projection doesn't really matter we can project $\overrightarrow v$ over $\overrightarrow w$ or $\overrightarrow w$ over $\overrightarrow v$ the order doesn't really matter
> Contents





#### Reduced Row Echelon Form

[[Gauss–Jordan elimination]]

#### Determinant

The factor by which the linear transformation changes any area is known as a **Determinant** . That is if the area of a Region is increased by 3 -> Determinant is 3. And a negative value of Determinant will invert the orientation.

###### For 2x2 Matrices

$$
det(A) = |A| = \begin{vmatrix}
a & b  \\ c & d
\end{vmatrix} = ad - cb 
$$

###### For 3x3 Matrices

$$
det(A) = |A| = \begin{vmatrix}
a & b & c\\
d & e & f\\
g & h & i
\end{vmatrix} = a\begin{vmatrix}
e & f\\
h & i
\end{vmatrix} - b\begin{vmatrix}
d & f\\
g & i
\end{vmatrix} + c\begin{vmatrix}
d & e\\
g & h
\end{vmatrix}
$$
![[Determinant.excalidraw]]

<!-- TODO: -->
#todo Rank





#### 

[Source](https://youtu.be/aAFP5wsmH2k?si=6OVmgu5MlKmEk48q)

#### Properties

1. Associativity
   $$
   A(BC) = (AB)C
   $$
2. $$
      AA^{-1} = A^{-1}A = I
   $$
   Where $I$ is the identity Matrix ^fcc442

$$
 I = \begin{bmatrix}
  1 & 0 & 0 \\ 0 & 1& 0 \\ 0 & 0 & 1 \end{bmatrix} \tag{Identity 3x3 Matrix}
$$

### Applications

##### Solving System of equations

$$
\begin{align*}
6x - 3y  +2y &=7 \\
x + 2y + 5z &= 0\\
2x -8y -z &= -2\\
\end{align*}
$$

It can be re written as

$$
\begin{bmatrix}
6  & -3 & 3  \\  1 &2 &5 \\ 2 & -8 &-1
\end{bmatrix}
\begin{bmatrix} x \\ y \\ z \end{bmatrix}
= \begin{bmatrix} 7 \\0  \\  -2 \end{bmatrix} \tag{1}
$$

> To Find the value of $x,y,z$ we multiply the x with the inverse of the LHS and RHS matrix ie, in this case the variable $x$ is been scaled to some level

>Equation $(1)$ look similar to 
>$$
A \overrightarrow x = \overrightarrow v
>$$
> In order to calculate the value of $x,y,z$ we perform $I \overrightarrow x = A^{-1} \overrightarrow v$ due to [[#^fcc442|Identity Property]] where $I = Identity\ Matrix$  
## References

1. [Source](https://youtu.be/aAFP5wsmH2k?si=6OVmgu5MlKmEk48q)
2. ![[associativity matric.mp4]]
