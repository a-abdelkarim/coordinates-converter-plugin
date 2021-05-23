class CoordsConverter:
    
    def dm_to_dms(self, latitude, longtude):
        is_lat_positive = int(latitude) >= 0
        is_lon_positive = int(longtude) >= 0

        lat = []
        lon = []

        # calc lat
        lat_degree = int(latitude)
        lat_minut = int( ( latitude - lat_degree ) * 60 )
        z_lat = ( float(latitude) - lat_degree ) - ( lat_minut / 60 )
        c_lat = 3600
        lat_sec = float( z_lat * c_lat )

        lat.append(lat_degree); lat.append(lat_minut); lat.append(round(lat_sec, 3))


        # calc long
        lon_degree = int(longtude)
        lon_minut = int( ( longtude - lon_degree ) * 60 )
        z_lon = ( float(longtude) - lon_degree ) - ( lon_minut / 60 )
        c_lon = 3600
        lon_sec = float( z_lon * c_lon )

        lon.append(lon_degree); lon.append(lon_minut); lon.append(round(lon_sec, 3))


        return lat, lon


    def dms_to_dm(self, latitude, longtude):
        # calc latitude
        lat_degree = float(latitude[0])
        lat_minut = float(latitude[1])
        lat_sec = float(latitude[2])

        lat = (lat_degree + (lat_minut)/60) + (lat_sec / 3600)


        # calc longtude
        lon_degree = float(longtude[0])
        lon_minut = float(longtude[1])
        lon_sec = float(longtude[2])

        lon = (lon_degree + (lon_minut)/60) + (lon_sec / 3600)


        return lat, lon
