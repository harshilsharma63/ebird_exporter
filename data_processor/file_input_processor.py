from .base_processor import BaseProcessor


class FileInputDataProcessor(BaseProcessor):
    def run(self, *args, **kwargs):
        input_file_path = kwargs.get('input_file_path')
        records = self.__generate_records(input_file_path)
        self.__export_records(records)

    def __generate_records(self, input_file_path):
        records = []
        with open(input_file_path) as input_file:
            record = {}
            for line in input_file:
                line = line[:-1]  # removing EOL character
                if line == '':
                    BaseProcessor.fill_input_constant(record, file=True)
                    records.append(record)
                    record = {}
                    # self.__save_record(record, records)
                else:
                    components = line.split('$$')
                    key = components[0]
                    value = components[1]
                    if key == 'common_names':
                        value = BaseProcessor.create_specie_list(value)
                    record[key] = value
            # self.__save_record(record, records)
            BaseProcessor.fill_input_constant(record, file=True)
            records.append(record)
        return records

    def __export_records(self, records):
        for record in records:
            BaseProcessor.export_data(record)
