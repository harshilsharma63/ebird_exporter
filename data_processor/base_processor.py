from datetime import datetime

import utils


class BaseProcessor:
    EXCLUDED_SPECIES = ['edited', 'id help', '']
    COUNTRY_CODE = 'IN'
    EXPORT_FILE_COLUMN_ORDER = ['genus', 'species', 'number', 'species_comments', 'location_name', 'latitude',
                                'longitude', 'date', 'start_time', 'state/province', 'country_code', 'protocol',
                                'number_of_observers', 'duration', 'all_observations_reported', 'effort_distance_miles',
                                'effort_area_acres', 'submission_comments']
    GENERATED_FILE_NAME = None

    @staticmethod
    def compute_duration(start_time, end_time):
        start = datetime.strptime(start_time, '%I:%M %p')
        end = datetime.strptime(end_time, '%I:%M %p')
        delta = end - start
        return int(round(delta.seconds / 60))

    @staticmethod
    def create_specie_list(lightroom_raw_species_string):
        specie_list = lightroom_raw_species_string.split('*, ')
        last = len(specie_list) - 1
        specie_list[last] = specie_list[last][:-1]
        return specie_list

    @staticmethod
    def generate_export_file_name():
        if BaseProcessor.GENERATED_FILE_NAME is None:
            BaseProcessor.GENERATED_FILE_NAME = utils.format_filename("%s.csv" % str(datetime.now()))
        return BaseProcessor.GENERATED_FILE_NAME

    @staticmethod
    def fill_input_constant(inputs, file=False):
        inputs['genus'] = ''
        inputs['species'] = ''
        inputs['number'] = 'x'
        inputs['species_comments'] = ''
        inputs['latitude'] = ''
        inputs['longitude'] = ''
        inputs['country_code'] = BaseProcessor.COUNTRY_CODE
        inputs['effort_area_acres'] = ''
        inputs['submission_comments'] = ''
        if file:
            inputs['output_file_path'] = BaseProcessor.generate_export_file_name()
            inputs['duration'] = str(BaseProcessor.compute_duration(inputs['start_time'], inputs['end_time']))

    @staticmethod
    def export_data(inputs):
        species = inputs['common_names']
        output_file_path = inputs.get('output_file_path')
        with open(output_file_path, 'a') as output_file:
            for specie in species:
                if specie not in BaseProcessor.EXCLUDED_SPECIES:
                    output_file.write(specie)
                    for column in BaseProcessor.EXPORT_FILE_COLUMN_ORDER:
                        output_file.write(',' + inputs.get(column))
                    output_file.write('\n')
