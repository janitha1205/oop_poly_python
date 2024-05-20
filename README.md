
# Introduction to oop concept : Polymorphism

OOP concept: Object Oriented Programing concept
- The polymorphism is one of main characteristics of OOP concept
- Others are encapsulation, inheritance and abstraction
- Why these concept are useful:
- Complex code can make it more readable and productive to execute

# Types of polymorphism

## Overloading

According to unique number of input parameters can be able to execute unique function where overdefined by its name(function name)
 
```
Class ex{
    #overloading
    int Add(int x,int y){ 
        return x+y
        }
    #overloading
    int Add(int x,int y,int z){
        return x+y+z
    }
};
 
```
## Overriding

Rewrite same function in different inherited domain where different functionalities exist in inherited classes but in a unique fashion able to executed in existed class structure where number of parameters are equal but functionality is unique to both.
 
```
Class one{
    int function(int x,int y)
    { 
        return x+y
    }
};
#inherited class
Class two: one{
    #overriding
    int function(int x , int y){ 
        return(x*2+234+y*10)
    }
};
  
```
 

