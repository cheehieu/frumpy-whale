# frumpy-whale

This project was inspired by Intuitive Machine's TRaVeller Terrestrial Return Vehicle (TRV) spacecraft, and the suggested project statement to "let a user know if TRV is visible from their current location."

It pulls in real-time telemetry data from the TRV, and integrates it with the Android [Sky Map](https://code.google.com/p/stardroid/) open source project. 

* Google Sky Maps
* Stellarium running on virtual server, takes in user's location (long, lat) as input, returns 180-degree FOV image of night sky with TRV super imposed corresponding to real-time location
* * artificial satellites, including the International Space Station

# Data Params
*  GMT_timestamp
*  AFM_MET_time: Mission Elapsed Time
*  AFM_upp_time: GPS time epoch in seconds (since Jan 6, 1980)
*  AFM_fdir_gps_fail_flag: flag indicating GPS failure
*  AFM_fdir_strike_count_gps: # of consecutive GPS failures
*  AFM_fdir_loss_of_gps: flag indicating loss of GPS
*  UPP_ecef_longitude: longitude
*  UPP_ecef_gd_latitude: geodetic latitude
*  UPP_ecef_gd_altitude: geodetic altitude
*  UPP_esef_ground_ref_0_R_sc_cg_wrt_gp_ECEF_0
*  UPP_esef_ground_ref_0_R_sc_cg_wrt_gp_ECEF_1
*  UPP_esef_ground_ref_0_R_sc_cg_wrt_gp_ECEF_2
*  UPP_esef_flight_path_angle


