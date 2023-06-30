---
Title: Momentum, impulse, and energy
Author: D Evangelista
Date: \today
---
The Q4 test will be in class on \printdate{6/2/2021}. You may use two (2) hardcopy sheets of
\qtyproduct{8.5x11}{in} notes (both sides) and a calculator.[^mn1] 
Please do not plan to use your phone or your computer as either your 
notes or your calculator. Material from Q3 is fair game! Physics builds 
on previous physics and there is no way to separate momentum from the 
kinematics material covered during Q3. Also, use your **flash cards** to 
make sure you are solid regarding equations, correct units, etc.

[^mn1]: {-} The Q4 test will be on \printdate{6/2/2021}

# Momentum and impulse

**Momentum is the product of mass times velocity**:

$$\text{momentum}, [\unit{\kilo\gram\meter\per\second}] = \vec{p} = m \vec{v}.$$

It reflects how much mass is moving and how fast it is going. It is like
the hitting power of a bullet or a hockey defenseman/defensewoman, which
depends on both the mass and the velocity. Something big and fast hurts
when it hits. Expect to use momentum in problems dealing with bullets,
collisions, things smacking together and sticking or bouncing.

The **impulse equation** comes from looking at when forces are applied,
or when objects change velocity.[^mn2]

[^mn2]: If you get a problem and realize it deals with the impulse equation, immediately write "impulse equation" and copy these equations onto your paper. Show your thinking, show what you know.

$$\Delta p = F \Delta t = m \Delta v$$

Know how to use this equation to compute the average force acting on a
body that has changed velocity due to rocket motors, friction, etc.

## Momentum conservation during collisions

We thought about three types of collisions: **elastic collisions,
inelastic collisions, and explosions**[^sn1]. During elastic collisions, the
bodies bounce off one another. During an inelastic collision, bodies
stick together after the collision. During an explosion, two bodies
initially connected and typically stationary explode apart. Momentum is
**conserved** in all of these; in other words, **the momentum of the
system before the collision or explosion is the same as the momentum of
the system after**. 

[^sn1]: Most likely you will see inelastic collisions and explosions on the final. Elastic collisions require setting up and solving two simultaneous equations with the second equation coming from energy conservation or by rewriting the problem to be relative to the center of mass.

$$\text{initial momentum} = \text{final momentum},$$
$$p_0 = p_f.$$

Momentum conservation[^sn2] can also be understood as a case of Newton's first
and second laws; if the sum of the forces is zero, then the time rate of
change of momentum is zero; thus momentum is constant.

[^sn2]: Conservation of (linear) momentum is one example of a **conservation law** in physics. Many other quantities are conserved (e.g. charge, angular momentum, energy) and such conservation laws provide a useful entry to solving many sorts of problems.

## Inelastic collisions

In **inelastic collisions, the bodies collide and stick together**.
Momentum is conserved during this type of collision. The governing
equation is[^sn3]

[^sn3]: If you get a problem and realize it deals with inelastic collisions, immediately write "inelastic collision" and copy these equations onto your paper. Show your thinking, show what you know.

$$m_1 v_{1,0} + m_2 v_{2,0} = (m_1 + m_2) v_{f},$$

or the initial momentum of the system is equal to the final momentum of the
system. Use the word problem to identify which terms are zero and which
terms are known, then solve for the unknown, which is typically $v_f$.

Examples of inelastic collisions that you should be comfortable with:
inelastic collisions of carts on the momentum track experimnent;
inelastic collisions of a bocce ball with your device; any of the
pogils/gizmo/etc in class exercise examples, e.g. big fish eats little
fish, cars crash, etc...

## Explosions

In **explosions, two or more bodies initially joined and usually at rest
explode apart in different directions**. Momentum is conserved during
this type of collision. The governing equation if the system starts from
rest is 

$$0 = m_1 v_{1,f} + m_2 v_{2,f},$$

or the initial momentum of the system is equal to the final momentum of 
the system. Use the word problem to identify which terms are known, usually 
the masses and one of the velocities, then solve for the unknown, usually 
other velocity.

Examples of inelastic collisions that you should be comfortable with:
guns, cannons, explosive decoupling of a space station, birds vomiting
mid-flight...

# Energy, work, and power

**Work** is force multiplied by the distance over which the force is
applied[^snwork]:

[^snwork]: You can think of work as it takes more work to lift a heavy mass, and it takes more work to lift something farther. Combining the two together by multiplying the force times the (parallel) distance gives us the expression for work in physics. There are fine details about the type of multiplication (a "dot product") used that you are not responsible for in Physics 9; you will only get plain conservative constant forces applied over simple parallel distances and path-independent work terms only

$$\text{work}, [\unit{\joule}] = \text{force} \cdot \text{distance}$$
$$W = \vec{F} \cdot \Delta\vec{x}.$$

Work and energy are measured in joules (\unit{\joule}), where $\qty{1}{\joule} = \qty{1}{\newton} \cdot \qty{1}{\meter}.$

**Energy conservation states that energy is neither created nor
destroyed; but it can change form** (from potential to kinetic; from
electrical to heat; etc). In a closed system, we might observe potential
energy being changed to kinetic energy, for example. This law is
sometimes called the **first law of thermodynamics**.

**Gravitational potential energy** is the work done by gravity in
lifting a weight up from some height where the energy is zero:

$$GPE = mgh$$

Potential energy could also be stored by springs, be
stored electrically by something like a battery, and so on.

**Kinetic energy** is the energy something has by virtue of how fast it
is moving: 

$$KE = \frac{1}{2} m v^2$$

## Power

**Power** is the time rate of change of doing work:

$$P = \dfrac{\Delta W}{\Delta t}.$$

and is measured in watts (\unit{\watt}) where 
$\qty{1}{\watt} = \qty{1}{\joule\per\second}$. 
For example, when you get a light bulb, its rated power might be \qty{45}{\watt}; this means in \qty{1}{\second} it consumes \qty{45}{\joule} of energy.

When a force $F$ is applied to push something moving at some velocity
$v$, the power is the product 

$$P = F \cdot v.$$

This form is useful when considering, for example, the raw power output of 
an engine or propulsion system; or the power dissipated by a braking system; 
or the power dissipated by a resistor ($P=IV$)

## Example energy conservation problems

A typical problem with energy might involve a roller coster and ask you
to recognize that **energy is conserved**, such as converting the GPE of
the roller coaster at the highest hill to KE at the bottom, e.g.

$$\text{initial GPE} = \text{final KE}$$
$$mgh = \dfrac{1}{2}mv_f^2$$

Along the track, we might expect $GPE+KE$ to be constant; or perhaps to 
reflect small losses due to friction in real, measured data.

Another problem may be apply the first law[^snofthermo] to estimate how much energy
was lost to friction (or how much work was done on a system) in moving
from an initial state to a final state. 

[^snofthermo]: of thermodynamics 

$$\text{initial GPE} - \text{work done} = \text{final KE}$$
$$mgh - \Delta W = \dfrac{1}{2}mv_f^2$$

Energy is traded back and forth between potential and kinetic energy in
cases such as simple harmonic motion, vibration, etc. In perfectly
elastic systems, the energy can be traded back and forth indefinitely;
most real systems have loss and as a result, vibrations may die out
after some time[^snvibedieout].

[^snvibedieout]: This is sometimes desirable in cases like car suspensions, skis, musical instruments when playing staccato notes, etc...

Energy is **not** conserved during inelastic collisions (energy of
system decreases) nor during explosions (energy of system increases).
