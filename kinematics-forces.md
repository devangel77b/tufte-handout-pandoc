---
title: Kinematics and Forces
author: Dennis Evangelista
date: 'June 30, 2023'
lang: en-US
---


# Kinematics

Kinematics is the quantitative study of motion. To describe how an object moves, we typically describe its position, velocity, and acceleration in some useful coordinate system / coordinate frame. 

## Position, velocity, acceleration

**Position** is a **vector**[^whatsavector] and describes where an object is in space relative to an established coordinate system. Typical SI units for position are $\unit{\meter}$. I normally use $\vec{r}$, $x$, $y$, or $z$ as variables to describe position, often with an arrow over them to remind myself they are vectors. 

[^whatsavector]: A vector is a number and a direction. To convince yourself direction matters, imagine flying up from the ground $\qty{33}{\meter}$, versus flying down into the ground $\qty{33}{\meter}$; are those different? Would the direction matter? Yes!

**Velocity** is also a vector and describes the **time rate of change of position**. Its units are $\unit{\meter\per\second}$. I normally use $\vec{v}$ to represent velocity. Considering $\Delta$ or $d$ as a "change in", velocity becomes

$$\text{velocity}, [\si{\meter\per\second}] = \dfrac{\text{change in position}}{\text{change in time}}$$
$$ = \dfrac{\Delta \vec{x}}{\Delta t}$$
$$ = \dfrac{d\vec{x}}{dt}$$

[^nocalculus] 
The "time rate of change of position" relationship means that **velocity is like the slope of a position versus time graph,** and that **position is like the area under a velocity versus time graph.** 

[^nocalculus]: The last form, read "dee x dee tee," is how velocity is typically written as a "derivative" in **calculus**, an advanced type of math that was invented partially to make physics easier to understand. You are not responsible for this in Physics 9.

**Acceleration** is obtained from doing a Madlibs sort of thing... we take it as the **time rate of change of velocity**. Its units are $\unit{\meter\per\second\squared}$. I normally use $\vec{a}$ to represent acceleration. 

$$\text{acceleration}, [\si{\meter\per\second\squared}] = \dfrac{\text{change in velociy}}{\text{change in time}}$$
$$= \dfrac{\Delta \vec{v}}{\Delta t}$$
$$= \dfrac{d \vec{v}}{dt}$$

The "time rate of change of velocity" relationship means that **acceleration is like the slope[^whatsaccel] of a velocity versus time graph,** and that **velocity is like the area under an acceleration versus time graph.** 

[^whatsaccel]: Remember slope is rise over run in $y=mx+b$ in math; here compare to $x=vt+x_0$ and $v=at+v_0$.

## Related scalar quantities

Vector position and **displacement** are related to the scalar quantity **distance**.  **Distance** will normally be considered to be the total distance traveled along a path from $\vec{x}_0$ to $\vec{x}_f$ and is only a simple number (e.g. 50 miles) so it is a **scalar**[^whatsascalar] quantity.  **Displacement** ($\vec{d}$) is a vector quantity and is normally taken as $\vec{x}_f - \vec{x}_0$. 

[^whatsascalar]: A scalar is just a plain old number; distance, temperature, mass don't really have a direction to them so they are not vectors.

Vector velocity is related to the scalar quantity **speed**. Speed is normally either the scalar magnitude of velocity, e.g. instantaneous speed, $|v|$, or the total distance traveled divided by the total time (average speed). 

## 1D motion with constant velocity

The following equations hold for 1D motion at **constant (linear) velocity**, which means the speed *and direction*[^doweneedcircularmotion] of the object are not changing:

[^doweneedcircularmotion]: In Physics 9 you are not responsible for circular motion, in which speed might be constant but direction is constantly changing, nor are you responsible for angular velocity

$$x(t) = v t + x_0$$
$$v(t) = v\ \text{(constant)}$$
$$a(t) = 0$$

Examples of 1D motion at constant velocity would include things like a skier moving at $\qty{5}{\meter\per\second}$ north; a softball in space with no forces acting on it; or an object that is not accelerating. The big example fo this is when we pushed people on chairs at constant speed, and also the horizontal component of the marble shooting experiment. 

## 1D motion with constant acceleration

The following equations hold for 1D motion with **constant (linear) acceleration**, which means there is a net force acting on the object that makes it go faster or slower. 

