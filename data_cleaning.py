import pandas
import tts


def data_cleaning(file, output_file):
    tts.speak("Getting Data", print_text=True)
    data_frame = pandas.read_csv(file)
    tts.speak("Done Getting Data", print_text=True)

    tts.speak("Cleaning Data In Progress", print_text=True)
    del data_frame["hyperlink"]
    del data_frame["temp_planet_date"]
    del data_frame["temp_planet_mass"]
    del data_frame["pl_letter"]
    del data_frame["pl_name"]
    del data_frame["pl_controvflag"]
    del data_frame["pl_pnum"]
    del data_frame["pl_orbper"]
    del data_frame["pl_orbpererr1"]
    del data_frame["pl_orbpererr2"]
    del data_frame["pl_orbperlim"]
    del data_frame["pl_orbsmax"]
    del data_frame["pl_orbsmaxerr1"]
    del data_frame["pl_orbsmaxerr2"]
    del data_frame["pl_orbsmaxlim"]
    del data_frame["pl_orbeccen"]
    del data_frame["pl_orbeccenerr1"]
    del data_frame["pl_orbeccenerr2"]
    del data_frame["pl_orbeccenlim"]
    del data_frame["pl_orbinclerr1"]
    del data_frame["pl_orbinclerr2"]
    del data_frame["pl_orbincllim"]
    del data_frame["pl_bmassj"]
    del data_frame["pl_bmassjerr1"]
    del data_frame["pl_bmassjerr2"]
    del data_frame["pl_bmassjlim"]
    del data_frame["pl_bmassprov"]
    del data_frame["pl_radj"]
    del data_frame["pl_radjerr1"]
    del data_frame["pl_radjerr2"]
    del data_frame["pl_radjlim"]
    del data_frame["pl_denserr1"]
    del data_frame["pl_denserr2"]
    del data_frame["pl_denslim"]
    del data_frame["pl_ttvflag"]
    del data_frame["pl_kepflag"]
    del data_frame["pl_k2flag"]
    del data_frame["pl_nnotes"]
    del data_frame["ra"]
    del data_frame["dec"]
    del data_frame["st_dist"]
    del data_frame["st_disterr1"]
    del data_frame["st_disterr2"]
    del data_frame["st_distlim"]
    del data_frame["gaia_dist"]
    del data_frame["gaia_disterr1"]
    del data_frame["gaia_disterr2"]
    del data_frame["gaia_distlim"]
    del data_frame["st_optmag"]
    del data_frame["st_optmagerr"]
    del data_frame["st_optmaglim"]
    del data_frame["st_optband"]
    del data_frame["gaia_gmag"]
    del data_frame["gaia_gmagerr"]
    del data_frame["gaia_gmaglim"]
    del data_frame["st_tefferr1"]
    del data_frame["st_tefferr2"]
    del data_frame["st_tefflim"]
    del data_frame["st_masserr1"]
    del data_frame["st_masserr2"]
    del data_frame["st_masslim"]
    del data_frame["st_raderr1"]
    del data_frame["st_raderr2"]
    del data_frame["st_radlim"]
    del data_frame["rowupdate"]
    del data_frame["pl_facility"]
    tts.speak("Data Cleaned", print_text=True)

    tts.speak("Renaming Columns", print_text=True)
    data_frame = data_frame.rename({
        'pl_hostname': "solar_system_name",
        'pl_discmethod': "planet_discovery_method",
        'pl_orbincl': "planet_orbital_inclination",
        'pl_dens': "planet_density",
        'ra_str': "right_ascension",
        'dec_str': "declination",
        "st_teff": "host_temperature",
        'st_mass': "host_mass",
        'st_rad': "host_radius"
    }, axis='columns')
    tts.speak("Done Renaming Columns", print_text=True)

    tts.speak("Creating Output", print_text=True)
    data_frame.to_csv(output_file)
    tts.speak("Output file is ready", print_text=True)
