from .base_processor import BaseProcessor


class CommandLineInputDateProcessor(BaseProcessor):
    USER_INPUT_FIELDS = {
        'output_file_path': 'Output file path: ',
        'location_name': 'Location: ',
        'date': 'Date (MM/DD/YYYY): ',
        'start_time': 'Start Time (HH:MM AM/PM): ',
        'state/province': 'State Code: ',
        'protocol': 'Protocol: ',
        'number_of_observers': "Number of observers: ",
        'duration': 'Duration (minutes): ',
        'all_observations_reported': 'All observations reported?: ',
        'effort_distance_miles': 'Distance in Miles: ',
    }

    def obtain_user_inputs(self):
        # obtaining specie list
        lightroom_raw_data = input('Lightroom\'s raw keyword data: ')
        specie_list = BaseProcessor.create_specie_list(lightroom_raw_data)
        inputs = {'common_names': specie_list}
        # obtaining other values
        for key, user_input_text in enumerate(self.USER_INPUT_FIELDS):
            inputs[key] = input(user_input_text)
        return inputs

    def run(self):
        inputs = self.obtain_user_inputs()
        self.fill_input_constant(inputs)
        BaseProcessor.export_data(inputs)
