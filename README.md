# Pole secant method
Solution of algebraic and transcendental equations by the method of half division and the pole secant method
The pole secant method is two-step iterative.
Using Newton's method, we find: 

$$x_1 = x_0 - \frac{f(x_0)}{f'(x_0)}$$

Next, we find the parameters c, d:

$$ c = x_1 - \frac{f(x_1)+1}{f'(x_1)} $$

$$ d = f(x_1)$$

Find the second step through the zero and the first:

$$x_2 = x_1 - \frac{f(x_1)}{\frac{f(x_0)-f(x_1)}{x_0 - x_1} - \frac{d}{c-x_1}}$$

$$x_0 = x_1$$

$$ x_1 = x_2 $$

![image](https://user-images.githubusercontent.com/113716137/226746356-fbd9b3b9-2fcf-4793-b266-2f306936dfef.png)
![image](https://user-images.githubusercontent.com/113716137/226746585-b8310e4e-8204-4797-82ba-3eed59e45ba0.png)
![image](https://user-images.githubusercontent.com/113716137/226746648-99ecec73-cce2-4130-a6cb-6c88cd7dd0e5.png)
![image](https://user-images.githubusercontent.com/113716137/226746787-298d0c78-07ab-4baa-86bd-0984e69c5436.png)
![image](https://user-images.githubusercontent.com/113716137/226746869-b80193ac-7943-4315-b0b8-eb69768f8946.png)
