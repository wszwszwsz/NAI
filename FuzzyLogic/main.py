"""
Authors: Tomasz Mnich, Wojciech Szypelt
==========================================
Fuzzy Control Systems: The Fan Speed
==========================================
If you're new to the world of fuzzy control systems, you might want
to check out the `Fuzzy Control Primer
<../userguide/fuzzy_control_primer.html>`_
-------------------
Let's create a fuzzy control system which models how fast fan would work.
We would formulate this problem as:
* Antecedents (Inputs)
   - `gpu_temperature`
      *  What is the temperature of the graphics processor on a scale of 0 to 80
      * Fuzzy set (fuzzy value range): low, medium, high
   - `cpu_temperature`
      *  What is the temperature of the computer processor on a scale of 0 to 75
      * Fuzzy set (fuzzy value range): low, medium, high
   - `gpu_load`
      *  What is the load on the graphics processor on a scale of 0 to 100
      * Fuzzy set (fuzzy value range): low, medium, high
   - `cpu_load`
      *  What is the load on the computer processor on a scale of 0 to 100
      * Fuzzy set (fuzzy value range): low, medium, high

* Consequents (Outputs)
   - `fan_speed`
      * What is the fan speed of 0 to 100
      * Fuzzy set (fuzzy value range): low, medium, high
* Rules

     Gpu Temperature  	Cpu Temperature     gpu_load       cpu_load         Fan Speed
        high	or	        high       or     high	  or     high    THEN     high
     Gpu Temperature  	Cpu Temperature     gpu_load       cpu_load         Fan Speed
        medium	or	        medium     or     medium  or     medium  THEN    medium
     Gpu Temperature  	Cpu Temperature     gpu_load       cpu_load         Fan Speed
        low 	or	        low        or     low	  or     low     THEN     low

Creating the Fan Controller Using the skfuzzy control API
-------------------------------------------------------------
We can use the `skfuzzy` control system API to model this.  First, let's
define fuzzy variables
"""
import numpy as np
import skfuzzy as fuzz
import matplotlib
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership
# functions
gpu_temperature = ctrl.Antecedent(np.arange(0, 81, 1), 'gpu_temperature')
cpu_temperature = ctrl.Antecedent(np.arange(0, 76, 1), 'cpu_temperature')
gpu_load = ctrl.Antecedent(np.arange(0, 101, 1), 'gpu_load')
cpu_load = ctrl.Antecedent(np.arange(0, 101, 1), 'cpu_load')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')


# Custom membership functions can be built interactively with a familiar,
# Pythonic API
gpu_temperature['low'] = fuzz.trimf(gpu_temperature.universe, [0, 0, 40])
gpu_temperature['medium'] = fuzz.trimf(gpu_temperature.universe, [0, 55, 80])
gpu_temperature['high'] = fuzz.trimf(gpu_temperature.universe, [55, 80, 80])

cpu_temperature['low'] = fuzz.trimf(cpu_temperature.universe, [0, 0, 40])
cpu_temperature['medium'] = fuzz.trimf(cpu_temperature.universe, [0, 52, 75])
cpu_temperature['high'] = fuzz.trimf(cpu_temperature.universe, [52, 75, 75])

gpu_load['low'] = fuzz.trimf(gpu_load.universe, [0, 0, 50])
gpu_load['medium'] = fuzz.trimf(gpu_load.universe, [0, 50, 100])
gpu_load['high'] = fuzz.trimf(gpu_load.universe, [50, 100, 100])

cpu_load['low'] = fuzz.trimf(cpu_load.universe, [0, 0, 50])
cpu_load['medium'] = fuzz.trimf(cpu_load.universe, [0, 50, 100])
cpu_load['high'] = fuzz.trimf(cpu_load.universe, [50, 100, 100])

fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 25])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [0, 50, 100])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [25, 100, 100])


"""
To help understand what the membership looks like, use the ``view`` methods.
These return the matplotlib `Figure` and `Axis` objects. They are persistent
as written in Jupyter notebooks; other environments may require a `plt.show()`
command after each `.view()`.
"""
gpu_temperature.view()
cpu_temperature.view()
gpu_load.view()
cpu_load.view()
fan_speed.view()

"""
Now, to make these triangles useful, we define the *fuzzy relationship*
between input and output variables. For the purposes of our example, consider
three simple rules:
"""
rule01 = ctrl.Rule(gpu_temperature['low'] | gpu_load['low'] | cpu_temperature['low'] | cpu_load['low'], fan_speed['low'])
rule02 = ctrl.Rule(gpu_temperature['medium'] | gpu_load['medium'] | cpu_temperature['medium'] | cpu_load['medium'], fan_speed['medium'])
rule03 = ctrl.Rule(gpu_temperature['high'] | gpu_load['high'] | cpu_temperature['high'] | cpu_load['high'], fan_speed['high'])

"""
Now that we have our rules defined, we can simply create a control system
via:
"""
fan_ctrl = ctrl.ControlSystem([rule01, rule02, rule03])

speeding = ctrl.ControlSystemSimulation(fan_ctrl)

"""
We can now simulate our control system by simply specifying the inputs
and calling the ``compute`` method.
"""
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
speeding.input['gpu_temperature'] = 0
speeding.input['cpu_temperature'] = 0
speeding.input['gpu_load'] = 0
speeding.input['cpu_load'] = 0

# Crunch the numbers
speeding.compute()

"""
Once computed, we can view the result as well as visualize it.
"""
print(speeding.output['fan_speed'])
fan_speed.view(sim=speeding)