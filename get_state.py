def change_state(location):
    if location.lower() in ["baden-Württemberg", "Baden Württemberg", "BW"]:
        location = "BW"
    elif location.lower() in ["bayern", "by"]:
        location = "BY"
    elif location.lower() in ["berlin", "be"]:
        location = "BE"
    elif location.lower() in ["brandenburg", "bb"]:
        location = "BB"
    elif location.lower() in ["bremen", "hb"]:
        location = "HB"
    elif location.lower() in ["hamburg", "hh"]:
        location = "HH"
    elif location.lower() in ["hessen", "he"]:
        location = "HE"
    elif location.lower() in [
        "mecklenburg-vorpommern",
        "mecklenburg vorpommern",
        "mv",
    ]:
        location = "MV"
    elif location.lower() in ["niedersachsen", "ni"]:
        location = "NI"
    elif location.lower() in [
        "nordrhein-westfalen",
        "nordrhein westfalen",
        "nrw",
        "nw",
    ]:
        location = "NW"
    elif location.lower() in ["rheinland-pfalz", "rheinland pfalz", "rp"]:
        location = "RP"
    elif location.lower() in ["saarland", "sl"]:
        location = "SL"
    elif location.lower() in ["sachsen", "sn"]:
        location = "SN"
    elif location.lower() in ["sachsen-anhalt", "sachsen anhalt", "st"]:
        location = "ST"
    elif location.lower() in ["schleswig-holstein", "schleswigh holstein", "sh"]:
        location = "SH"
    elif location.lower() in ["thüringen", "th"]:
        location = "TH"
    else:
        return "error"

    return location