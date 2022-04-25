# Features

- Adding fixture "classes"/templates to the system
    - e.g. Mac Aura --> modes, weight, poweravg, power max, 5p/3p, powerlinkable
- editing fixture "classes"/templates 
- Linking fixtures to a truss or area
- Linking fixtures to a universe and then signal output
- assigning signal outputs to a universe
    - Signal outputs has ---> 5p/3p, universe


## Preliminary class structure: 


```
fixture_template:
    modes
    weight
    poweravg
    power max
    5p/3p
    powerlinkable
    dim/nondim
    name

fixture:
    type(fixture_template)
    address
    truss
    universe
    signal_out
    power_out
    ID


signal_output:
    5p/3p/other
    universe
    ID

power_output
    ID
    type(soca/single)
    dim/nondim
    truss/are.ID


truss: 
    ID
    fixtures [fixture.ID]
    signal_outputs [signal_output.ID]
    power_outputs [power_out.ID]

```