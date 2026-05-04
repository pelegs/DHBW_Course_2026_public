* Vector addition and scaling
  - Solve the conditions on spanning vectors in R^2
  - Use python (sympy) to perform solution
  - Show that the result of linear combos of two vectors is always a parallelogram:
    1) 2D case (desmos)
    1) 3D case (desmos 3D)
  - Same for LCs of three vectors
  - Discuss the area of said parallelogram (first geometrically, then algebraically)
  - Subspaces (desmos 3D)

* Vector projections
  - Show 2D and 3D cases (desmos)
  - Derive *geometric* form of dot product
  - Go over some properties of the dot product:
    1) Orthogonality <=> dot product = 0
    1) Commutativity
    1) Scalars can be moved around
  - Derive *component* form of dot product
  - Derive form of reflection of a vector off of a plane
    1) Form: $\vec{r}=\vec{d}-2\left(\vec{d}\cdot\hat{n}\right)\hat{n}$
    1) Sanity checks for 2D, e.g. $\hat{n}=\left(0,1\right)$ and $\vec{d}=\left(1,-1\right)$.
    1) Sanity checks for 3D, e.g. $\hat{n}=\left(0,0,1\right)$ and $\vec{d}$ is anything
       (expectation: $z$-component is reversed)

* Linear transformations
  - Introduce as the preservation of LCs/span
  - Show grid form of LTs
  - Geometric properties (proof each one?):
    1) origin is preserved
    1) lines remain lines
    1) parallel directions remain parallel
    1) areas are scaled uniformly
  - From LTs to matrices: show how, and construct some examples:
    1) scaling
    1) skew/shear
    1) rotation
    1) reflection by x/y 
  - Compositing LTs <==> matrix multiplication
    1) That's why MM isn't commutative in general
    1) Use LTs composition to set up reflection across any line that goes through the origin
  - The determinant
  - Eigenvalues and eigenvectors

* Systems of linear equations