$$x(t) = \dfrac{1}{2} a t^2 + v_0 t + x_0 $$
$$v(t) = at + v_0 $$
$$a(t) = a\ \text{(constant)} $$

Examples of 1D motion with constant acceleration include the case of a ball dropped from the second floor balcony, or a car at a stop light when it hits the accelerator and before shifting gears, or a rocket ship firing a thruster with a specified force output. The big example of this is when we dropped stuff from the balcony; as well as the vertical component of the marble shooting experiment. 

**For this test, do not expect 3D motion or motions that cannot be modeled as either constant velocity or constant acceleration.**

## Alternate form of equations 

When working with displacement[^notchangein] $d$, alternate forms of the equations of motion for constant accelerations are[^thephysicsclassroom]

[^notchangein]: $d$ here means displacement and does not mean "change in"

[^thephysicsclassroom]: See The Physics Classroom, <https://www.physicsclassroom.com>

$$d = v_i t + \dfrac{1}{2} a t^2$$
$$v_f^2 = v_i^2 + 2 a d $${#eq:tpc2}
$$v_f = v_i + a t $$
$$d = \dfrac{v_i+v_f}{2} t $${#eq:tpc4}

These have the advantage of giving displacement in terms of the initial and final velocities ($v_i$ and $v_f$, respectively), the acceleration $a$ and the time $t$. All are equivalent so use whatever form you are most comfortable with. @Eq:tpc2 can be derived from energy conservation and provides a handy way to find final velocity when displacement is known. @Eq:tpc4 has a term related to the average speed $\dfrac{v_i+v_f}{2}$ during the time interval $t$ (sometimes given as $\Delta t$); which may be useful when considering what quantities a problem wishes you to compute. 




# Forces

**Forces** can come from things like weight (gravity)[^whatsgravity], aerodynamic lift or drag, thrust from an engine, friction from the ground, normal forces from the ground; forces also arise from charges, electric and magnetic fields, reaction forces, etc etc. The SI unit of force is a newton, $\unit{\newton}$, defined as $\qty{1}{\newton}=\qty{1}{\kilo\gram\meter\per\second\squared}$. You may also see force specified as pounds force (lbf) when working with non-SI units (such as in specifying the thrust of a jet engine). The form of Newton's second law used in Physics 9 is

$$\text{net force} = \text{mass} \cdot \text{acceleration} $$
$$\sum\vec{F} = m\vec{a} $$

[^whatsgravity]:The force of gravity on an object of mass $m$ is $F = mg$ directed downwards, where $g=\qty{9.8}{\meter\per\second\squared}$ is the acceleration of gravity at the surface of the Earth. You can also get this from Newton's second law. $g$ will be provided for you in the equation sheet.

## Free body diagrams 

**Free body diagrams** are ways to visualize the force acting on an object. The object is drawn isolated from the rest of the universe, and arrows are used to show the forces that are acting on it and their location and directions. This is a useful tool in analyzing the mechanics of all sorts of things, but **for this test you may only be asked to draw free body diagrams of very simple situations**[^whatsimplesituations].

[^whatsimplesituations]: For example, falling objects with or without air drag; rockets sitting on a launch pad, etc.

## Newton's laws

1. An object at rest will stay at rest, unless acted upon by an outside force; an object in motion will stay in motion unless acted upon by an outside force. 
2. If there is an outside force acting, the sum of the forces will equal the time rate of change of momentum[^whatsmomentum].
3. For every action, there is an equal and opposite reaction. 

[^whatsmomentum]: Momentum is $\vec{p} = m \vec{v}$ and is the product of mass and velocity. Since in Physics 9 we are usually dealing with objects of constant mass, a simpler version of this law is just $\sum\vec{F} = m \vec{a}$, where $\sum\vec{F}$ is the net force or the sum of the forces, $m$ is mass, and $\vec{a}$ is acceleration. 

The first law could also be viewed as the case of the second law where $\vec{a}=0$, and (together with the third law) is studied most in **statics**[^whats2001], when considering the balance of forces for and within objects that are not accelerating. 

[^whats2001]: First course taken by many engineers in college...

The second law shows up most in cases where objects are accelerating, such as in studies of vehicles, maneuvers, propulsion systems, or generally in **dynamics**[^whats2002].

[^whats2002]: Second course taken by many engineers in college... 

The third law does not show up very often; one place in engineering is when an object pushing on the ground or some other object, the force it feels is often called the **reaction force** and given the symbol $R$ in reference to the third law. 

