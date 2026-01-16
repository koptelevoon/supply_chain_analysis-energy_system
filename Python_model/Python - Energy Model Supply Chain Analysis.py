import datetime

import numpy as np
import csv

import graphs
import model

##Fixed parameters
yearly_power_demand = 28170     #The total load of electricity for the full year
full_load_hours = 950           #Full-load hours of solar
kwh_kg = 40                     #Conversion parameter to calculate between kWh and kg hydrogen
m3_kg = 11.126                  #Conversion parameter to calculate between m3 natural gas and kg hydrogen
e_efficiency = 70               #The efficiency level of the electrolyzer [%]
fc_efficiency = 70              #The efficiency level of the fuel cell [%]

##Experimental parameters
m_injection = 20                 #The maximum allowed injection rate [% of natural gas load]
amount_turbines = 1             #The amount of 4.2 MW Enercon E-126 EP4 wind turbines
solar_pen = 4.2                 #The capacity of PV [MW]
m_export = 0                    #The maximum hourly allowed export quantity [kWh]
indirect_allowed = 0            #Write 1 if injection from the buffer is allowed. Write 0 if indirect injection is not allowed


## Input variables
wind_gen = []                   #Wind generation [kWh] for each hour of the year
sol_gen = []                    #PV generation [kWh] for each hour of the year
RES_gen = []                    #The total of wind and PV generation [kWh] for each hour of the year
local_power_demand = []         #The electricity load for each hour of the year

## Decision variables
dir_dem_sat = []                #The flow of hourly generated wind and PV that directly satisfies the electricity load for each hour of the year [kWh]
exported = []                   #The flow of excess wind and PV that is exported to the giher-voltage grid for each hour of the year [kWh]
imported = []                   #The flow of imported power from the higher-voltage grid for each hour of the year [kWh]
dir_injected = []               #The flow of generated hydrogen directly headed for injection for each hour of the year [kg hydrogen]
stored = []                     #The flow of generated hydrogen headed for the hydrogen buffer for each hour of the year [kg hydrogen]
indir_injected = []             #The flow of hydrogen that is injected indirectly from the buffer for each hour of the year [kg hydrogen]
reconverted = []                #The flow of hydrogen that is reconverted to satisy the excess electricity laod for each hour of the year [kg hydrogen]
tot_injected = []               #The total flow of direct and indirect injection for each hour of the year [kg hydrogen]

## Objective variable
kg_storage = []                 #The amount of hydrogen residing within the buffer for each hour of the year [kg hydrogen]


dates = []
times = []


