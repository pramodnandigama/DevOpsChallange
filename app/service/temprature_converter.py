import enum


def fconv(f_input) -> dict:
    coutput = (((f_input - 32) * 5) / 9)
    koutput = coutput + 273.15
    routput = f_input + 459.67
    return {
        'celsius': coutput,
        'kelvin': koutput,
        'rankine': routput,
        'fahrenheit': f_input
    }


def cconv(c_input) -> dict:
    foutput = (((c_input * 9) / 5) + 32)
    koutput = c_input + 273.15
    routput = foutput + 459.67
    return {
        'fahrenheit': foutput,
        'kelvin': koutput,
        'rankine': routput,
        'celsius': c_input
    }


def kconv(k_input) -> dict:
    coutput = k_input - 273.15
    foutput = (((coutput * 9) / 5) + 32)
    routput = foutput + 459.67
    return {
        'celsius': coutput,
        'fahrenheit': foutput,
        'rankine': routput,
        'kelvin': k_input
    }


def rconv(r_input) -> dict:
    foutput = r_input - 459.67
    coutput = (((foutput - 32) * 5) / 9)
    koutput = coutput + 273.15
    return {
        'fahrenheit': foutput,
        'celsius': coutput,
        'kelvin': koutput,
        'rankine': r_input
    }


def convert_temperature(temperature_input, input_temperature_type, target_temperature_type) -> int:
    # string lowercase
    if target_temperature_type.lower() not in ['celsius', 'fahrenheit', 'kelvin', 'rankine']:
        return -1
    if input_temperature_type.lower() == "fahrenheit":
        return fconv(temperature_input)[target_temperature_type.lower()]
    elif input_temperature_type.lower() == "celsius":
        return cconv(temperature_input)[target_temperature_type.lower()]
    elif input_temperature_type.lower() == "kelvin":
        return kconv(temperature_input)[target_temperature_type.lower()]
    elif input_temperature_type.lower() == "rankine":
        return rconv(temperature_input)[target_temperature_type.lower()]
    else:
        return -1


