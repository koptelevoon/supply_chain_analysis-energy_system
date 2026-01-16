#Calculation formula for hourly wind power generation

def calc_wind_power(turbines, avg_wind_speed, powercurve):
    if avg_wind_speed == 0:
        return 0
    else:
        return powercurve[avg_wind_speed - 1][1] * turbines


#Calculation formula for hourly PV power generation

def calc_sol_gen(solar_pen, full_load_hours, frac_sol_rad):
    return solar_pen * full_load_hours * frac_sol_rad * 1000


#Calculation formula for Hourly electricity load

def calc_local_power_demand(yearly_power_demand, frac_power_demand):
    return yearly_power_demand * frac_power_demand * 1000


#Calculation formula for hourly flow of wind and PV that directly satisfies the electricity load

def calc_dir_dem_satisfac(local_power_demand, wind_gen, sol_gen):
    if local_power_demand >= wind_gen + sol_gen:
        return wind_gen + sol_gen
    else:
        return local_power_demand


#Calculation formula for hourly flow of power that is exported towards the higher-voltage grid

def calc_exported(wind_gen, sol_gen, dir_dem_satisfac, max_export):
    if wind_gen + sol_gen - dir_dem_satisfac < max_export:
        return wind_gen + sol_gen - dir_dem_satisfac
    else:
        return max_export


#Calculation formula for hourly flow of power that is imported from the higher-voltage grid to satisfy excess load

def calc_imported(local_power_demand, dir_dem_satisfac, reconverted, kwh_kg, fuel_cell_eff):
    if local_power_demand > dir_dem_satisfac + (reconverted * kwh_kg * (fuel_cell_eff/100)):
        return local_power_demand - dir_dem_satisfac - (reconverted * kwh_kg * (fuel_cell_eff/100))
    else:
        return 0


#Calculation formula for hourly generated hydrogen that is directly injected into the natural gas network

def calc_dir_injected(wind_gen, sol_gen, local_power_demand, dir_dem_satisfac, exported, gas_demand, max_inject, electrolyzer_eff, kwh_kg, m3_kg):
    if wind_gen + sol_gen > local_power_demand:
        inject = (wind_gen + sol_gen - dir_dem_satisfac - exported) * (electrolyzer_eff/100) / kwh_kg
    else:
        inject = 0

    if inject < gas_demand / m3_kg * (max_inject/100):
        return (wind_gen + sol_gen - dir_dem_satisfac - exported) * (electrolyzer_eff/100) / kwh_kg
    else:
        return gas_demand / m3_kg * (max_inject/100)


#Calculation formula for hourly generated hydrogen that is stored in the hydrogen buffer

def calc_stored(wind_gen, sol_gen, dir_dem_satisfac, exported, injected, kwh_kg, electrolyzer_eff):
    if wind_gen + sol_gen - dir_dem_satisfac - exported - (injected * kwh_kg / (electrolyzer_eff/100)) > 0:
        return (wind_gen + sol_gen - dir_dem_satisfac - exported - (injected * kwh_kg / (electrolyzer_eff/100))) * (electrolyzer_eff/100) / kwh_kg
    else:
        return 0


#Calculation formula for hourly  flow of hydrogen that is indirectly injected from the buffer

def calc_indir_injected(ind_allowed, injected, gas_demand, m3_kg, max_inject, storage):
    if ind_allowed == 1:
        if injected < gas_demand / m3_kg * (max_inject/100):
            inj_possibility = gas_demand / m3_kg * (max_inject/100) - injected
        else:
            inj_possibility = 0

        if storage >= inj_possibility:
            return inj_possibility
        else:
            return storage
    elif ind_allowed == 0:
        return 0


#Calculation formula for the hourly flow of hydrogen that is reconverted to electricity to satisfy excess electricity load

def calc_reconverted(storage, indir_inj, fuel_cell_eff, local_power_demand, dir_dem_satisfac, kwh_kg):
    if (storage - indir_inj) * kwh_kg * (fuel_cell_eff/100) >= local_power_demand - dir_dem_satisfac:
        quantity = (local_power_demand - dir_dem_satisfac) / (fuel_cell_eff/100) / kwh_kg
    else:
        quantity = storage - indir_inj

    if local_power_demand > dir_dem_satisfac:
        return quantity
    else:
        return 0


#Calculation formula for the amount of hydrogen residing in the buffer at the end of the first hour

def calc_storage_first(stored, reconverted, indir_inj):
    return stored - reconverted - indir_inj


#Calculation formula  for the amount of hydrogen residing in the buffer at the end of each hour

def calc_storage(storage, stored, reconverted, indir_inj):
    return storage + (stored - reconverted - indir_inj)



