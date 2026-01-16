**1)	Project overview**<br />
-----------------------------
**Main business question:**<br />
*How can energy system operators minimize hydrogen storage capacity while maximizing renewable energy utilization?*<br /><br />

This project analyzes a local energy supply chain combining renewable electricity generation, hydrogen production, storage, and distribution. The objective is to determine how much hydrogen storage capacity is required under different system configurations, and to what extent hydrogen injection into the natural gas network can reduce that requirement.<br /><br />

Using a simulation model built in **Python and Excel**, I evaluate trade-offs between:<br />
- Renewable energy curtailment<br />
- Hydrogen storage capacity<br />
- Hydrogen injection thresholds<br />
- System flexibility options<br /><br />

The results provide data-driven guidance for capacity planning and investment decisions for Distribution System Operators (DSOs), energy planners, and infrastructure investors.<br /><br />

**2)	North Star Metrics and Dimensions**<br />
-----------------------------
Core decision metrics<br />
- Required hydrogen buffer size (kg)<br />
- Renewable energy utilization (%)<br />
- Hydrogen injected vs. stored (%)<br />
- Total hydrogen injected (kg)<br /><br />

Key dimensions<br />
- Injection threshold: 0%, 3%, 10%, 20% of hourly natural gas load<br />
- Renewable mix: Wind vs. PV capacity (multiple penetration levels)<br />
- Export constraints: 0 / 250 / 500 kWh allowed grid export<br />
- Operational flexibility: Indirect injection from storage (yes/no)<br />
- Time: Hourly resolution over a full year (2020)<br /><br />

**3)	Data & Model Preperation**<br />
-----------------------------
This project models a realistic energy supply chain using hourly time-series data and physical conversion constraints.<br /><br />

**Data inputs**<br />
- Wind generation (power curve–based, hourly wind speeds)<br />
- PV generation (solar radiation–based)<br />
- Electricity demand profiles<br />
- Natural gas demand profiles<br />
**Model features**<br />
- Electrolyzer & fuel cell conversion logic<br />
- Hydrogen storage inventory tracking<br />
- Injection constraints linked to gas demand<br />
- Priority-based flow decisions (export → injection → storage)<br />
**Tools & Methods**<br />
- Python (simulation logic, scenario execution)<br />
- Excel (simulation logic, scenario execution)<br />
- Scenario analysis & sensitivity analysis<br /><br />

**4)	Summary of Insights**<br />
-----------------------------
**Renewable Mix Insights**<br />
- Wind-heavy systems require significantly larger hydrogen buffers than PV-heavy systems due to short-duration generation peaks<br />
- Hydrogen injection is most effective in wind-dominated systems, especially at higher injection thresholds<br /><br />

*Implication: Injection delivers the highest flexibility value when variability is high.*<br /><br />

**Injection Threshold Trade-offs**<br />
- 3% injection: Limited impact on peak storage reduction<br />
- 10% injection: Strong storage reduction, but highly dependent on operational flexibility<br />
- 20% injection: Largest and most stable reduction in required storage<br /><br />

*Implication: Strong reduction in required hydrogen storage size when increasing the hydrogen injection percentage*<br /><br />

**Export vs. Injection**<br />
- Allowing grid export reduces storage, but at high injection levels (10-20%) export competes with injection and its effectiveness is reduced<br />
- Injection adds most value when export is constrained<br /><br />

*Implication: Helps reduce excess in energy supply though limited functionality when the hydrogen injection percentage is increased*<br /><br />

**Operational Flexibility (Risk Lens)**<br />
- Disallowing indirect injection from storage significantly increases required buffer size<br />
- Especially critical under 10% injection, where consecutive generation peaks occur<br /><br />

*Implication: Operational flexibility has a huge advantage on the eventual maximum storage size required*<br /><br />

**4)	Recommendations & Next Steps**<br />
-----------------------------
**Answer to main business question:**<br />
*Hydrogen injection can substantially reduce required storage capacity when perofrming within a system that operates under the right characteristics while guaranteeing operational flexibility.*<br /><br />

**Strategic Recommendations**<br />
- Prioritize injection in wind-heavy systems: Highest impact on storage reduction<br />
- Target 10% injection as a practical baseline thanks to a balance between infrastructure feasibility and flexibility gains<br />
- Avoid over-investing in storage alone due to diminishing marginal returns<br />
- Preserve operational flexibility as indirect injection capabilities significantly reduces storage requirements<br />
- Use scenario-based planning: optimal configurations depend on the renewable energy mix, export limits, and demand patterns