if __name__ == '__main__':

    #The first part of the code extracts and filters data to retrieve the correct data on wind power generation, solar power generation, and local power demand for each hour of the year
    #Hereby, the code makes use of the calc_data.csv file which contains: The data and corresponding time of the hour, the average wind speed [m/s], the relative fractions of solar radiation, and the electricity demand profile fractions
    #The powercurve.csv file is used to calculate wind power generation for each wind power speed [m/s]

    with open('calc_data.csv') as data:
        reformeddata = []
        dataset = csv.reader(data, delimiter=';')
        list_dataset = list(dataset)
        powercurve = np.genfromtxt('powercurves.csv', delimiter=';')

        for row in list_dataset:
            date = row[0].split("-")
            time = row[1].split(":")
            dates.append(datetime.datetime(int(date[2]), int(date[1]), int(date[0]), int(time[0]), int(time[1])))
            row[2] = int(row[2])
            row[3] = float(row[3])
            row[4] = float(row[4])
            row[5] = int(row[5])
            wind_gen.append(model.calc_wind_power(amount_turbines, row[2], powercurve))
            sol_gen.append(model.calc_sol_gen(solar_pen, full_load_hours, row[3]))
            local_power_demand.append(model.calc_local_power_demand(yearly_power_demand, row[4]))

    #The calculations make use of the formulas from the model.py file
    #The first hour of the year is calculated seperately as the calculations for reconverted and indirect injection start from the second hour

        dir_dem_sat.append(model.calc_dir_dem_satisfac(local_power_demand[0], wind_gen[0], sol_gen[0]))
        exported.append(model.calc_exported(wind_gen[0], sol_gen[0], dir_dem_sat[-1], m_export))
        dir_injected.append(model.calc_dir_injected(wind_gen[0], sol_gen[0], local_power_demand[0], dir_dem_sat[-1], exported[-1], list_dataset[0][5], m_injection, e_efficiency, kwh_kg, m3_kg))
        stored.append(model.calc_stored(wind_gen[0], sol_gen[0], dir_dem_sat[-1], exported[-1], dir_injected[-1], kwh_kg, e_efficiency))
        reconverted.append(0)
        indir_injected.append(float(0))
        imported.append(model.calc_imported(local_power_demand[0], dir_dem_sat[-1], reconverted[-1], kwh_kg, fc_efficiency))
        kg_storage.append(model.calc_storage_first(stored[-1], reconverted[-1], indir_injected[-1]))

    #Now the complete set of calculations are made for each hour of the year

        for (dataset_row, wind_gen_row, sol_gen_row, local_power_demand_row) in zip(list_dataset[1:], wind_gen[1:], sol_gen[1:], local_power_demand[1:]):
            dir_dem_sat.append(model.calc_dir_dem_satisfac(local_power_demand_row, wind_gen_row, sol_gen_row))
            exported.append(model.calc_exported(wind_gen_row, sol_gen_row, dir_dem_sat[-1], m_export))
            dir_injected.append(model.calc_dir_injected(wind_gen_row, sol_gen_row, local_power_demand_row, dir_dem_sat[-1], exported[-1], dataset_row[5], m_injection, e_efficiency, kwh_kg, m3_kg))
            stored.append(model.calc_stored(wind_gen_row, sol_gen_row, dir_dem_sat[-1], exported[-1], dir_injected[-1], kwh_kg, e_efficiency))
            indir_injected.append(float(model.calc_indir_injected(indirect_allowed, dir_injected[-1], dataset_row[5], m3_kg, m_injection, kg_storage[-1])))
            reconverted.append(model.calc_reconverted(kg_storage[-1], indir_injected[-1], fc_efficiency, local_power_demand_row, dir_dem_sat[-1], kwh_kg))
            imported.append(model.calc_imported(local_power_demand_row, dir_dem_sat[-1], reconverted[-1], kwh_kg, fc_efficiency))
            kg_storage.append(model.calc_storage(kg_storage[-1], stored[-1], reconverted[-1], indir_injected[-1]))

        tot_injected.extend([x + y for x, y in zip(dir_injected, indir_injected)])
        RES_gen.extend([x + y for x, y in zip(wind_gen, sol_gen)])


    #The following variables were made to obtain graphs oon the period of 20-23 April, necessary to explain the results from the indirect injection scenario

        RES_gen_20april_23april = RES_gen[2640:2736]
        kg_storage_20april_23april = kg_storage[2640:2736]
        dates_20april_23april = dates[2640:2736]


    ##Total of input & decision variables
        total_wind = sum(wind_gen)
        total_pv = sum(sol_gen)
        total_exported = sum(exported)
        total_dir_dem_sat = sum(dir_dem_sat)
        total_dir_injected = sum(dir_injected)
        total_indir_injected = sum(indir_injected)
        total_stored = sum(stored)
        total_reconverted = sum(reconverted)
        total_local_power_demand = sum(local_power_demand)
        total_imported = sum(imported)

    ##Output variable calculations
        req_hydrogen_volume = max(kg_storage)
        RES_supply_stored = total_stored * kwh_kg / (e_efficiency/100) / (total_wind + total_pv)
        total_volume_injected = total_dir_injected + total_indir_injected
        RES_supply_injected = (total_dir_injected + total_indir_injected) * kwh_kg / (e_efficiency / 100) / (total_wind + total_pv)


    ##Final output
    print("Required hydrogen buffer capacity:", f'{round(req_hydrogen_volume):,}', "kg")
    print("RES supply stored:", format(RES_supply_stored, ".2%"))
    print("Total volume injected:", f'{round(total_volume_injected):,}', "kg")
    print("RES supply injected:", format(RES_supply_injected, ".2%"))


graphs.createlineChart1500(dates, kg_storage, "date time", "amount stored [kg]", "Hydrogen buffer over timw")