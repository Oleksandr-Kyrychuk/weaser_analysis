import os
import cdsapi

client = cdsapi.Client()
output_dir = 'era5_land_data'
os.makedirs(output_dir, exist_ok=True)

for year in range(2020, 2026):  # 2020 по 2025 включно
    for month in range(1, 13):
        print(f"Починаю завантаження за {year}-{str(month).zfill(2)}")

        filename = os.path.join(output_dir, f'era5_land_{year}_{str(month).zfill(2)}.nc')

        try:
            client.retrieve(
                'reanalysis-era5-land',
                {
                    'variable': [
                        '2m_temperature',
                        'total_precipitation',
                        # 'surface_pressure',  # прибрав для економії місця
                        # '10m_u_component_of_wind',
                        # '10m_v_component_of_wind',
                        # '2m_dewpoint_temperature',
                        # 'snow_depth',
                    ],
                    'year': str(year),
                    'month': str(month).zfill(2),
                    'day': [str(d).zfill(2) for d in range(1, 32)],
                    'time': ['00:00', '12:00'],
                    'format': 'netcdf',
                },
                filename
            )
            print(f"Завантаження за {year}-{str(month).zfill(2)} завершено!")
        except Exception as e:
            print(f"Помилка завантаження за {year}-{str(month).zfill(2)}: {e}")
