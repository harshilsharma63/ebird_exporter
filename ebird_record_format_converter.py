#!/usr/bin/python3
import sys
import data_processor


def main():
    processor = data_processor.FileInputDataProcessor()
    processor.run(input_file_path='/home/harshilsharma/Downloads/2016.txt')
    # if sys.argv[1] == '-f':
    #     input_file_path = sys.argv[2]
    #     processor = data_processor.FileInputDataProcessor()
    #     processor.run(input_file_path=input_file_path)
    # else:
    #     processor = data_processor.CommandLineInputDateProcessor()
    #     processor.run()


if __name__ == '__main__':
    main()
